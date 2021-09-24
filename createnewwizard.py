# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:58:28 2021
"""


import logging
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_createnewwizard import Ui_CreateNewWizard
from alert import Alert
from translucent import MaskWidget


class CreateNewWizard(QMainWindow):
    
    switch_window = Signal(dict)
    
    def __init__(self):
        super(CreateNewWizard, self).__init__()

        self.ui = Ui_CreateNewWizard()
        self.ui.setupUi(self)

        self.ui.label_3.adjustSize()
        self.ui.label_9.setGeometry(self.ui.label_3.geometry().x() + self.ui.label_3.geometry().width() + 7,
                                     self.ui.label_9.geometry().y(),
                                     self.ui.label_9.geometry().width(),
                                     self.ui.label_9.geometry().height())

        self.ui.label_4.adjustSize()
        self.ui.label_10.setGeometry(self.ui.label_4.geometry().x() + self.ui.label_4.geometry().width() + 7,
                                     self.ui.label_10.geometry().y(),
                                     self.ui.label_10.geometry().width(),
                                     self.ui.label_10.geometry().height())


        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self._translate = QCoreApplication.translate
        
        self.ui.pushButton_Browse.clicked.connect(self._button_Browse_clicked)
        self.ui.pushButton_Create.clicked.connect(self._button_Create_clicked)
        self.ui.pushButton_Cancel.clicked.connect(self._button_Cancel_clicked)

    def _button_Browse_clicked(self):
        saveDirectory = QFileDialog.getExistingDirectory(self,
                                                         self._translate("NewBookWizard", "Select one directory"),
                                                         "./")
        logging.debug(saveDirectory)
        if len(saveDirectory) > 0:
            self.ui.lineEdit_BookPath.setText(saveDirectory)
            self.ui.lineEdit_BookPath.setReadOnly(True)

    def _button_Create_clicked(self):
        saveDir = self.ui.lineEdit_BookPath.text()
        bookTitle = self.ui.lineEdit_BookTitle.text()
        author = self.ui.lineEdit_Author.text()
        publisher = self.ui.lineEdit_Publisher.text()
        readBy = self.ui.lineEdit_ReadBy.text()
        if saveDir and bookTitle:
            logging.debug(saveDir + ":" + bookTitle)
            self.switch_window.emit({"saveDir": saveDir,
                                     "bookTitle": bookTitle,
                                     "author": {"type": "Person", "name": author},
                                     "publisher": publisher,
                                     "readBy": {"type": "Person", "name": readBy}})

        else:
            self.mask = MaskWidget(self)
            self.mask.show()

            self.alert = Alert(self._translate("CreateNewWizard", "You must select one directory and" 
                                                                  " keyin the booktitle!"),
                               self._translate("CreateNewWizard", "Warning!"))

            self.alert.move(
                self.geometry().x() +
                self.geometry().width() / 2 -
                self.alert.geometry().width() / 2,
                self.geometry().y() +
                self.geometry().height() / 2 -
                self.alert.geometry().height() / 2)

            result = self.alert.exec_()
            self.mask.close()

    def _button_Cancel_clicked(self):
        self.switch_window.emit({})
        self.close()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if hasattr(self, "oldPos"):
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()





