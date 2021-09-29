# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 04:34:20 2021
"""

import logging
from multipledispatch import dispatch
import json
import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_mainwindow import Ui_MainWindow
from metadatawidget import MetadataWidget
from readingorderwidget import ReadingOrderWidget
# from supplementallistitem import SupplementalListWidget
from supplementallistwidgetwithwidgets import SupplementalListWidgetWithWidgets
# from supplementallistwidgettitlebar import SupplementalListWidgetTitleBar
# from attachfromwidgetwithouturl import AttachFromWidgetWithoutURL
from toclistwidget import TOCListWidget
from coverpreviewwidget import CoverPreviewWidget
from book import Audiobook, Helper
from validator import Validator
from alert import Alert, AlertWithButtons
from translucent import MaskWidget


class MainWindow(QMainWindow):
    switch_window = Signal()
    signal_exit = Signal()
    signal_close = Signal()
    signal_new = Signal()
    signal_open = Signal()

    MaxRecentFiles = 10

    @dispatch(Audiobook)
    def __init__(self, book):
        super(MainWindow, self).__init__()

        self.book = book

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate
        # MenuBar CSS
        self.ui.menubar.setStyleSheet(
            'QMenuBar::item { color: #FFFFFF } QMenuBar::item::selected { background: #383838; color: #FFFFFF } '
            'QMenu::item { color: #FFFFFF } QMenu::item::selected { background: #383838; color: #FFFFFF }')
        # MainWindow Title
        self.setWindowTitle(self._translate("MainWindow", "Audiobook Editor"))
        # Set Window Icon
        # self.setWindowIcon(QIcon(':/pic/icon/audiobook-editor-logo.ico'))
        # Hide Minimize & Maximize buttons
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # WindowMinMaxButtonsHint)

        # Magic to make title bar disappear
        self.ui.dockWidget_Left.setTitleBarWidget(QWidget(None))
        self.ui.dockWidget_CoverPreviewWidget.setTitleBarWidget(QWidget(None))
        self.ui.dockWidget_SupplementalList.setTitleBarWidget(QWidget(None))

        layout = QVBoxLayout(self.ui.tab_Metadata)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.metadataWidget = MetadataWidget(self, self.book.ManifestDict)
        layout.addWidget(self.metadataWidget)

        layout = QVBoxLayout(self.ui.dockWidgetContents)
        layout.setContentsMargins(0, 0, 0, 0)
        self.coverPreviewWidget = CoverPreviewWidget(self.book.CoverDict, self.book.BookDir, self)
        layout.addWidget(self.coverPreviewWidget, 1)

        w = QWidget()
        layout = QHBoxLayout(w)
        layout.setContentsMargins(0, 0, 0, 0)
        self.readingOrderWidget = ReadingOrderWidget(self.book.ReadingOrderList, self.book.BookDir, self)
        self.readingOrderWidget.signal_Duration_Changed.connect(self.metadataWidget.onDurationChanged)
        layout.addWidget(self.readingOrderWidget)
        self.setCentralWidget(w)
        self.readingOrderWidget.getDuration()

        layout = QVBoxLayout(self.ui.tab_TOC)
        layout.setContentsMargins(0, 0, 0, 0)
        self.tocWidget = TOCListWidget(self, self.book.TOCList)
        layout.addWidget(self.tocWidget)

        layout = QVBoxLayout(self.ui.dockWidgetContents_2)
        layout.setContentsMargins(0, 0, 0, 0)
        self.supplementalListWidget = SupplementalListWidgetWithWidgets(self.book.SupplementalList, self)
        layout.addWidget(self.supplementalListWidget, 1)

        self.supplementalListWidget.signal_Add_Resource_to_TOC.connect(self.tocWidget.add_Resource_to_TOC_triggered)
        self.readingOrderWidget.signal_Add_Resource_to_TOC.connect(self.tocWidget.add_Resource_to_TOC_triggered)

        self.ui.action_New.triggered.connect(self._new)
        self.ui.action_Open.triggered.connect(self._open)
        self.ui.action_Exit.triggered.connect(self._exit)
        self.ui.action_Save.triggered.connect(self._save)
        self.ui.action_Close.triggered.connect(self._close)
        self.ui.action_Validate.triggered.connect(self._validate)
        self.ui.action_Pack.triggered.connect(self._pack)

        logging.debug(self.supplementalListWidget.ui.listWidget.objectName())
        logging.debug(self.supplementalListWidget.ui.listWidget.geometry())

        logging.debug(self.supplementalListWidget.ui.listWidget.parent().objectName())
        logging.debug(self.supplementalListWidget.ui.listWidget.parent().geometry())

        logging.debug(self.supplementalListWidget.objectName())
        logging.debug(self.supplementalListWidget.geometry())
        logging.debug(self.supplementalListWidget.parent().objectName())
        logging.debug(self.supplementalListWidget.parent().geometry())
        logging.debug(self.supplementalListWidget.parent().parent().objectName())
        logging.debug(self.supplementalListWidget.parent().parent().geometry())

        self.settings = QSettings()
        self.recentFilesOrDirectoriesInSettings = ''

        self.ui.action_EN.triggered.connect(
            lambda: self.changeUILanguage('EN', self.ui.action_EN))
        self.ui.action_TC.triggered.connect(
            lambda: self.changeUILanguage('TC', self.ui.action_TC))

        app = QApplication.instance()
        for action in self.ui.menu_Language.actions():
            if action.objectName() == 'action_' + app.ui_Language:
                action.setChecked(True)
            else:
                action.setChecked(False)

        self.updateSettings()

    @dispatch(dict)
    def __init__(self, dict_New):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate
        # MenuBar CSS
        self.ui.menubar.setStyleSheet(
            'QMenuBar::item { color: #FFFFFF } QMenuBar::item::selected { background: #383838; color: #FFFFFF } '
            'QMenu::item { color: #FFFFFF } QMenu::item::selected { background: #383838; color: #FFFFFF }')
        # MainWindow Title
        self.setWindowTitle('Audiobook Editor')
        # Set Window Icon
        # self.setWindowIcon(QIcon(':/pic/icon/audiobook-editor-logo.ico'))
        # Hide Minimize & Maximize buttons
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # WindowMinMaxButtonsHint)

        # Magic to make title bar disappear
        self.ui.dockWidget_Left.setTitleBarWidget(QWidget(None))
        self.ui.dockWidget_CoverPreviewWidget.setTitleBarWidget(QWidget(None))
        self.ui.dockWidget_SupplementalList.setTitleBarWidget(QWidget(None))

        # self.ui.action_Qt.triggered.connect(self.on_action_Qt_triggered)
        self.book = Audiobook.getInstance()

        layout = QVBoxLayout(self.ui.tab_Metadata)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.metadataWidget = MetadataWidget(self, dict_New)
        layout.addWidget(self.metadataWidget)

        # Magic to make title bar disappear
        self.ui.dockWidget_Left.setTitleBarWidget(QWidget(None))
        self.ui.dockWidget_CoverPreviewWidget.setTitleBarWidget(QWidget(None))
        self.ui.dockWidget_SupplementalList.setTitleBarWidget(QWidget(None))

        layout = QVBoxLayout(self.ui.dockWidgetContents)
        layout.setContentsMargins(0, 0, 0, 0)
        self.coverPreviewWidget = CoverPreviewWidget(self)
        layout.addWidget(self.coverPreviewWidget)

        w = QWidget()
        layout = QHBoxLayout(w)
        layout.setContentsMargins(0, 0, 0, 0)
        self.readingOrderWidget = ReadingOrderWidget(self)
        layout.addWidget(self.readingOrderWidget)
        # layout.addStretch(0)
        self.setCentralWidget(w)

        layout = QVBoxLayout(self.ui.tab_TOC)
        self.tocWidget = TOCListWidget(self)
        layout.addWidget(self.tocWidget)
        self.readingOrderWidget.signal_Add_Resource_to_TOC.connect(self.tocWidget.add_Resource_to_TOC_triggered)
        self.readingOrderWidget.signal_Duration_Changed.connect(self.metadataWidget.onDurationChanged)

        layout = QVBoxLayout(self.ui.dockWidgetContents_2)
        layout.setContentsMargins(0, 0, 0, 0)
        self.supplementalListWidget = SupplementalListWidgetWithWidgets(self)
        layout.addWidget(self.supplementalListWidget)
        self.supplementalListWidget.signal_Add_Resource_to_TOC.connect(self.tocWidget.add_Resource_to_TOC_triggered)

        # self.supplementalListWidget.addItems(1)
        self.ui.action_New.triggered.connect(self._new)
        self.ui.action_Open.triggered.connect(self._open)
        self.ui.action_Exit.triggered.connect(self._exit)
        self.ui.action_Save.triggered.connect(self._save)
        self.ui.action_Close.triggered.connect(self._close)
        self.ui.action_Validate.triggered.connect(self._validate)
        self.ui.action_Pack.triggered.connect(self._pack)

        self.settings = QSettings()
        self.recentFilesOrDirectoriesInSettings = ''

        self.ui.action_EN.triggered.connect(
            lambda: self.changeUILanguage('EN', self.ui.action_EN))
        self.ui.action_TC.triggered.connect(
            lambda: self.changeUILanguage('TC', self.ui.action_TC))

        app = QApplication.instance()
        for action in self.ui.menu_Language.actions():
            if action.objectName() == 'action_' + app.ui_Language:
                action.setChecked(True)
            else:
                action.setChecked(False)

    @Slot()
    def on_action_Qt_triggered(self):
        self.mask = MaskWidget(self)
        self.mask.show()

        QApplication.aboutQt()
        self.mask.close()

    @Slot()
    def on_action_Thanks_triggered(self):
        self._openAlertWindow("backports.tempfile, beautifulsoup4, html5lib, jsonschema, multipledispatch, tinytag,"
                              " PySide2, Python, Qt5, regex, requests, urllib3",
                              self._translate("MainWindow",
                                              "Special thanks"))

    @Slot()
    def on_action_Version_triggered(self):
        app = QApplication.instance()
        self._openAlertWindow("<center>" + self._translate("MainWindow", "Audiobook Editor") + "</center>" +
                              "<center>" + app.applicationVersion() + "</center>" +
                              "<center>" + self._translate("MainWindow", "Hyweb Technology Co., LTD.") + "</center>",
                              self._translate("MainWindow",
                                              "Version information"))

    @Slot()
    def on_action_Issues_triggered(self):
        QDesktopServices.openUrl(QUrl('https://github.com/hywebr00/audiobook-editor/issues'))

    @Slot()
    def on_action_License_triggered(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile('about_licenses.html'))

    def _openAlertWindow(self, str_Msg, str_Title):
        self.mask = MaskWidget(self)
        self.mask.show()

        self.alert = Alert(str_Msg,
                           str_Title)
        self.alert.move(
            self.geometry().x() +
            self.geometry().width() / 2 -
            self.alert.geometry().width() / 2,
            self.geometry().y() +
            self.geometry().height() / 2 -
            self.alert.geometry().height() / 2)

        result = self.alert.exec_()
        self.mask.close()
        return result

    def _exit(self):
        self.signal_exit.emit()

    def _pack(self):

        book = Audiobook.getInstance()
        try:
            self._save(flag_Pack=True)
            book.on_action_Pack_triggered(self)
        except Exception as ex:
            logging.debug("{0}".format(ex))

    def _save(self, flag_Pack=False):
        logging.debug("_save()")

        # required fields should be checked first
        manifest = self.metadataWidget.save()

        if manifest == {}:
            if not flag_Pack:
                return
            else:
                raise Exception('Some necessary fields are empty!')

        toc = self.tocWidget.save()

        if toc == {}:
            if not flag_Pack:
                return
            else:
                raise Exception('Some necessary fields are empty!')

        cover = self.coverPreviewWidget.save()

        readingOrder = self.readingOrderWidget.save()

        supplementalList = self.supplementalListWidget.save()

        logging.debug(manifest)
        self.book.ManifestDict = manifest

        logging.debug(readingOrder)
        self.book.ReadingOrderList = readingOrder

        logging.debug(toc)
        self.book.TOCList = toc

        logging.debug(cover)
        self.book.CoverDict = cover

        logging.debug(supplementalList)
        self.book.SupplementalList = supplementalList
        self.updateSettings()

        self.book.on_action_Save_Audiobook_triggered()

    def refreshToc(self):
        tocList = []
        return tocList

    def refreshManifest(self):
        return {}

    def _new(self):
        """
        toc_refreshed = refreshToc()
        manifest_refreshed = refreshManifest()
        """
        # self.book.on_action_Save_Audiobook_triggered()
        self.updateSettings()
        self.signal_new.emit()

    def updateSettings(self):
        self.settings = QSettings()
        self.recentFilesOrDirectoriesInSettings = self.settings.value('RecentlyOpenedFilesOrDirectories', '', type=str)
        logging.debug(self.recentFilesOrDirectoriesInSettings)
        self.recentFilesOrDirectoriesInSettings = self.recentFilesOrDirectoriesInSettings[:-1]
        self.recentFilesOrDirectoriesInSettings = self.recentFilesOrDirectoriesInSettings[1:]
        if len(self.recentFilesOrDirectoriesInSettings) > 0:
            self.recentFilesOrDirectoriesInSettings = [json.loads(obj) for obj in
                                                       self.recentFilesOrDirectoriesInSettings.split(';')]
        else:
            self.recentFilesOrDirectoriesInSettings = []
        bookPath = self.book.BookDir
        coverFile = self.book.CoverDict
        manifest = self.book.ManifestDict

        logging.debug(bookPath)
        logging.debug(coverFile)
        logging.debug(manifest)

        dict_One = {}

        if self.book.is_LPF:

            dict_One = next((one for one in self.recentFilesOrDirectoriesInSettings if
                             one["bookPath"] == self.book.LPFFilename), None)
            logging.debug(dict_One)
            if dict_One is None:
                self.recentFilesOrDirectoriesInSettings.insert(0, {"bookPath": self.book.LPFFilename,
                                                                   "coverFile": coverFile.get("url", ""),
                                                                   "bookTitle": manifest.get("name", ""),
                                                                   "lastOpenedDate": QDate.currentDate().toString(
                                                                       Qt.ISODate)})
            else:
                self.recentFilesOrDirectoriesInSettings.remove(dict_One)
                dict_One["lastOpenedDate"] = QDate.currentDate().toString(Qt.ISODate)
                dict_One["coverFile"] = coverFile.get('url', "")
                dict_One["bookTitle"] = manifest.get("name", "")
                self.recentFilesOrDirectoriesInSettings.insert(0, dict_One)

        else:
            dict_One = next((one for one in self.recentFilesOrDirectoriesInSettings if one["bookPath"] == bookPath),
                            None)
            logging.debug(dict_One)
            if dict_One is None:
                dict_Str = json.dumps({"bookPath": bookPath,
                                       "coverFile": coverFile.get("url", ""),
                                       "bookTitle": manifest.get("name", ""),
                                       "lastOpenedDate": QDate.currentDate().toString(Qt.ISODate)}, ensure_ascii=False)
                self.recentFilesOrDirectoriesInSettings.insert(0, {"bookPath": bookPath,
                                                                   "coverFile": coverFile.get("url", ""),
                                                                   "bookTitle": manifest.get("name", ""),
                                                                   "lastOpenedDate": QDate.currentDate().toString(
                                                                       Qt.ISODate)})
            else:
                self.recentFilesOrDirectoriesInSettings.remove(dict_One)
                dict_One["lastOpenedDate"] = QDate.currentDate().toString(Qt.ISODate)
                dict_One["coverFile"] = coverFile.get("url", "")
                dict_One["bookTitle"] = manifest.get("name", "")
                self.recentFilesOrDirectoriesInSettings.insert(0, dict_One)

        logging.debug(self.recentFilesOrDirectoriesInSettings)
        self.settings.setValue('RecentlyOpenedFilesOrDirectories',
                               '[' + ';'.join([json.dumps(o) for o in self.recentFilesOrDirectoriesInSettings]) + ']')

    def _open(self):
        self.updateSettings()
        self.signal_open.emit()

    def _close(self):
        self.book.on_action_Save_Audiobook_triggered()
        self.updateSettings()
        self.signal_close.emit()

    def _validate(self):
        logging.debug("_validate")
        try:
            self._save(True)
        except Exception as ex:
            logging.debug('omit validation process')
            return

        manifestForTest = self.book.ManifestDict
        logging.debug(manifestForTest)

        self.mask = MaskWidget(self)
        self.mask.show()

        with open(os.path.join(os.path.dirname(__file__), 'audiobooks.schema.json')) as f:
            schemaData = f.read()
        schema = json.loads(schemaData)

        self.validator = Validator(self._translate('MainWindow', 'Please wait...\n'),
                                   self._translate('MainWindow', 'Validation begins:'),
                                   schema,
                                   manifestForTest)

        self.validator.move(
            self.geometry().x() +
            self.geometry().width() / 2 -
            self.validator.geometry().width() / 2,
            self.geometry().y() +
            self.geometry().height() / 2 -
            self.validator.geometry().height() / 2)

        result = self.validator.exec_()

        self.mask.close()

    def changeUILanguage(self, lang, action):
        logging.debug('changeUILanguage')
        translator = QTranslator()
        app = QApplication.instance()
        app.removeTranslator(app.ui_Translator)

        for act in self.ui.menu_Language.actions():
            if act == action:
                action.setChecked(True)
            else:
                act.setChecked(False)

        # EN, TC
        translator.load(os.path.dirname(__file__) + '/Language/appLang_' + lang + '.qm')
        app.ui_Language = lang
        app.installTranslator(translator)
        app.ui_Translator = translator

        self.ui.retranslateUi(self)

        settings = QSettings(app.organizationName(),
                             app.applicationName())

        settings.setValue('Language', lang)

    def mousePressEvent(self, event):
        logging.debug('mousePressEvent')
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if hasattr(self, "oldPos"):
            logging.debug('mouseMoveEvent with oldPos')
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
            screenCount = QApplication.instance().desktop().screenCount()
            for screenNo in range(screenCount):
                if QApplication.instance().screens()[screenNo] == self.screen():
                    logging.debug('mouseMoveEvent on screen {}'.format(screenNo))
                    break
            # logging.debug('mouseMoveEvent on screen {}'.format(self.screen()))

    def resizeEvent(self, event):
        width, height = event.size().width(), event.size().height()

        # logging.debug('resizeEvent with {}'.format(event.size()))
        # screenNo = QApplication.instance().screenAt(self.pos())
        screenCount = QApplication.instance().desktop().screenCount()
        for screenNo in range(screenCount):
            if QApplication.instance().screens()[screenNo] == self.screen():
                logging.debug(
                    'resizeEvent {} on screen {} with {}'.format(event.size(), screenNo, self.screen().size()))
                sWidth, sHeight = self.screen().size().width(), self.screen().size().height()
                break
        minWidth, minHeight = self.minimumWidth(), self.minimumHeight()
        if minWidth <= sWidth and minHeight <= sHeight:
            event.accept()
        else:
            event.accept()
            self.showMaximized()

