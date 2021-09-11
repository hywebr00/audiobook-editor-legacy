# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StartingPanel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_StartingPanel(object):
    def setupUi(self, StartingPanel):
        if not StartingPanel.objectName():
            StartingPanel.setObjectName(u"StartingPanel")
        StartingPanel.resize(640, 480)
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/AudiobookEditorLogo@16.svg", QSize(), QIcon.Normal, QIcon.Off)
        StartingPanel.setWindowIcon(icon)
        StartingPanel.setStyleSheet(u"/* starting panel */\n"
"\n"
"\n"
"position: relative;\n"
"width: 640px;\n"
"height: 480px;\n"
"\n"
"background: #333333;")
        self.label = QLabel(StartingPanel)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 100, 60, 60))
        self.label.setStyleSheet(u"/* Rectangle 39 */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 60px;\n"
"height: 60px;\n"
"left: 290px;\n"
"top: 100px;\n"
"\n"
"background: rgba(10, 110, 202, 0.3);\n"
"border-radius: 30px;")
        self.label.setPixmap(QPixmap(u":/SVG/svg/icon/AudiobookEditorLogo@16.svg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(StartingPanel)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(233, 186, 174, 28))
        font = QFont()
        font.setFamily(u"Noto Sans TC")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"position: static;\n"
"width: 174px;\n"
"height: 28px;\n"
"left: 73px;\n"
"top: 16px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"line-height: 27px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(StartingPanel)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(48, 238, 544, 30))
        self.label_3.setStyleSheet(u"/* This is a public prototype conforming and demostrating the Audiobooks. W3C Recommendation 10 November 2020. Have fun :) */\n"
"\n"
"\n"
"position: static;\n"
"width: 504px;\n"
"height: 30px;\n"
"left: 48px;\n"
"top: 8px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 11px;\n"
"line-height: 15px;\n"
"text-align: center;\n"
"\n"
"color: rgba(255, 255, 255, 0.6);\n"
"\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 1;\n"
"margin:0px 0px;")
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_4 = QLabel(StartingPanel)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(241, 338, 194, 36))
        self.label_4.setStyleSheet(u"position: static;\n"
"width: 194px;\n"
"height: 24px;\n"
"left: 60px;\n"
"top: 6px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"/* icon/primary */\n"
"\n"
"color: #5AB0FF;\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 1;\n"
"align-self: stretch;\n"
"flex-grow: 0;\n"
"margin: 6px 0px;")
        self.label_5 = QLabel(StartingPanel)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(241, 374, 194, 36))
        self.label_5.setStyleSheet(u"position: static;\n"
"width: 194px;\n"
"height: 24px;\n"
"left: 60px;\n"
"top: 6px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"/* icon/primary */\n"
"\n"
"color: #5AB0FF;\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 1;\n"
"align-self: stretch;\n"
"flex-grow: 0;\n"
"margin: 6px 0px;")
        self.pushButton_New = QPushButton(StartingPanel)
        self.pushButton_New.setObjectName(u"pushButton_New")
        self.pushButton_New.setGeometry(QRect(211, 344, 24, 24))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_New.sizePolicy().hasHeightForWidth())
        self.pushButton_New.setSizePolicy(sizePolicy)
        self.pushButton_New.setStyleSheet(u"border : 0px")
        icon1 = QIcon()
        icon1.addFile(u":/SVG/svg/icon/welcome-new.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_New.setIcon(icon1)
        self.pushButton_New.setIconSize(QSize(24, 24))
        self.pushButton_Open_File = QPushButton(StartingPanel)
        self.pushButton_Open_File.setObjectName(u"pushButton_Open_File")
        self.pushButton_Open_File.setGeometry(QRect(211, 380, 24, 24))
        sizePolicy.setHeightForWidth(self.pushButton_Open_File.sizePolicy().hasHeightForWidth())
        self.pushButton_Open_File.setSizePolicy(sizePolicy)
        self.pushButton_Open_File.setStyleSheet(u"border : 0px")
        self.pushButton_Open_File.setText(u"")
        icon2 = QIcon()
        icon2.addFile(u":/SVG/svg/icon/welcome-file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Open_File.setIcon(icon2)
        self.pushButton_Open_File.setIconSize(QSize(24, 24))
        self.label_6 = QLabel(StartingPanel)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(241, 410, 194, 36))
        self.label_6.setStyleSheet(u"position: static;\n"
"width: 194px;\n"
"height: 24px;\n"
"left: 60px;\n"
"top: 6px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"/* icon/primary */\n"
"\n"
"color: #5AB0FF;\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 1;\n"
"align-self: stretch;\n"
"flex-grow: 0;\n"
"margin: 6px 0px;")
        self.pushButton_Open_Project = QPushButton(StartingPanel)
        self.pushButton_Open_Project.setObjectName(u"pushButton_Open_Project")
        self.pushButton_Open_Project.setGeometry(QRect(211, 416, 24, 24))
        sizePolicy.setHeightForWidth(self.pushButton_Open_Project.sizePolicy().hasHeightForWidth())
        self.pushButton_Open_Project.setSizePolicy(sizePolicy)
        self.pushButton_Open_Project.setStyleSheet(u"border : 0px")
        self.pushButton_Open_Project.setText(u"")
        icon3 = QIcon()
        icon3.addFile(u":/SVG/svg/icon/welcome-folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Open_Project.setIcon(icon3)
        self.pushButton_Open_Project.setIconSize(QSize(24, 24))
        self.toolButton_Close = QToolButton(StartingPanel)
        self.toolButton_Close.setObjectName(u"toolButton_Close")
        self.toolButton_Close.setGeometry(QRect(610, 6, 24, 24))
        self.toolButton_Close.setMinimumSize(QSize(24, 24))
        self.toolButton_Close.setBaseSize(QSize(24, 24))
        self.toolButton_Close.setStyleSheet(u"border : 0px")
        self.toolButton_Close.setText(u"")
        icon4 = QIcon()
        icon4.addFile(u":/SVG/svg/icon/starting-panel-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_Close.setIcon(icon4)
        self.toolButton_Close.setIconSize(QSize(24, 24))

        self.retranslateUi(StartingPanel)

        QMetaObject.connectSlotsByName(StartingPanel)
    # setupUi

    def retranslateUi(self, StartingPanel):
        StartingPanel.setWindowTitle(QCoreApplication.translate("StartingPanel", u"Audiobook Editor", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("StartingPanel", u"Audiobook Editor", None))
        self.label_3.setText(QCoreApplication.translate("StartingPanel", u"This is a public prototype conforming and demostrating the Audiobooks W3C Recommendation 10 November 2020. Have fun :)", None))
        self.label_4.setText(QCoreApplication.translate("StartingPanel", u"Create a new audiobook project", None))
        self.label_5.setText(QCoreApplication.translate("StartingPanel", u"Open a file", None))
        self.pushButton_New.setText("")
        self.label_6.setText(QCoreApplication.translate("StartingPanel", u"Open a project", None))
    # retranslateUi

