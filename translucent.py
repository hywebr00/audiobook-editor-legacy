# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 02:24:00 2021

@ref: https://www.codestudyblog.com/cnb/0319212758.html
"""


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MaskWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setStyleSheet("background:rgba(0,0,0,102);")
        self.setAttribute(Qt.WA_DeleteOnClose)

    def show(self):
        """Rewrite show, set the mask size to be consistent with the parent
        """
        if self.parent() is None:
            return

        parent_rect = self.parent().geometry()
        self.setGeometry(0, 0, parent_rect.width(), parent_rect.height())
        super().show()

