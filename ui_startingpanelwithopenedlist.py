# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StartingPanelWithOpenedList.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_StartingPanelWithOpenedList(object):
    def setupUi(self, StartingPanelWithOpenedList):
        if not StartingPanelWithOpenedList.objectName():
            StartingPanelWithOpenedList.setObjectName(u"StartingPanelWithOpenedList")
        StartingPanelWithOpenedList.resize(640, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StartingPanelWithOpenedList.sizePolicy().hasHeightForWidth())
        StartingPanelWithOpenedList.setSizePolicy(sizePolicy)
        StartingPanelWithOpenedList.setMinimumSize(QSize(640, 480))
        StartingPanelWithOpenedList.setMaximumSize(QSize(640, 480))
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/AudiobookEditorLogo@16.svg", QSize(), QIcon.Normal, QIcon.Off)
        StartingPanelWithOpenedList.setWindowIcon(icon)
        StartingPanelWithOpenedList.setStyleSheet(u"/* starting panel */\n"
"\n"
"\n"
"position: relative;\n"
"width: 640px;\n"
"height: 480px;\n"
"\n"
"background: #333333;\n"
"")
        self.label = QLabel(StartingPanelWithOpenedList)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 100, 60, 60))
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setBaseSize(QSize(60, 60))
        self.label.setStyleSheet(u"/* Rectangle 39 */\n"
"\n"
"\n"
"position: absolute;\n"
"height: 60px;\n"
"left: 130px;\n"
"right: 130px;\n"
"top: 100px;\n"
"\n"
"background: rgba(10, 110, 202, 0.3);\n"
"border-radius: 10px;")
        self.label.setPixmap(QPixmap(u":/SVG/svg/icon/AudiobookEditorLogo@16.svg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(StartingPanelWithOpenedList)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(73, 186, 174, 28))
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
        self.label_3 = QLabel(StartingPanelWithOpenedList)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(22, 238, 276, 45))
        self.label_3.setStyleSheet(u"position: static;\n"
"width: 276px;\n"
"height: 45px;\n"
"left: 22px;\n"
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
"flex-grow: 0;\n"
"margin: 00px 0px;")
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.frame_Right = QFrame(StartingPanelWithOpenedList)
        self.frame_Right.setObjectName(u"frame_Right")
        self.frame_Right.setGeometry(QRect(320, 0, 320, 480))
        self.frame_Right.setStyleSheet(u"/* recently open section */\n"
"\n"
"\n"
"\n"
"\n"
"background: #262626;\n"
"\n"
"border : 0px")
        self.frame_Right.setFrameShape(QFrame.StyledPanel)
        self.frame_Right.setFrameShadow(QFrame.Raised)
        self.frame_Right.setLineWidth(0)
        self.verticalLayoutWidget = QWidget(self.frame_Right)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 331, 549))
        self.verticalLayout_Right = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_Right.setSpacing(0)
        self.verticalLayout_Right.setObjectName(u"verticalLayout_Right")
        self.verticalLayout_Right.setContentsMargins(0, 0, 0, 0)
        self.pushButton_New = QPushButton(StartingPanelWithOpenedList)
        self.pushButton_New.setObjectName(u"pushButton_New")
        self.pushButton_New.setGeometry(QRect(36, 332, 24, 24))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_New.sizePolicy().hasHeightForWidth())
        self.pushButton_New.setSizePolicy(sizePolicy1)
        self.pushButton_New.setMinimumSize(QSize(24, 24))
        self.pushButton_New.setBaseSize(QSize(24, 24))
        self.pushButton_New.setStyleSheet(u"\n"
"background: rgba(255,255,255, 0);\n"
"")
        self.pushButton_New.setText(u"")
        icon1 = QIcon()
        icon1.addFile(u":/SVG/svg/icon/welcome-new.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_New.setIcon(icon1)
        self.pushButton_New.setIconSize(QSize(24, 24))
        self.label_4 = QLabel(StartingPanelWithOpenedList)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 326, 194, 36))
        self.label_4.setStyleSheet(u"/* Create a new audiobook project */\n"
"\n"
"\n"
"position: static;\n"
"width: 194px;\n"
"height: 24px;\n"
"left: 60px;\n"
"top: 6px;\n"
"\n"
"font-family: Noto Sans;\n"
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
"margin: 0px 0px;")
        self.pushButton_Open_File = QPushButton(StartingPanelWithOpenedList)
        self.pushButton_Open_File.setObjectName(u"pushButton_Open_File")
        self.pushButton_Open_File.setGeometry(QRect(36, 368, 24, 24))
        sizePolicy1.setHeightForWidth(self.pushButton_Open_File.sizePolicy().hasHeightForWidth())
        self.pushButton_Open_File.setSizePolicy(sizePolicy1)
        self.pushButton_Open_File.setMinimumSize(QSize(24, 24))
        self.pushButton_Open_File.setBaseSize(QSize(24, 24))
        self.pushButton_Open_File.setStyleSheet(u"background: rgba(255, 255, 255, 0);")
        self.pushButton_Open_File.setText(u"")
        icon2 = QIcon()
        icon2.addFile(u":/SVG/svg/icon/welcome-file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Open_File.setIcon(icon2)
        self.pushButton_Open_File.setIconSize(QSize(24, 24))
        self.label_5 = QLabel(StartingPanelWithOpenedList)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 362, 194, 36))
        self.label_5.setStyleSheet(u"/* Open a project or file */\n"
"\n"
"\n"
"position: static;\n"
"width: 194px;\n"
"height: 24px;\n"
"left: 60px;\n"
"top: 6px;\n"
"\n"
"font-family: Noto Sans;\n"
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
"margin: 0px 0px;")
        self.pushButton_Open_Project = QPushButton(StartingPanelWithOpenedList)
        self.pushButton_Open_Project.setObjectName(u"pushButton_Open_Project")
        self.pushButton_Open_Project.setGeometry(QRect(36, 402, 24, 24))
        sizePolicy1.setHeightForWidth(self.pushButton_Open_Project.sizePolicy().hasHeightForWidth())
        self.pushButton_Open_Project.setSizePolicy(sizePolicy1)
        self.pushButton_Open_Project.setMinimumSize(QSize(24, 24))
        self.pushButton_Open_Project.setStyleSheet(u"background: rgba(255, 255, 255, 0);")
        self.pushButton_Open_Project.setText(u"")
        icon3 = QIcon()
        icon3.addFile(u":/SVG/svg/icon/welcome-folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Open_Project.setIcon(icon3)
        self.pushButton_Open_Project.setIconSize(QSize(24, 24))
        self.label_6 = QLabel(StartingPanelWithOpenedList)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 398, 194, 36))
        self.label_6.setStyleSheet(u"/* Open a project or file */\n"
"\n"
"\n"
"position: static;\n"
"width: 194px;\n"
"height: 24px;\n"
"left: 60px;\n"
"top: 6px;\n"
"\n"
"font-family: Noto Sans;\n"
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
"margin: 0px 0px;")

        self.retranslateUi(StartingPanelWithOpenedList)

        QMetaObject.connectSlotsByName(StartingPanelWithOpenedList)
    # setupUi

    def retranslateUi(self, StartingPanelWithOpenedList):
        StartingPanelWithOpenedList.setWindowTitle(QCoreApplication.translate("StartingPanelWithOpenedList", u"Audiobook Editor", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("StartingPanelWithOpenedList", u"Audiobook Editor", None))
        self.label_3.setText(QCoreApplication.translate("StartingPanelWithOpenedList", u"This is a public prototype conforming and demostrating the Audiobooks W3C Recommendation 10 November 2020. Have fun :)", None))
        self.label_4.setText(QCoreApplication.translate("StartingPanelWithOpenedList", u"Create a new audiobook project", None))
        self.label_5.setText(QCoreApplication.translate("StartingPanelWithOpenedList", u"Open a file", None))
        self.label_6.setText(QCoreApplication.translate("StartingPanelWithOpenedList", u"Open a project", None))
    # retranslateUi

