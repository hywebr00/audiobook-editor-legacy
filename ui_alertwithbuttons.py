# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AlertWithButtons.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_AlertWithButtons(object):
    def setupUi(self, AlertWithButtons):
        if not AlertWithButtons.objectName():
            AlertWithButtons.setObjectName(u"AlertWithButtons")
        AlertWithButtons.setWindowModality(Qt.ApplicationModal)
        AlertWithButtons.resize(280, 162)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AlertWithButtons.sizePolicy().hasHeightForWidth())
        AlertWithButtons.setSizePolicy(sizePolicy)
        AlertWithButtons.setMinimumSize(QSize(280, 162))
        AlertWithButtons.setMaximumSize(QSize(280, 162))
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/audiobook-editor-logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        AlertWithButtons.setWindowIcon(icon)
        AlertWithButtons.setStyleSheet(u"background: #474747;\n"
"box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.28);\n"
"border-radius: 6px;")
        self.label = QLabel(AlertWithButtons)
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
        self.toolButton_Close = QToolButton(AlertWithButtons)
        self.toolButton_Close.setObjectName(u"toolButton_Close")
        self.toolButton_Close.setGeometry(QRect(250, 5, 24, 24))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton_Close.sizePolicy().hasHeightForWidth())
        self.toolButton_Close.setSizePolicy(sizePolicy1)
        self.toolButton_Close.setMinimumSize(QSize(24, 24))
        self.toolButton_Close.setBaseSize(QSize(24, 24))
        self.toolButton_Close.setToolTipDuration(-1)
        self.toolButton_Close.setText(u"")
        icon1 = QIcon()
        icon1.addFile(u":/SVG/svg/icon/attach-panel-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_Close.setIcon(icon1)
        self.toolButton_Close.setIconSize(QSize(24, 24))
        self.label_Msg = QLabel(AlertWithButtons)
        self.label_Msg.setObjectName(u"label_Msg")
        self.label_Msg.setGeometry(QRect(16, 34, 247, 64))
        self.label_Msg.setStyleSheet(u"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"\n"
"color: rgba(255, 255, 255, 0.65);")
        self.label_Msg.setWordWrap(True)
        self.pushButton_Ok = QPushButton(AlertWithButtons)
        self.pushButton_Ok.setObjectName(u"pushButton_Ok")
        self.pushButton_Ok.setGeometry(QRect(150, 114, 114, 28))
        sizePolicy.setHeightForWidth(self.pushButton_Ok.sizePolicy().hasHeightForWidth())
        self.pushButton_Ok.setSizePolicy(sizePolicy)
        self.pushButton_Ok.setStyleSheet(u"align-items: center;\n"
"\n"
"background: #3095F2;\n"
"border-radius: 5px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.pushButton_Cancel = QPushButton(AlertWithButtons)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")
        self.pushButton_Cancel.setGeometry(QRect(20, 114, 114, 28))
        sizePolicy.setHeightForWidth(self.pushButton_Cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_Cancel.setSizePolicy(sizePolicy)
        self.pushButton_Cancel.setStyleSheet(u"align-items: center;\n"
"\n"
"background: #3095F2;\n"
"border-radius: 5px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")

        self.retranslateUi(AlertWithButtons)

        QMetaObject.connectSlotsByName(AlertWithButtons)
    # setupUi

    def retranslateUi(self, AlertWithButtons):
        AlertWithButtons.setWindowTitle(QCoreApplication.translate("AlertWithButtons", u"Message and Choice", None))
        self.label.setText(QCoreApplication.translate("AlertWithButtons", u"Alert", None))
        self.label_Msg.setText(QCoreApplication.translate("AlertWithButtons", u"You must select one directory and keyin the booktitle! You must select one directory and keyin the booktitle!", None))
        self.pushButton_Ok.setText(QCoreApplication.translate("AlertWithButtons", u"OK", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("AlertWithButtons", u"Cancel", None))
    # retranslateUi

