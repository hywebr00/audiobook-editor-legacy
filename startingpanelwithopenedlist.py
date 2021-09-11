# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:40:51 2021
"""

import json
import logging
from multipledispatch import dispatch

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_startingpanelwithopenedlist import Ui_StartingPanelWithOpenedList
from openedlist import OpenedList
# import resources_rc


class StartingPanelWithOpenedList(QMainWindow):
    
    signal_switch_window = Signal([bool], [str])
    # signal_switch_window = pyqtSignal(str)
    
    MaxRecentFiles = 9

    def __init__(self):
        super(StartingPanelWithOpenedList, self).__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.ui = Ui_StartingPanelWithOpenedList()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate

        self.openedList = OpenedList(self)
        # self.openedList.show()
        self.ui.verticalLayout_Right.addWidget(self.openedList, 1)

        self.settings = QSettings()
        self.recentFilesOrDirectoriesInSettings = self.settings.value('RecentlyOpenedFilesOrDirectories', '', type=str)
        logging.debug(self.recentFilesOrDirectoriesInSettings)
        self.recentFilesOrDirectoriesInSettings = self.recentFilesOrDirectoriesInSettings[:-1]
        self.recentFilesOrDirectoriesInSettings = self.recentFilesOrDirectoriesInSettings[1:]
        if len(self.recentFilesOrDirectoriesInSettings) > 0:
            self.recentFilesOrDirectoriesInSettings = [json.loads(obj) for obj in self.recentFilesOrDirectoriesInSettings.split(';')]
        else:
            self.recentFilesOrDirectoriesInSettings = []
        # self.recentFilesOrDirectoriesInSettings = [json.loads(obj) for obj in self.recentFilesOrDirectoriesInSettings.split(';')]

        for one in self.recentFilesOrDirectoriesInSettings:
            self.openedList.addItem(one["bookPath"], one["coverFile"], one["bookTitle"], one["lastOpenedDate"])

        self.openedList.signal_close.connect(lambda: self.close())
        self.openedList.ui.listWidget.itemDoubleClicked.connect(self.itemDoubleClicked)

        self.ui.pushButton_New.clicked.connect(self.new)
        self.ui.pushButton_Open_File.clicked.connect(self.open_File)
        self.ui.pushButton_Open_Project.clicked.connect(self.open_Project)

        self.ui.label_4.installEventFilter(self)
        self.ui.label_5.installEventFilter(self)
        self.ui.label_6.installEventFilter(self)

    def eventFilter(self, watched, event):
        if watched == self.ui.label_4:
            if event.type() == QEvent.MouseButtonPress:
                # mouseEvent = QMouseEvent(event)
                if event.buttons() == Qt.LeftButton:
                    logging.debug("Label_4 is clicked!")
                    self.ui.pushButton_New.clicked.emit()
                    return True
        elif watched == self.ui.label_5:
            if event.type() == QEvent.MouseButtonPress:
                # mouseEvent = QMouseEvent(event)
                if event.buttons() == Qt.LeftButton:
                    logging.debug("Label_5 is clicked!")
                    self.ui.pushButton_Open_File.clicked.emit()
                    return True
        elif watched == self.ui.label_6:
            if event.type() == QEvent.MouseButtonPress:
                # mouseEvent = QMouseEvent(event)
                if event.buttons() == Qt.LeftButton:
                    logging.debug("Label_6 is clicked!")
                    self.ui.pushButton_Open_Project.clicked.emit()
                    return True

        return super().eventFilter(watched, event)

    def closeEvent(self, event):
        logging.debug('window close')

    def new(self):
        logging.debug("new is clicked")
        self.signal_switch_window[bool].emit(True)

    def open_File(self):
        logging.debug("open_File is clicked")
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         self._translate("StartingPanel", "Select a book"),
                                                         "./",
                                                         self._translate("StartingPanel", "Audiobooks(*.lpf)"))
        if len(filename) > 0: 
            logging.debug(filename)
        else:
            return
        self.signal_switch_window[str].emit(filename)

    def open_Project(self):
        openDirectory = QFileDialog.getExistingDirectory(self, self._translate("StartingPanel", "Select one directory"),
                                                         self._translate("StartingPanel", "./"))
        logging.debug(openDirectory)
        self.signal_switch_window[str].emit(openDirectory)        

    def doubleClicked(self, qModelIndex):
        logging.debug(self.recentFilesOrDirectoriesInSettings[qModelIndex.row()])
        # item = self.recentFilesOrDirectoriesInSettings[qModelIndex.row()]

    def itemDoubleClicked(self, item):
        logging.debug('itemDoubleClicked = ' + self.openedList.ui.listWidget.itemWidget(item).getBookTitle())
        dict_Selected = {"bookPath": self.openedList.ui.listWidget.itemWidget(item).getBookPath(),
                         "coverFile": self.openedList.ui.listWidget.itemWidget(item).getCoverFile(),
                         "bookTitle": self.openedList.ui.listWidget.itemWidget(item).getBookTitle(),
                         "lastOpenedDate": self.openedList.ui.listWidget.itemWidget(item).getLastOpenedDate()}
        logging.debug(dict_Selected)
        # self.updateSettings(False, dict_Selected)
        self.signal_switch_window[str].emit(dict_Selected["bookPath"])

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if hasattr(self, "oldPos"):
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def resizeEvent(self, event):
        width, height = event.size().width(), event.size().height()
        if width != self.minimumWidth() or height != self.minimumHeight():
            event.accept()
            self.resize(self.minimumWidth(), self.minimumHeight())

