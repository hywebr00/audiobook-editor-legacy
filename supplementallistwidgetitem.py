# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 09:21:12 2021
"""


import logging
import mimetypes
from multipledispatch import dispatch

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from book import Audiobook
from ui_supplementallistwidgetitem import Ui_SupplementalListWidgetItem
# import resources_rc


class SupplementalListWidgetItem(QWidget):
    
    add_Resource_to_TOC = Signal(str)
    
    @dispatch(QListWidgetItem, int)
    def __init__(self, item, serialNo=-1):
        logging.debug('@dispatch(QListWidgetItem, int)')
        super(SupplementalListWidgetItem, self).__init__()
        self.ui = Ui_SupplementalListWidgetItem()
        self.ui.setupUi(self)
        
        self._serialNo = serialNo
        self._listItem = item        
        self._translate = QCoreApplication.translate     

    @dispatch(str, QListWidgetItem, int)
    def __init__(self, fullFilename, item, serialNo=-1):
        logging.debug('@dispatch(str, QListWidgetItem, int)')
        super(SupplementalListWidgetItem, self).__init__()
        self.ui = Ui_SupplementalListWidgetItem()
        self.ui.setupUi(self)
        self._fullFilename = fullFilename
        
        mime, encoding = mimetypes.guess_type(fullFilename)

        # kind = filetype.guess(fullFilename)
            
        if mime is None:
            logging.warning('Cannot guess file type!')
            
        else:
            extension = mimetypes.guess_extension(mime)
            logging.debug('File extension: %s' % extension)
            logging.debug('File MIME type: %s' % mime)
            if mime.startswith('image'):
                self.ui.label_Filetype.setPixmap(QPixmap(":/SVG/svg/icon/resource-image.svg"))
            elif mime.startswith('audio'):
                self.ui.label_Filetype.setPixmap(QPixmap(":/SVG/svg/icon/resource-audio.svg"))
            elif mime == 'application/pdf':
                self.ui.label_Filetype.setPixmap(QPixmap(":/SVG/svg/icon/resource-pdf.svg"))
 
        logging.debug(fullFilename)  
        
        '''
        filename, file_extension = os.path.splitext(item_Open)
        if file_extension == '.lpf':   
        '''    
        book = Audiobook.getInstance()
        logging.debug((fullFilename.replace(book.getBookDir() + '/', ""), fullFilename)
                      [fullFilename.startswith('http')])
        shortFilename = (fullFilename.replace(book.getBookDir() + '/', ""),
                         fullFilename)[fullFilename.startswith('http')]
        displayFilename = shortFilename
        if mime is not None:
            if len(shortFilename) >= 8:
                displayFilename = shortFilename[0:5] + ".." + extension
        else:
            if len(shortFilename) >= 8:
                # src = QFile(fullFilename)
                info = QFileInfo(fullFilename)
                displayFilename = shortFilename[0:5] + ".." + info.suffix()

        logging.debug("displayFilename = " + displayFilename)    
        self.ui.lineEdit.setText(displayFilename)
        # self.ui.lineEdit.setText(fullFilename.replace(book.getBookDir() + '/', ""))
        
        self._serialNo = serialNo
        self._listItem = item        
        self._translate = QCoreApplication.translate

        self.ui.lineEdit.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;" 
                                    "font-weight: 400;font-size: 14px;line-height: 20px;\">" +
                                    fullFilename +
                                    "</p>")
        self.ui.pushButton_Remove.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;" 
                                             "font-weight: 400;font-size: 14px;line-height: 20px;\">" +
                                             self._translate("SupplementalListWidgetItem", "Remove this item") +
                                             "</p>")
        self.ui.pushButton_Add.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;" 
                                             "font-weight: 400;font-size: 14px;line-height: 20px;\">" +
                                          self._translate("SupplementalListWidgetItem", "Add this item to TOC") +
                                          "</p>")

    def serialNo(self):
        return self._serialNo
        
    @Slot()
    def on_pushButton_Remove_clicked(self):
        logging.debug("on_pushButton_Remove_clicked")
        self._listItem.listWidget().parent().removeItem(self._listItem)
        QFile.remove(self.getFullFilename())

    @Slot()
    def on_pushButton_Add_clicked(self):
        logging.debug("ListWidgetItem : on_pushButton_Add_clicked")
        self._listItem.listWidget().parent().add_Resource_to_TOC(self._fullFilename, "")
        
    def getFullFilename(self):
        return self._fullFilename

    def changeEvent(self, event):
        """Handle LanguageChange event"""
        if event.type() == QEvent.LanguageChange:
            logging.debug("Language changed")
            self.ui.retranslateUi(self)
            self.ui.pushButton_Remove.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
                                                 "font-weight: 400;font-size: 14px;line-height: 20px;\">" +
                                                 self._translate("SupplementalListWidgetItem", "Remove this item") +
                                                 "</p>")
            self.ui.pushButton_Add.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
                                              "font-weight: 400;font-size: 14px;line-height: 20px;\">" +
                                              self._translate("SupplementalListWidgetItem", "Add this item to TOC") +
                                              "</p>")
        super().changeEvent(event)

    def mousePressEvent(self, event):
        logging.debug('mousePressEvent')
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        logging.debug('mouseMoveEvent')
        mimeData = QMimeData()
        # mimeData.setText(self.getFullFilename())
        mimeData.setUrls([QUrl(self.getFullFilename())])

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        # drag.setHotSpot(event.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.CopyAction | Qt.MoveAction)

