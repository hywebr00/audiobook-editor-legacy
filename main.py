# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:18:02 2021
"""

import json
import logging
from multipledispatch import dispatch
import sys
# import ctypes
import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from loadingwidget import LoadingWidget
from startingpanel import StartingPanel
from startingpanelwithopenedlist import StartingPanelWithOpenedList
from createnewwizard import CreateNewWizard
from mainwindow import MainWindow
from book import Audiobook, Helper

# import resources_rc

DISPLAY_ON_SCREEN = 1

ORGANIZATION_NAME = "Hyweb Technology Co., LTD."
ORGANIZATION_DOMAIN = "hyweb.com.tw"
APPLICATION_NAME = "Audiobook Editor"
APPLICATION_VERSION = "0.7.0"


class Controller(QObject):
    signal_switch_to_mainwindow = Signal(str)

    _translate = QCoreApplication.translate

    def __init__(self):
        super().__init__()
        self.loadingWidget = None
        self.settings = None
        self.recentFilesOrDirectoriesInSettings = None
        self.startingPanel = None
        self.createNewWizard = None
        self.book = None
        self.mainWindow = None

    def show_LoadingWidget(self):
        self.loadingWidget = LoadingWidget()
        # app = QApplication.instance()
        # desktop = QApplication.instance().desktop()
        # displayScreenGeometry = QApplication.instance().desktop().screenGeometry(DISPLAY_ON_SCREEN)
        self.loadingWidget.move(QApplication.instance().desktop().screenGeometry(DISPLAY_ON_SCREEN).center().x() -
                                self.loadingWidget.size().width() / 2,
                                QApplication.instance().desktop().screenGeometry(DISPLAY_ON_SCREEN).center().y() -
                                self.loadingWidget.size().height() / 2)
        self.loadingWidget.switch_window.connect(self.show_StartingPanel)
        self.loadingWidget.show()

    def show_StartingPanel(self):
        self.settings = QSettings()
        self.recentFilesOrDirectoriesInSettings = self.settings.value('RecentlyOpenedFilesOrDirectories', '', type=str)
        logging.info(self.recentFilesOrDirectoriesInSettings)
        self.recentFilesOrDirectoriesInSettings = self.recentFilesOrDirectoriesInSettings[:-1]
        self.recentFilesOrDirectoriesInSettings = self.recentFilesOrDirectoriesInSettings[1:]
        if len(self.recentFilesOrDirectoriesInSettings) > 0:
            self.recentFilesOrDirectoriesInSettings = [json.loads(obj) for obj in self.recentFilesOrDirectoriesInSettings.split(';')]
        else:
            self.recentFilesOrDirectoriesInSettings = []
        for one in self.recentFilesOrDirectoriesInSettings:
            bookPath = one["bookPath"]
            if not os.path.isfile(bookPath) and not os.path.isdir(bookPath):
                self.recentFilesOrDirectoriesInSettings.remove({"bookPath": one["bookPath"],
                                                                "coverFile": one["coverFile"],
                                                                "bookTitle": one["bookTitle"],
                                                                "lastOpenedDate": one["lastOpenedDate"]})

        self.settings.setValue('RecentlyOpenedFilesOrDirectories',
                               "[" + ";".join([json.dumps(o) for o in self.recentFilesOrDirectoriesInSettings]) + "]")
        if len(self.recentFilesOrDirectoriesInSettings) > 0:
            self.startingPanel = StartingPanelWithOpenedList()
        else:
            self.startingPanel = StartingPanel()

        self.startingPanel.signal_switch_window[bool].connect(self.show_CreateNewWizard)
        self.startingPanel.signal_switch_window[str].connect(self.show_MainWindow)
        self.loadingWidget.close()

        self.startingPanel.move(QApplication.instance().desktop().screenGeometry(DISPLAY_ON_SCREEN).center().x() -
                                self.startingPanel.size().width() / 2,
                                QApplication.instance().desktop().screenGeometry(DISPLAY_ON_SCREEN).center().y() -
                                self.startingPanel.size().height() / 2)

        self.startingPanel.show()

    @Slot(bool)
    def show_CreateNewWizard(self, newOrOpen):
        logging.debug("show_CreateNewWizard")
        if newOrOpen:
            self.createNewWizard = CreateNewWizard()
            self.startingPanel.close()
            self.createNewWizard.switch_window[dict].connect(self.show_MainWindow)

            self.createNewWizard.move(QApplication.instance().desktop().screenGeometry(DISPLAY_ON_SCREEN).center().x() -
                                      self.createNewWizard.size().width() / 2,
                                      QApplication.instance().desktop().screenGeometry(DISPLAY_ON_SCREEN).center().y() -
                                      self.createNewWizard.size().height() / 2)

            self.createNewWizard.show()

    @dispatch(dict)
    def show_MainWindow(self, dict_New):
        logging.debug("show_MainWindow for dict")
        if dict_New == {}:
            self.show_StartingPanel()
        else:
            self.book = Audiobook.getInstance(dict_New)
            logging.debug(dict_New)
            self.mainWindow = MainWindow(dict_New)
            self.mainWindow.setStatusBar(None)
            self.mainWindow.signal_exit.connect(self.exit)
            self.mainWindow.signal_close.connect(self.close)
            self.mainWindow.signal_new.connect(self.new)
            self.mainWindow.signal_open.connect(self.open)

            if hasattr(self, 'createNewWizard'):
                self.createNewWizard.close()

            self.mainWindow.move(QApplication.instance().desktop().screenGeometry(DISPLAY_ON_SCREEN).center().x() -
                                 self.mainWindow.size().width() / 2,
                                 QApplication.instance().desktop().screenGeometry(DISPLAY_ON_SCREEN).center().y() -
                                 self.mainWindow.size().height() / 2)

            self.mainWindow.show()

    @dispatch(str)
    def show_MainWindow(self, item):
        logging.debug("show_MainWindow for str = " + item)

        if item == "":
            return
        self.startingPanel.close()

        self.book = Audiobook.getInstance(item)

        self.mainWindow = MainWindow(self.book)
        self.mainWindow.setStatusBar(None)
        self.mainWindow.signal_exit.connect(self.exit)
        self.mainWindow.signal_close.connect(self.close)

        self.mainWindow.signal_new.connect(self.new)
        self.mainWindow.signal_open.connect(self.open)

        self.mainWindow.move(QApplication.instance().desktop().screenGeometry(DISPLAY_ON_SCREEN).center().x() -
                             self.mainWindow.size().width() / 2,
                             QApplication.instance().desktop().screenGeometry(DISPLAY_ON_SCREEN).center().y() -
                             self.mainWindow.size().height() / 2)

        self.mainWindow.show()

    def exit(self):
        logging.debug("exit")
        if hasattr(self, 'mainWindow'):
            self.mainWindow.close()
            del self.mainWindow

        if hasattr(self, 'book'):
            del self.book

        QCoreApplication.quit()

    def close(self):
        logging.debug('close')
        if hasattr(self, 'mainWindow'):
            self.mainWindow.close()
            del self.mainWindow
            self.show_StartingPanel()
        if hasattr(self, 'book'):
            del self.book

    def new(self):
        logging.debug('new')
        if hasattr(self, 'mainWindow'):
            self.mainWindow.close()
            del self.mainWindow
            self.show_CreateNewWizard(True)

        if hasattr(self, 'book'):
            del self.book
        Audiobook._instance = None

    def open(self):
        logging.debug('open')
        if hasattr(self, 'mainWindow'):
            self.mainWindow.close()
            del self.mainWindow
        if hasattr(self, 'book'):
            del self.book
        Audiobook._instance = None
        self.show_StartingPanel()


def getScreenResolutions():
    logging.debug('getScreenResolutions')
    screenCount = QApplication.instance().desktop().screenCount()
    logging.debug('Desktop DevicePixelRatio = {}'.format(str(QApplication.instance().desktop().devicePixelRatio())))

    global DISPLAY_ON_SCREEN
    if DISPLAY_ON_SCREEN >= screenCount:
        DISPLAY_ON_SCREEN = 0

    primaryScreen = QApplication.primaryScreen()

    for displayNo in range(screenCount):
        screen = QApplication.screens()[displayNo]
        if screen == primaryScreen:
            DISPLAY_ON_SCREEN = displayNo
        size = screen.size()
        logging.debug("Display " +
                      str(displayNo) +
                      " : size = " +
                      str(size.width()) + "*" +
                      str(size.height()) + "\n" +
                      "devicePixelRatio = " +
                      str(screen.devicePixelRatio()) + "\n" +
                      "screenID = " +
                      str(id(screen)) + '\n' + '*' * 20)


def loadApplicationFonts(fontPaths):
    logging.debug('loadApplicationFonts')
    appFontDirs = fontPaths
    for i in appFontDirs:
        fontDir = QDir(i)
        fontFiles = fontDir.entryList(['*.otf', '*.ttf'], QDir.Files, QDir.Name)
        for fontFile in fontFiles:
            fontID = QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                                   os.path.join(i, fontFile)))
            if fontID == -1:
                logging.error("Can\'t load {}!" % fontFile)
            else:
                logging.debug("loaded fontID = {} with {}!".format(str(fontID), fontFile))
                pass


if __name__ == "__main__":
    os.environ['QT_MAC_WANTS_LAYER'] = '1'

    # if sys.platform.startswith('win'):
    #     errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(0)

    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(module)s %(funcName)s %(message)s'
    LOGGING_DATE_FORMAT = '%Y%m%d %H:%M:%S'
    logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT, datefmt=LOGGING_DATE_FORMAT)

    app = QApplication(sys.argv)
    getScreenResolutions()

    app.setOrganizationName(ORGANIZATION_NAME)
    app.setOrganizationDomain(ORGANIZATION_DOMAIN)
    app.setApplicationName(APPLICATION_NAME)
    app.setApplicationVersion(APPLICATION_VERSION)

    settings = QSettings(app.organizationName(),
                         app.applicationName())

    language = settings.value('Language', '')
    installerLanguage = settings.value('InstallerLanguage', '')
    if language != '':
        pass
    elif installerLanguage != '' and language == '':
        language = installerLanguage
    else:
        language = 'EN'

    translator = QTranslator()
    try:
        translator.load(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Language/appLang_' + language + '.qm'))
        app.ui_Language = language
    except Exception as ex:
        logging.error(ex)
        translator.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Language/appLang_EN.qm'))
        app.ui_Language = 'EN'

    settings.setValue('Language', app.ui_Language)
    app.installTranslator(translator)
    app.ui_Translator = translator

    loadApplicationFonts(["Noto_Sans", "Noto_Sans_TC"])

    controller = Controller()
    controller.show_LoadingWidget()

    sys.exit(app.exec_())
