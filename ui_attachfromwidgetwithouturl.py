# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AttachFromWidgetWithoutURL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_AttachFromWidgetWithoutURL(object):
    def setupUi(self, AttachFromWidgetWithoutURL):
        if not AttachFromWidgetWithoutURL.objectName():
            AttachFromWidgetWithoutURL.setObjectName(u"AttachFromWidgetWithoutURL")
        AttachFromWidgetWithoutURL.setWindowModality(Qt.ApplicationModal)
        AttachFromWidgetWithoutURL.resize(321, 162)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AttachFromWidgetWithoutURL.sizePolicy().hasHeightForWidth())
        AttachFromWidgetWithoutURL.setSizePolicy(sizePolicy)
        AttachFromWidgetWithoutURL.setMinimumSize(QSize(321, 162))
        AttachFromWidgetWithoutURL.setMaximumSize(QSize(321, 162))
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(14)
        AttachFromWidgetWithoutURL.setFont(font)
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/audiobook-editor-logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        AttachFromWidgetWithoutURL.setWindowIcon(icon)
        AttachFromWidgetWithoutURL.setStyleSheet(u"background: #474747;\n"
"box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.28);\n"
"border-radius: 6px;")
        self.label_AttachFrom = QLabel(AttachFromWidgetWithoutURL)
        self.label_AttachFrom.setObjectName(u"label_AttachFrom")
        self.label_AttachFrom.setGeometry(QRect(14, 9, 81, 16))
        sizePolicy.setHeightForWidth(self.label_AttachFrom.sizePolicy().hasHeightForWidth())
        self.label_AttachFrom.setSizePolicy(sizePolicy)
        self.label_AttachFrom.setMinimumSize(QSize(81, 16))
        self.label_AttachFrom.setMaximumSize(QSize(81, 16))
        self.label_AttachFrom.setStyleSheet(u"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"/* panel/section title */\n"
"\n"
"color: rgba(255, 255, 255, 0.5);")
        self.frame_LocalFile = QFrame(AttachFromWidgetWithoutURL)
        self.frame_LocalFile.setObjectName(u"frame_LocalFile")
        self.frame_LocalFile.setGeometry(QRect(16, 42, 288, 64))
        sizePolicy.setHeightForWidth(self.frame_LocalFile.sizePolicy().hasHeightForWidth())
        self.frame_LocalFile.setSizePolicy(sizePolicy)
        self.frame_LocalFile.setMinimumSize(QSize(288, 64))
        self.frame_LocalFile.setMaximumSize(QSize(288, 64))
        self.frame_LocalFile.setStyleSheet(u"QFrame {	\n"
"	border: 1px dashed rgba(255, 255, 255, 0.4);\n"
"	box-sizing: border-box;\n"
"	border-radius: 6px;\n"
"	margin: 0px 0px;\n"
"}")
        self.frame_LocalFile.setFrameShape(QFrame.StyledPanel)
        self.frame_LocalFile.setFrameShadow(QFrame.Raised)
        self.pushButton_BrowseLocalFile = QPushButton(self.frame_LocalFile)
        self.pushButton_BrowseLocalFile.setObjectName(u"pushButton_BrowseLocalFile")
        self.pushButton_BrowseLocalFile.setGeometry(QRect(84, 25, 16, 16))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_BrowseLocalFile.sizePolicy().hasHeightForWidth())
        self.pushButton_BrowseLocalFile.setSizePolicy(sizePolicy1)
        self.pushButton_BrowseLocalFile.setMinimumSize(QSize(16, 16))
        font1 = QFont()
        font1.setFamily(u"Noto Sans")
        font1.setPointSize(13)
        self.pushButton_BrowseLocalFile.setFont(font1)
        self.pushButton_BrowseLocalFile.setStyleSheet(u"/* common/button */\n"
"\n"
"\n"
"/* Auto Layout */\n"
"\n"
"display: flex;\n"
"flex-direction: row;\n"
"justify-content: center;\n"
"align-items: center;\n"
"padding: 4px 12px;\n"
"\n"
"position: absolute;\n"
"width: 145px;\n"
"height: 26px;\n"
"left: calc(50% - 145px/2 + 0.5px);\n"
"top: calc(50% - 26px/2);\n"
"\n"
"border-radius: 6px;")
        icon1 = QIcon()
        icon1.addFile(u":/SVG/svg/icon/common-add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_BrowseLocalFile.setIcon(icon1)
        self.pushButton_BrowseLocalFile.setIconSize(QSize(16, 16))
        self.lineEdit_BrowseLocalFile = QLineEdit(self.frame_LocalFile)
        self.lineEdit_BrowseLocalFile.setObjectName(u"lineEdit_BrowseLocalFile")
        self.lineEdit_BrowseLocalFile.setGeometry(QRect(104, 23, 101, 18))
        sizePolicy.setHeightForWidth(self.lineEdit_BrowseLocalFile.sizePolicy().hasHeightForWidth())
        self.lineEdit_BrowseLocalFile.setSizePolicy(sizePolicy)
        self.lineEdit_BrowseLocalFile.setMinimumSize(QSize(101, 18))
        self.lineEdit_BrowseLocalFile.setMaximumSize(QSize(288, 18))
        font2 = QFont()
        font2.setFamily(u"Noto Sans TC")
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.lineEdit_BrowseLocalFile.setFont(font2)
        self.lineEdit_BrowseLocalFile.setStyleSheet(u"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #5AB0FF;\n"
"\n"
"margin: 0px 0px;")
        self.pushButton_Create = QPushButton(AttachFromWidgetWithoutURL)
        self.pushButton_Create.setObjectName(u"pushButton_Create")
        self.pushButton_Create.setEnabled(False)
        self.pushButton_Create.setGeometry(QRect(17, 122, 288, 28))
        sizePolicy.setHeightForWidth(self.pushButton_Create.sizePolicy().hasHeightForWidth())
        self.pushButton_Create.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamily(u"Noto Sans TC")
        font3.setPointSize(11)
        self.pushButton_Create.setFont(font3)
        self.pushButton_Create.setStyleSheet(u"/*background: #3095F2;*/\n"
"\n"
"\n"
"QPushButton:disabled {\n"
"border: 1px solid rgba(255, 255, 255, 0.12);\n"
"box-sizing: border-box;\n"
"border-radius: 5px;\n"
"margin: 0px 0px;\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"background: #3095F2;\n"
"border: 1px solid rgba(255, 255, 255, 0.12);\n"
"box-sizing: border-box;\n"
"border-radius: 5px;\n"
"margin: 0px 0px;\n"
"color: #FFFFFF;\n"
"}")
        self.toolButton_Close = QToolButton(AttachFromWidgetWithoutURL)
        self.toolButton_Close.setObjectName(u"toolButton_Close")
        self.toolButton_Close.setGeometry(QRect(291, 5, 24, 24))
        sizePolicy1.setHeightForWidth(self.toolButton_Close.sizePolicy().hasHeightForWidth())
        self.toolButton_Close.setSizePolicy(sizePolicy1)
        self.toolButton_Close.setMinimumSize(QSize(24, 24))
        self.toolButton_Close.setText(u"")
        icon2 = QIcon()
        icon2.addFile(u":/SVG/svg/icon/attach-panel-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_Close.setIcon(icon2)
        self.toolButton_Close.setIconSize(QSize(24, 24))

        self.retranslateUi(AttachFromWidgetWithoutURL)

        QMetaObject.connectSlotsByName(AttachFromWidgetWithoutURL)
    # setupUi

    def retranslateUi(self, AttachFromWidgetWithoutURL):
        AttachFromWidgetWithoutURL.setWindowTitle(QCoreApplication.translate("AttachFromWidgetWithoutURL", u"Select file...", None))
        self.label_AttachFrom.setText(QCoreApplication.translate("AttachFromWidgetWithoutURL", u"Attach from...", None))
        self.pushButton_BrowseLocalFile.setText("")
        self.lineEdit_BrowseLocalFile.setText(QCoreApplication.translate("AttachFromWidgetWithoutURL", u"Browse local file", None))
        self.pushButton_Create.setText(QCoreApplication.translate("AttachFromWidgetWithoutURL", u"Create", None))
    # retranslateUi

