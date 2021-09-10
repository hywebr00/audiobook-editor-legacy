# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Alert.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Alert(object):
    def setupUi(self, Alert):
        if not Alert.objectName():
            Alert.setObjectName(u"Alert")
        Alert.setWindowModality(Qt.ApplicationModal)
        Alert.resize(280, 162)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Alert.sizePolicy().hasHeightForWidth())
        Alert.setSizePolicy(sizePolicy)
        Alert.setMinimumSize(QSize(280, 162))
        Alert.setMaximumSize(QSize(280, 162))
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/audiobook-editor-logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        Alert.setWindowIcon(icon)
        Alert.setStyleSheet(u"background: #474747;\n"
"box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.28);\n"
"border-radius: 6px;")
        self.label = QLabel(Alert)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(14, 9, 231, 16))
        font = QFont()
        font.setFamily(u"Noto Sans TC")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"/*\n"
"font-family: Noto Sans;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"*/\n"
"/* panel/section title */\n"
"\n"
"color: rgba(255, 255, 255, 0.5);")
        self.toolButton_Close = QToolButton(Alert)
        self.toolButton_Close.setObjectName(u"toolButton_Close")
        self.toolButton_Close.setGeometry(QRect(250, 5, 24, 24))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton_Close.sizePolicy().hasHeightForWidth())
        self.toolButton_Close.setSizePolicy(sizePolicy1)
        self.toolButton_Close.setMinimumSize(QSize(24, 24))
        self.toolButton_Close.setToolTipDuration(-1)
        self.toolButton_Close.setText(u"")
        icon1 = QIcon()
        icon1.addFile(u":/SVG/svg/icon/attach-panel-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_Close.setIcon(icon1)
        self.toolButton_Close.setIconSize(QSize(24, 24))
        self.label_Msg = QLabel(Alert)
        self.label_Msg.setObjectName(u"label_Msg")
        self.label_Msg.setGeometry(QRect(16, 34, 247, 74))
        font1 = QFont()
        font1.setFamily(u"Noto Sans TC")
        font1.setPointSize(13)
        self.label_Msg.setFont(font1)
        self.label_Msg.setStyleSheet(u"/*\n"
"font-family: Noto Sans;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"*/\n"
"color: rgba(255, 255, 255, 0.65);")
        self.label_Msg.setWordWrap(True)
        self.pushButton_Ok = QPushButton(Alert)
        self.pushButton_Ok.setObjectName(u"pushButton_Ok")
        self.pushButton_Ok.setGeometry(QRect(16, 124, 247, 28))
        sizePolicy.setHeightForWidth(self.pushButton_Ok.sizePolicy().hasHeightForWidth())
        self.pushButton_Ok.setSizePolicy(sizePolicy)
        self.pushButton_Ok.setFont(font1)
        self.pushButton_Ok.setStyleSheet(u"\n"
"align-items: center;\n"
"\n"
"background: #3095F2;\n"
"border-radius: 5px;\n"
"/*\n"
"font-family: Noto Sans;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"*/\n"
"text-align: center;\n"
"color: #FFFFFF;")

        self.retranslateUi(Alert)

        QMetaObject.connectSlotsByName(Alert)
    # setupUi

    def retranslateUi(self, Alert):
        Alert.setWindowTitle(QCoreApplication.translate("Alert", u"Message", None))
        self.label.setText(QCoreApplication.translate("Alert", u"Alert", None))
        self.label_Msg.setText(QCoreApplication.translate("Alert", u"You must select one directory and keyin the booktitle! You must select one directory and keyin the booktitle!", None))
        self.pushButton_Ok.setText(QCoreApplication.translate("Alert", u"OK", None))
    # retranslateUi

