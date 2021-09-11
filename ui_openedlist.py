# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OpenedList.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_OpenedList(object):
    def setupUi(self, OpenedList):
        if not OpenedList.objectName():
            OpenedList.setObjectName(u"OpenedList")
        OpenedList.resize(320, 480)
        OpenedList.setStyleSheet(u"/*background: #262626;*/\n"
"\n"
"\n"
"QListWidget::item:hover{ background: rgba(0, 0, 0, 1); }\n"
"\n"
"")
        self.listWidget = QListWidget(OpenedList)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 32, 320, 420))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setStyleSheet(u"border: 0px;\n"
"")
        self.listWidget.setAutoScroll(False)
        self.listWidget.setAutoScrollMargin(0)
        self.listWidget.setProperty("showDropIndicator", False)
        self.toolButton_Close = QToolButton(OpenedList)
        self.toolButton_Close.setObjectName(u"toolButton_Close")
        self.toolButton_Close.setGeometry(QRect(290, 6, 24, 24))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton_Close.sizePolicy().hasHeightForWidth())
        self.toolButton_Close.setSizePolicy(sizePolicy1)
        self.toolButton_Close.setMinimumSize(QSize(24, 24))
        self.toolButton_Close.setBaseSize(QSize(24, 24))
        self.toolButton_Close.setStyleSheet(u"")
        self.toolButton_Close.setText(u"")
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/starting-panel-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_Close.setIcon(icon)
        self.toolButton_Close.setIconSize(QSize(24, 24))

        self.retranslateUi(OpenedList)

        QMetaObject.connectSlotsByName(OpenedList)
    # setupUi

    def retranslateUi(self, OpenedList):
        OpenedList.setWindowTitle(QCoreApplication.translate("OpenedList", u"Form", None))
    # retranslateUi

