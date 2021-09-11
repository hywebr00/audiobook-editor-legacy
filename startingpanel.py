# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:40:51 2021
"""


import logging
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_startingpanel import Ui_StartingPanel


class StartingPanel(QMainWindow):
    
    signal_switch_window = Signal([bool], [str])
    # signal_switch_window = pyqtSignal(str)
    
    MaxRecentFiles = 10
    # windowList = []

    def __init__(self):
        super(StartingPanel, self).__init__()

        # QMainWindow.__init__(self)
        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.ui = Ui_StartingPanel()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate

        self.ui.pushButton_New.clicked.connect(self.new)
        self.ui.pushButton_Open_File.clicked.connect(self.open_File)
        self.ui.pushButton_Open_Project.clicked.connect(self.open_Project)
        self.ui.toolButton_Close.clicked.connect(self.close)

        self.ui.label_4.installEventFilter(self)
        self.ui.label_5.installEventFilter(self)
        self.ui.label_6.installEventFilter(self)
        
    def new(self):
        logging.debug("new is clicked")
        self.signal_switch_window[bool].emit(True)

    def open_File(self):
        logging.debug("open_File is clicked")
        
        filename, filetype = QFileDialog.getOpenFileName(self, self._translate("StartingPanel", "Select a book"), "./", self._translate("StartingPanel", "Audiobooks(*.lpf)"))
        if len(filename) > 0: 
            logging.debug(filename)
        else:
            return

        self.signal_switch_window[str].emit(filename)

    def open_Project(self):
        openDirectory = QFileDialog.getExistingDirectory(self, self._translate("StartingPanel", "Select one directory"), self._translate("StartingPanel", "./"))
        logging.debug(openDirectory)
        self.signal_switch_window[str].emit(openDirectory)        

    def eventFilter(self, watched, event):
        if watched == self.ui.label_4:
            if event.type() == QEvent.MouseButtonPress:
                # mouseEvent = QMouseEvent(event)
                if event.buttons() == Qt.LeftButton:
                    logging.debug("Label_4 is clicked!")
                    self.ui.pushButton_New.clicked.emit()
                    return True
        elif watched == self.ui.label_5:
            if event.type() == QEvent.MouseButtonPress:
                # mouseEvent = QMouseEvent(event.type())
                if event.buttons() == Qt.LeftButton:
                    logging.debug("Label_5 is clicked!")
                    self.ui.pushButton_Open_File.clicked.emit()
                    return True
        elif watched == self.ui.label_6:
            if event.type() == QEvent.MouseButtonPress:
                # mouseEvent = QMouseEvent(event)
                if event.buttons() == Qt.LeftButton:
                    logging.debug("Label_6 is clicked!")
                    self.ui.pushButton_Open_Project.clicked.emit()
                    return True

        return super().eventFilter(watched, event)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if hasattr(self, "oldPos"):
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()


