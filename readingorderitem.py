# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 22:48:05 2021
"""


import logging
import mimetypes
from multipledispatch import dispatch

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import *

from book import Audiobook, Helper
from ui_readingorderitem import Ui_ReadingOrderItem
# import resources_rc


class ReadingOrderItem(QWidget):

    @dispatch(QListWidgetItem, int)
    def __init__(self, item, serialNo=-1):
        super(ReadingOrderItem, self).__init__()
        
        self.ui = Ui_ReadingOrderItem()
        self.ui.setupUi(self)
        self.player = QMediaPlayer()
        self._fullFilename = '*.mp3'
        
        self._translate = QCoreApplication.translate
        self._listItem = item
        self._serialNo = serialNo
        self._seconds = 0.0
                
    @dispatch(str, QListWidgetItem, int)
    def __init__(self, fullFilename, item, serialNo=-1):
        logging.debug('@dispatch(str, QListWidgetItem, int)')
        super(ReadingOrderItem, self).__init__()
        
        self.ui = Ui_ReadingOrderItem()
        self.ui.setupUi(self)
        self.player = QMediaPlayer()
        self._fullFilename = fullFilename

        self._translate = QCoreApplication.translate

        mime, encoding = mimetypes.guess_type(fullFilename)
        extension = mimetypes.guess_extension(fullFilename)

        logging.debug(fullFilename)    
        
        book = Audiobook.getInstance()

        if fullFilename.startswith('http'):
            logging.debug(fullFilename)
            self.ui.label_Href.setText(fullFilename)

            self.ui.label_Href.setToolTip("<p style=\"color:#FFFFFF\">" +
                                          fullFilename +
                                          "</p>")

            duration = Helper.getMP3Duration(fullFilename)
            self.ui.label_Duration.setText(
                "{:02d}".format(int(duration // 3600)) +
                ":{:02d}".format(int(duration // 60)) +
                ":{:02d}".format(int(duration % 60)))
            self.ui.progressBar.setMaximum(int(duration))
            self.ui.progressBar.setValue(0)
            self._seconds = duration
        else:
            logging.debug(fullFilename.replace(book.getBookDir() + '/', ""))
            self.ui.label_Href.setText(fullFilename.replace(book.getBookDir() + '/', ""))

            self.ui.label_Href.setToolTip("<p style=\"color:#FFFFFF\">" +
                                          fullFilename +
                                          "</p>")

            duration = Helper.getMP3Duration(fullFilename)
            self.ui.label_Duration.setText("{:02d}".format(int(duration // 3600)) +
                                           ":{:02d}".format(int(duration // 60)) +
                                           ":{:02d}".format(int(duration % 60)))
            self.ui.progressBar.setMaximum(int(duration))
            self.ui.progressBar.setValue(0)
            self._seconds = duration

        self._listItem = item
        self._serialNo = serialNo

        self.ui.pushButton_Remove.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;" 
                                             "font-weight: 400;font-size: 14px;line-height: 20px;\">" +
                                             self._translate("ReadingOrderItem", "Remove this item") +
                                             "</p>")

        self.ui.pushButton_Add.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;" 
                                          "font-weight: 400;font-size: 14px;line-height: 20px;\">" +
                                          self._translate("ReadingOrderItem", "Add this item to TOC") +
                                          "</p>")

        self.ui.pushButton_Play.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;" 
                                             "font-weight: 400;font-size: 14px;line-height: 20px;\">" +
                                           self._translate("ReadingOrderItem", "Play voice!") +
                                           "</p>")
    
    def getDuration(self):
        return self._seconds
    
    def serialNo(self):
        return self._serialNo
    
    def getFullFilename(self):
        return self._fullFilename

    def getLabelIndex(self):
        return self.ui.label_Index.text()
    
    @Slot()
    def on_pushButton_Add_clicked(self):
        logging.debug("on_pushButton_Add_clicked")
        self._listItem.listWidget().parent().add_Resource_to_TOC(self._fullFilename, self.ui.lineEdit.text())
        
    @Slot()
    def on_pushButton_Remove_clicked(self):
        logging.debug("on_pushButton_Remove_clicked")
        self.player.stop()
        self._listItem.listWidget().parent().removeItem(self._listItem)
        QFile.remove(self.getFullFilename())
    
    def getPosition(self, p):
        self.ui.progressBar.setValue(int(p/1000))
    
    @Slot()
    def on_pushButton_Play_clicked(self):
        logging.debug("on_pushButton_Play_clicked")
        self.player.setVolume(60)
        if self.ui.label_Href.text() != "*.mp3" and self.player.state() != QMediaPlayer.PlayingState:
            logging.debug("playing")
            logging.debug(self.ui.label_Href.text())
            content = QMediaContent(QUrl.fromLocalFile(self._fullFilename))
            logging.debug(content)
            self.player.setMedia(content)
            self.player.positionChanged.connect(self.getPosition)
            self.player.play()
            self.ui.pushButton_Play.setIcon(QIcon(QPixmap(":/SVG/svg/icon/reading-order-stop.svg")))
            
        elif self.player.state() == QMediaPlayer.PlayingState:
            logging.debug("stop")
            self.player.stop()
            self.ui.pushButton_Play.setIcon(QIcon(QPixmap(":/SVG/svg/icon/reading-order-play.svg")))

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
                                                 self._translate("ReadingOrderItem", "Remove this item") +
                                                 "</p>")

            self.ui.pushButton_Add.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
                                              "font-weight: 400;font-size: 14px;line-height: 20px;\">" +
                                              self._translate("ReadingOrderItem", "Add this item to TOC") +
                                              "</p>")

            self.ui.pushButton_Play.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
                                               "font-weight: 400;font-size: 14px;line-height: 20px;\">" +
                                               self._translate("ReadingOrderItem", "Play voice!") +
                                               "</p>")

            self.ui.label_Href.setText(self._fullFilename.replace(book.getBookDir() + '/', ""))

        super().changeEvent(event)

    def getItem(self):
        return self._listItem

    def mousePressEvent(self, event):
        logging.debug('mousePressEvent')
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        logging.debug('mouseMoveEvent')
        mimeData = QMimeData()
        mimeData.setText(self.ui.lineEdit.text())
        mimeData.setUrls([QUrl(self.getFullFilename())])

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        # drag.setHotSpot(event.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.CopyAction | Qt.MoveAction)
