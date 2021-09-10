# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 04:34:20 2021
"""


import logging
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_alert import Ui_Alert
from ui_alertwithbuttons import Ui_AlertWithButtons


class Alert(QDialog):
    
    close_alert = Signal()

    def __init__(self, message, title=""):
        super(Alert, self).__init__()

        logging.debug(message)

        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui = Ui_Alert()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate

        if title:
            self.ui.label.setText(title)
        self.ui.label_Msg.setText(message)
        self.ui.pushButton_Ok.clicked.connect(self.accept)
        self.ui.toolButton_Close.clicked.connect(self.reject)


class AlertWithButtons(QDialog):
    close_alert = Signal()

    def __init__(self, message, title=""):
        super(AlertWithButtons, self).__init__()

        logging.debug(message)

        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui = Ui_AlertWithButtons()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate

        if title:
            self.ui.label.setText(title)
        self.ui.label_Msg.setText(message)
        self.ui.pushButton_Ok.clicked.connect(self.accept)
        self.ui.pushButton_Cancel.clicked.connect(self.reject)
        self.ui.toolButton_Close.clicked.connect(self.reject)
