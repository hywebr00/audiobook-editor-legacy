# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:39:07 2021
"""


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_pyqt5license import Ui_Dialog_PyQt5License
from translucent import MaskWidget


class Dialog_PyQt5License(QDialog):

    def __init__(self, mainWindow):
        super(Dialog_PyQt5License, self).__init__()

        self.mainWindow = mainWindow
        self.ui = Ui_Dialog_PyQt5License()

        self.ui.setupUi(self)

        self.mask = MaskWidget(self.mainWindow)
        self.mask.show()

        self.move(
            self.mainWindow.geometry().x() +
            self.mainWindow.geometry().width() / 2 -
            self.geometry().width() / 2,
            self.mainWindow.geometry().y() +
            self.mainWindow.geometry().height() / 2 -
            self.geometry().height() / 2)

        self._translate = QCoreApplication.translate

    @Slot()
    def accept(self):
        self.close()
        self.mask.close()

    @Slot()
    def closeEvent(self, closeEvent):
        self.close()
        self.mask.close()

    @Slot()
    def reject(self):
        self.close()
        self.mask.close()

