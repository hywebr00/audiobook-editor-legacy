# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:18:38 2021
"""


# import logging
# import os
# import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
# from multipledispatch import dispatch
# from book import Audiobook

from ui_supplementallistwidget import Ui_SupplementalListWidget

class SupplementalListWidget(QWidget):
    
    # switch_window = pyqtSignal()
    # signal_resize_item = pyqtSignal(int, int, int)
    
    def __init__(self):
        super(SupplementalListWidget, self).__init__()

        self.ui = Ui_SupplementalListWidget()
        self.ui.setupUi(self)
        self.ui.listWidget.setVisible(False)
        self._isEmpty = True
        self._translate = QCoreApplication.translate    
    
    @Slot()
    def on_pushButton_Add_clicked(self):
        print('on_pushButton_Add_clicked')
        if self._isEmpty:
            self.ui.label_NoItem.setVisible(False)
            self.ui.listWidget.setVisible(True)
            self._isEmpty = False

        


