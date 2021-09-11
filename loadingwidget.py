# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:08:06 2021
"""


import logging
# import sys
# import platform

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# ==> LAUNCH PAGE
from ui_loadingwidget import Ui_LoadingWidget
import CONSTANTS

# ==> GLOBALS
counter = 0

DEBUG = True


# LoadingWidget
class LoadingWidget(QMainWindow):
    switch_window = Signal()
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoadingWidget()
        self.ui.setupUi(self)

        if CONSTANTS.DEBUGGING:
            screen = QGuiApplication.screens()[CONSTANTS.DISPLAY_ON_MONITOR]
            logging.debug("LoadingWidget moved to ({}, {})".format(
                screen.availableGeometry().left() +
                (screen.availableGeometry().width() - self.width()) / 2,
                screen.availableGeometry().top() +
                (screen.availableGeometry().height() - self.height()) / 2))
            self.move(screen.availableGeometry().left() +
                      (screen.availableGeometry().width() - self.width())/2,
                      screen.availableGeometry().top() +
                      (screen.availableGeometry().height() - self.height())/2)

        # self.move(pLeft, pTop)
        # UI ==> INTERFACE CODES
        #

        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        # QTIMER ==> START
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text

        # Change Texts

        # SHOW ==> MAIN WINDOW
        #
        self.show()
        # ==> END

    # ==> APP FUNCTIONS
    #
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)
        self.ui.label_Progress.setText(str(counter) + "%")

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            # self.main = MainWindow()
            # self.main.show()

            self.switch_window.emit()
            # CLOSE LAUNCH PAGE
            self.close()

        # INCREASE COUNTER
        counter += 1

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if hasattr(self, "oldPos"):
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def resizeEvent(self, event):
        width, height = event.size().width(), event.size().height()
        if width != self.minimumWidth() or height != self.minimumHeight():
            event.accept()
            self.resize(self.minimumWidth(), self.minimumHeight())
