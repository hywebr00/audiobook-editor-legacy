# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:09:05 2021
"""

import logging
# import sys
# import urllib.request
from multipledispatch import dispatch

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from book import Audiobook, Helper
from ui_attachfromwidgetwithouturl import Ui_AttachFromWidgetWithoutURL


class AttachFromWidgetWithoutURL(QDialog):
    signal_add_resource = Signal(bool, str)
    signal_close = Signal()

    MARGIN_BROWSE_LOCAL_FILE = 10

    @dispatch(bool, str, str, str)
    def __init__(self,
                 bool_acceptURL=False,
                 str_Caption="Select files",
                 str_DefaultDir="./",
                 str_Filters=""):
        super().__init__()

        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.ui = Ui_AttachFromWidgetWithoutURL()
        self.ui.setupUi(self)
        # self.ui.pushButton_Create.setVisible(False)
        self._translate = QCoreApplication.translate

        self.ui.pushButton_BrowseLocalFile.clicked.connect(self.on_pushButton_BrowseLocalFile_Clicked)
        self.ui.pushButton_Create.clicked.connect(self.on_pushButton_Create_Clicked)
        self.ui.toolButton_Close.clicked.connect(self.reject)

        self.ui.lineEdit_BrowseLocalFile.installEventFilter(self)

        self.acceptURL = bool_acceptURL
        self.is_URL_existent = False
        self.is_Local_File_Ready = False
        self.URLs = []
        self.localFiles = []

        self.caption = str_Caption
        self.defaultDir = str_DefaultDir
        self.filters = str_Filters

    @dispatch(str, str, str)
    def __init__(self,
                 str_Caption="Select files",
                 str_DefaultDir="./",
                 str_Filters=""):
        super().__init__()

        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.ui = Ui_AttachFromWidgetWithoutURL()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate

        self.ui.pushButton_BrowseLocalFile.clicked.connect(self.on_pushButton_BrowseLocalFile_Clicked)
        self.ui.pushButton_Create.clicked.connect(self.on_pushButton_Create_Clicked)
        self.ui.toolButton_Close.clicked.connect(self.reject)

        self.is_URL_existent = False
        self.is_Local_File_Ready = False
        self.URLs = []
        self.localFiles = []

        self.caption = str_Caption
        self.defaultDir = str_DefaultDir
        self.filters = str_Filters

    def on_pushButton_BrowseLocalFile_Clicked(self):
        logging.debug('on_pushButton_BrowseLocalFile_Clicked')

        filenames, _ = QFileDialog.getOpenFileNames(self,
                                                    self.caption,
                                                    self.defaultDir,
                                                    self.filters)
        if filenames:

            logging.debug(";;;".join(filenames))
            self.is_Local_File_Ready = True
            self.localFiles = filenames
            self.ui.pushButton_BrowseLocalFile.setVisible(False)
            self.ui.lineEdit_BrowseLocalFile.setGeometry(AttachFromWidgetWithoutURL.MARGIN_BROWSE_LOCAL_FILE,
                                                         self.ui.lineEdit_BrowseLocalFile.geometry().y(),
                                                         self.ui.lineEdit_BrowseLocalFile.maximumSize().width() -
                                                         AttachFromWidgetWithoutURL.MARGIN_BROWSE_LOCAL_FILE * 2,
                                                         self.ui.lineEdit_BrowseLocalFile.geometry().height())

            self.ui.lineEdit_BrowseLocalFile.setText(";".join(filenames))
            if self.is_URL_existent or self.is_Local_File_Ready:
                self.ui.pushButton_Create.setEnabled(True)
        else:
            return

    def getURLs(self):
        return self.localFiles

    def on_pushButton_Create_Clicked(self):
        logging.debug('on_pushButton_Create_Clicked')
        self.accept()
        self.hide()

    def closeEvent(self, event):
        logging.debug('AttachFromWidgetWithoutURL close -> Mask should close, too')
        # self.signal_close.emit()
        event.accept()

    def eventFilter(self, watched, event):
        if watched == self.ui.lineEdit_BrowseLocalFile:
            if event.type() == QEvent.MouseButtonPress:
                # mouseEvent = QMouseEvent(event)
                if event.buttons() == Qt.LeftButton:
                    logging.debug("pushButton_BrowseLocalFile is clicked!")
                    self.ui.pushButton_BrowseLocalFile.clicked.emit()
                    return True

        return super().eventFilter(watched, event)
