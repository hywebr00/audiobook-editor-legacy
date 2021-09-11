# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OpenedListItem.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_OpenedListItem(object):
    def setupUi(self, OpenedListItem):
        if not OpenedListItem.objectName():
            OpenedListItem.setObjectName(u"OpenedListItem")
        OpenedListItem.resize(320, 52)
        OpenedListItem.setStyleSheet(u"background: rgba(0, 0, 0, 0.4);")
        self.label_Cover = QLabel(OpenedListItem)
        self.label_Cover.setObjectName(u"label_Cover")
        self.label_Cover.setGeometry(QRect(24, 10, 32, 32))
        self.label_Cover.setMinimumSize(QSize(32, 32))
        self.label_Cover.setStyleSheet(u"/* recent open item */\n"
"\n"
"\n"
"position: static;\n"
"width: 320px;\n"
"height: 52px;\n"
"left: 0px;\n"
"top: 32px;\n"
"\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.label_Cover.setPixmap(QPixmap(u":/SVG/svg/icon/AudiobookEditorLogo@16.svg"))
        self.label_Cover.setScaledContents(True)
        self.label_Title = QLabel(OpenedListItem)
        self.label_Title.setObjectName(u"label_Title")
        self.label_Title.setGeometry(QRect(68, 8, 144, 21))
        self.label_Title.setStyleSheet(u"position: absolute;\n"
"width: 144px;\n"
"height: 21px;\n"
"left: 0px;\n"
"top: 0px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 21px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"background: rgba(0, 0, 0, 0);")
        self.label_Path = QLabel(OpenedListItem)
        self.label_Path.setObjectName(u"label_Path")
        self.label_Path.setGeometry(QRect(68, 29, 228, 15))
        self.label_Path.setStyleSheet(u"position: static;\n"
"width: 228px;\n"
"height: 15px;\n"
"left: 0px;\n"
"top: 29px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 11px;\n"
"line-height: 15px;\n"
"/* identical to box height */\n"
"\n"
"background: rgba(0, 0, 0, 0);\n"
"\n"
"color: rgba(255, 255, 255, 0.5);\n"
"\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 1;\n"
"align-self: stretch;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.label_Ago = QLabel(OpenedListItem)
        self.label_Ago.setObjectName(u"label_Ago")
        self.label_Ago.setGeometry(QRect(232, 8, 64, 21))
        font = QFont()
        font.setFamily(u"Noto Sans TC")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Ago.setFont(font)
        self.label_Ago.setStyleSheet(u"position: absolute;\n"
"width: 64px;\n"
"height: 21px;\n"
"left: 164px;\n"
"top: 0px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 11px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: right;\n"
"\n"
"color: #7EC1FF;\n"
"\n"
"background: rgba(0, 0, 0, 0);")
        self.label_Ago.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.retranslateUi(OpenedListItem)

        QMetaObject.connectSlotsByName(OpenedListItem)
    # setupUi

    def retranslateUi(self, OpenedListItem):
        OpenedListItem.setWindowTitle(QCoreApplication.translate("OpenedListItem", u"Form", None))
        self.label_Cover.setText("")
        self.label_Title.setText(QCoreApplication.translate("OpenedListItem", u"Approach", None))
        self.label_Path.setText(QCoreApplication.translate("OpenedListItem", u"~/Desktop/Audiobook-Demo/test-12/Approach...", None))
        self.label_Ago.setText(QCoreApplication.translate("OpenedListItem", u"3 days ago", None))
    # retranslateUi

