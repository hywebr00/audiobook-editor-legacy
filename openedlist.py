# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:03:48 2021
"""


import logging
from multipledispatch import dispatch
import os
import tempfile
# from tempfile import NamedTemporaryFile
from zipfile import ZipFile

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_openedlistitem import Ui_OpenedListItem
from ui_openedlist import Ui_OpenedList
# import resources_rc


class OpenedListItem(QWidget):
    
    # switch_window = pyqtSignal()
    # signal_resize_item = pyqtSignal(int, int, int)
    
    @dispatch(QListWidgetItem, int, str, str, str, str)
    def __init__(self, item, serialNo, bookPath, coverFile, bookTitle, lastOpenedDate):
        super(OpenedListItem, self).__init__()

        self.ui = Ui_OpenedListItem()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate     
        self._serialNo = serialNo
        self._listItem = item
        
        self.lastOpenedDate = lastOpenedDate
        self.bookPath = bookPath
        self.coverFile = coverFile 
        self.bookTitle = bookTitle

        self.ui.label_Ago.setText(lastOpenedDate)
        
        if bookPath.endswith('.lpf'):
            with ZipFile(bookPath, 'r') as zipObj:
                # Get a list of all archived file names from the zip
                listOfFileNames = zipObj.namelist()
                # Iterate over the file names
                for fileName in listOfFileNames:
                    # Check filename endswith csv
                    if fileName == coverFile:
                        # Extract a single file from zip
                        with tempfile.TemporaryDirectory() as tmpdirname:
                            zipObj.extract(fileName, tmpdirname)

                            pixmap = QPixmap(os.path.join(tmpdirname, coverFile).replace('\\', '/'))
                            pixmap = pixmap.scaled(self.ui.label_Cover.size(), Qt.KeepAspectRatio)
                            self.ui.label_Cover.setPixmap(pixmap)
                            break
            # self.ui.label_Cover.setPixmap(QPixmap(":/SVG/svg/icon/welcome-recent-cover.png"))
        elif coverFile != "":
            pixmap = QPixmap(bookPath + '/' + coverFile)
            pixmap = pixmap.scaled(self.ui.label_Cover.size(), Qt.KeepAspectRatio)
            self.ui.label_Cover.setPixmap(pixmap)
        else:
            self.ui.label_Cover.setPixmap(QPixmap(":/SVG/svg/icon/welcome-recent-folder.png"))
            
        self.ui.label_Path.setText(bookPath)
        self.ui.label_Title.setText(bookTitle)             

    @dispatch(QListWidgetItem, int)
    def __init__(self, item, serialNo=-1):
        super(OpenedListItem, self).__init__()

        self.ui = Ui_OpenedListItem()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate     
        self._serialNo = serialNo
        self._listItem = item
        
        self.lastOpenedDate = QDate.currentDate().toString(Qt.ISODate)
        self.bookPath = ""
        self.coverFile = ""
        self.bookTitle = ""
        
        self.ui.label_Ago.setText("Today")
        self.ui.label_Cover.setPixmap(QPixmap(":/SVG/svg/icon/welcome-recent-folder.png"))
        self.ui.label_Path.setText("Path...")
        self.ui.label_Title.setText("Title")        

    def _serialNo(self):
        return self._serialNo
    serialNo = property(_serialNo)

    def getBookPath(self):
        return self.bookPath

    def getBookTitle(self):
        return self.bookTitle    
    
    def getCoverFile(self):
        return self.coverFile      

    def getLastOpenedDate(self):
        return self.lastOpenedDate       


class OpenedList(QWidget):
    
    signal_close = Signal()
    
    def __init__(self, defaultList={}, width=320, height=52):
        super(OpenedList, self).__init__()
        self.ui = Ui_OpenedList()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate 
        
        self._listWidgetItemSerialNo = 0  # Unique index
        self._hasList = False   
        self._itemWidth = width 
        self._itemHeight = height
        
        self.ui.toolButton_Close.clicked.connect(lambda: self.signal_close.emit())
        
    def getItemSize(self):
        return QSize(self._itemWidth, self._itemHeight)
    
    def getSerialNo(self):
        return self._listWidgetItemSerialNo

    def addItem(self, bookPath, coverFile, bookTitle, lastOpenedDate):
        logging.debug("addItem with bookPath = " + bookPath + ", coverFile = " + coverFile + ", bookTitle = " + bookTitle + ", lastOpenedDate = " + lastOpenedDate)
        if not self._hasList:
            self._hasList = True

        item = QListWidgetItem()  
        # item.setText(str(self.ui.listWidget.count()))
        item.setSizeHint(self.getItemSize()) 
        
        roi = OpenedListItem(item, self.getSerialNo(), bookPath, coverFile, bookTitle, lastOpenedDate)
        # roi.signal_resize_item.connect(self.on_signal_resize_item)
          
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.setItemWidget(item, roi)
        self._listWidgetItemSerialNo += 1   

    def addItems(self, number=1):
        logging.debug("addItems")
        if not self._hasList:
            self._hasList = True

        for i in range(number):
            logging.debug("item %d".format(i))
            item = QListWidgetItem()  
            # item.setText(str(self.ui.listWidget.count()))
            item.setSizeHint(self.getItemSize()) 
            
            roi = OpenedListItem(item, self.getSerialNo())
            # roi.signal_resize_item.connect(self.on_signal_resize_item)
              
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, roi)
            self._listWidgetItemSerialNo += 1   
