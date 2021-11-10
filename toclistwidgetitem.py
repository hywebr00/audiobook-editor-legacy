# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 01:59:13 2021
"""


import logging
import mimetypes
from multipledispatch import dispatch

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_toclistwidgetitem import Ui_TOCListWidgetItem
from book import Audiobook


class TOCListWidgetItem(QWidget):

    @dispatch(str, str)
    def __init__(self, title, href):
        pass
   
    @dispatch(QListWidgetItem, int)
    def __init__(self, item, serialNo=-1):
        super(TOCListWidgetItem, self).__init__()

        self.ui = Ui_TOCListWidgetItem()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate

        self._serialNo = serialNo
        self._listWidgetItem = item
        self._fullFilename = ''
        self._title = ''
        
    @dispatch(str, QListWidgetItem, int, str)
    def __init__(self, fullFilename, item, serialNo, title):
        super(TOCListWidgetItem, self).__init__()

        self.ui = Ui_TOCListWidgetItem()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate

        self._serialNo = serialNo
        self._listWidgetItem = item 
        self._fullFilename = fullFilename
        self._title = title
        
        book = Audiobook.getInstance()   

        mime, encoding = mimetypes.guess_type(fullFilename)
        extension = mimetypes.guess_extension(fullFilename)

        if mime and mime.startswith("audio"):
            self.ui.timeEdit_Start.setEnabled(True)
            self.ui.timeEdit_Start.setVisible(True)
        else:
            self.ui.timeEdit_Start.setEnabled(False)
            self.ui.timeEdit_Start.setVisible(False)

        self.ui.label_Href.setText((fullFilename.replace(book.getBookDir() + '/', ""),
                                    fullFilename)[fullFilename.startswith('http')])

        self.ui.label_Href.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
                                      "font-weight: 400;font-size: 14px;line-height: 20px;\">" +
                                      fullFilename +
                                      "</p>")

        self.ui.pushButton_Remove.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
                                             "font-weight: 400;font-size: 14px;line-height: 20px;\">" +
                                             self._translate("TOCListWidgetItem", "Remove this item") +
                                             "</p>")

        self.ui.lineEdit_Title.setText(title)

    def clone(self):
        clone = TOCListWidgetItem(self.ui.lineEdit_Title.text(), self.ui.label_Href.text())
        return clone   
        
    def serialNo(self):
        return self._serialNo

    def getFullFilename(self):
        return self._fullFilename

    def getTitle(self):
        return self.ui.lineEdit_Title.text()

    def setTitle(self, title):
        self._title = title
        self.ui.lineEdit_Title.setText(title)

    def getTimeStamps(self):
        return self.ui.timeEdit_Start.isEnabled(), self.ui.timeEdit_Start.time()

    @Slot()
    def on_pushButton_Remove_clicked(self):
        logging.debug("on_pushButton_Remove_clicked")
        logging.debug("my serialNo = %d" % self._serialNo)
        lwitem = self._listWidgetItem
        logging.debug(type(lwitem))
        lwitem.listWidget().parent().removeItem(lwitem)

    def changeEvent(self, event):
        """Handle LanguageChange event"""
        if event.type() == QEvent.LanguageChange:
            logging.debug("Language changed")
            book = Audiobook.getInstance()
            if book is None:
                return
            self.ui.retranslateUi(self)
            self.ui.pushButton_Remove.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
                                                 "font-weight: 400;font-size: 14px;line-height: 20px;\">" +
                                                 self._translate("TOCListWidgetItem", "Remove this item") +
                                                 "</p>")

            self.ui.lineEdit_Title.setText(self._title)
            self.ui.label_Href.setText((self._fullFilename.replace(book.getBookDir() + '/', ""),
                                        self._fullFilename)[self._fullFilename.startswith('http')])
        super().changeEvent(event)

    def mousePressEvent(self, event):
        logging.debug('mousePressEvent')
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        logging.debug('mouseMoveEvent')
        mimeData = QMimeData()
        mimeData.setText(self.ui.lineEdit_Title.text())
        mimeData.setUrls([QUrl(self.getFullFilename())])

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        # drag.setHotSpot(event.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.CopyAction | Qt.MoveAction)



