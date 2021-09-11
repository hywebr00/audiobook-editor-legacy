# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:47:21 2021
"""


import logging
import sys
import urllib.request
from multipledispatch import dispatch

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from book import Audiobook, Helper

from ui_attachfromwidget import Ui_AttachFromWidget


class AttachFromWidget(QMainWindow):
    
    signal_add_resource = Signal(bool, str)
    signal_close = Signal()

    @dispatch(bool, str, str, str)
    def __init__(self, bool_acceptURL=True,
                 str_Caption="Select one file",
                 str_DefaultDir="./",
                 str_Filters=""):
        super(AttachFromWidget, self).__init__()
        
        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.ui = Ui_AttachFromWidget()
        self.ui.setupUi(self)
        self.ui.label_ErrorMessage.setVisible(False)
        self.ui.pushButton_Create.setVisible(False)
        self._translate = QCoreApplication.translate  
        
        self.ui.pushButton_Add.clicked.connect(self.on_pushButton_Add_Clicked)
        self.ui.pushButton_BrowseLocalFile.clicked.connect(self.on_pushButton_BrowseLocalFile_Clicked)
        self.ui.pushButton_Create.clicked.connect(self.on_pushButton_Create_Clicked)

        self.acceptURL = bool_acceptURL
        self.is_URL_existent = False
        self.is_Local_File_Ready = False
        self.URL = ""
        self.localFile = ""
        
        self.caption = str_Caption
        self.defaultDir = str_DefaultDir
        self.filters = str_Filters    

        if not self.acceptURL:
            self.ui.lineEdit_URL.setVisible(False)
            self.ui.label_Or.setVisible(False)
            self.ui.pushButton_Add.setVisible(False)
    
    @dispatch(str, str, str)
    def __init__(self, str_Caption="Select one file",
                 str_DefaultDir="./",
                 str_Filters=""):
        super(AttachFromWidget, self).__init__()
        
        # REMOVE TITLE BAR
        # self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.ui = Ui_AttachFromWidget()
        self.ui.setupUi(self)
        self.ui.label_ErrorMessage.setVisible(False)
        self.ui.pushButton_Create.setVisible(False)
        self._translate = QCoreApplication.translate  
        
        self.ui.pushButton_Add.clicked.connect(self.on_pushButton_Add_Clicked)
        self.ui.pushButton_BrowseLocalFile.clicked.connect(self.on_pushButton_BrowseLocalFile_Clicked)
        self.ui.pushButton_Create.clicked.connect(self.on_pushButton_Create_Clicked)

        self.is_URL_existent = False
        self.is_Local_File_Ready = False
        self.URL = ""
        self.localFile = ""
        
        self.caption = str_Caption
        self.defaultDir = str_DefaultDir
        self.filters = str_Filters
    
    '''
    def show(self):
        print('show')
        super(AttachFromWidget, self).show()
    '''
    
    def on_pushButton_Add_Clicked(self):
        logging.debug('on_pushButton_Add_Clicked')
        text = self.ui.lineEdit_URL.text()
        result = Helper.checkURLAvailability(text)
        if result:
            logging.debug(True)
            self.is_URL_existent = True   
            self.URL = text
            if self.is_URL_existent or self.is_Local_File_Ready:
                self.ui.pushButton_Create.setVisible(True)
            # self.ui.label_ErrorMessage.setText('This URL is valid!')
        else:
            logging.debug(False)

    def on_pushButton_BrowseLocalFile_Clicked(self):
        logging.debug('on_pushButton_BrowseLocalFile_Clicked')
        
        filename, filetype = QFileDialog.getOpenFileName(self, self._translate("AttachFromWidget", self.caption), self.defaultDir, self._translate("AttachFromWidget", self.filters))
        if len(filename) > 0: 
            logging.debug(filename)
            self.is_Local_File_Ready = True
            self.localFile = filename
            self.ui.pushButton_BrowseLocalFile.setVisible(False)
            self.ui.lineEdit_BrowseLocalFile.setGeometry(10, 
                                                         self.ui.lineEdit_BrowseLocalFile.geometry().y(),
                                                         288 - 10 - 10,
                                                         self.ui.lineEdit_BrowseLocalFile.geometry().height())
            self.ui.lineEdit_BrowseLocalFile.setText(filename)
            if self.is_URL_existent or self.is_Local_File_Ready:
                self.ui.pushButton_Create.setVisible(True)            
        else:
            return        
        
    def on_pushButton_Create_Clicked(self):
        logging.debug('on_pushButton_Create_Clicked')    
        if self.is_URL_existent or self.is_Local_File_Ready:
            if self.is_Local_File_Ready:
                self.signal_add_resource.emit(False, self.localFile)
            
            else:
                self.signal_add_resource.emit(True, self.URL)
        self.close()        
        # self.signal_close.emit()
    
    def closeEvent(self, event):
        logging.debug('window close')  
        self.signal_close.emit()
        event.accept()

