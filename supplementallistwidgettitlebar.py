# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 02:49:33 2021
"""


import logging
# import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_supplementallistwidgettitlebar import Ui_SupplementalListWidgetTitleBar


class SupplementalListWidgetTitleBar(QWidget):
    
    signal_add_resource = Signal(bool, str)
    signal_pushButton_Add_clicked = Signal()
    
    def __init__(self):
        super(SupplementalListWidgetTitleBar, self).__init__()
        
        # REMOVE TITLE BAR
        # self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.ui = Ui_SupplementalListWidgetTitleBar()
        self.ui.setupUi(self)
        
    @Slot()
    def on_pushButton_Add_clicked(self):
        logging.debug('SupplementalListWidgetTitleBar : on_pushButton_Add_clicked')
        self.signal_pushButton_Add_clicked.emit()
        '''
        if self._isEmpty:
            self.ui.label_NoItem.setVisible(False)
            self.ui.listWidget.setEnabled(True)
            self._isEmpty = False
        
        book = Audiobook.getInstance()
        # fname, _ = QFileDialog.getOpenFileName(self, 'Open file', book.getBookDir() + '/', "Any file(*.*)")
        # print(fname, _)
        
        is_inBookDir = False
        fname = ''
        
        afw = AttachFromWidget(False, 'Open file', book.getBookDir() + '/', "Any file(*.*)")
        afw.signal_add_resource.connect(self.getAttachFromWidgetResult)
        afw.show() 

        '''         
        '''
        while (not is_inBookDir):
            
            fname, _ = QFileDialog.getOpenFileName(self, 'Open file', book.getBookDir() + '/', "Any file(*.*)")
        
            print(fname)
            if fname.startswith(book.getBookDir()):
                is_inBookDir = True
            else:
                QMessageBox.information(self, 'Tip', 'This file is not in your book directory, we\'d copy for you!')
                src = QFile(fname)
                info = QFileInfo(fname)
                if (not src.copy(book.getBookDir() + '/' + info.fileName())):
                    QMessageBox.warning(self, 'Warning', 'We couldn\'t copy this file for you!', QMessageBox.Ok, QMessageBox.Ok)
                    fname = ""
                else:
                    fname = book.getBookDir() + '/' + info.fileName()
                    is_inBookDir = True                    
        
        
        
        
        kind = filetype.guess(fname)
            
        if kind is None:
            print('Cannot guess file type!')
        else:    
            print('File extension: %s' % kind.extension)
            print('File MIME type: %s' % kind.mime)               
                            
        self.addItems(fname)
        '''    
