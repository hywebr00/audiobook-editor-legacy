# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AttachFromWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_AttachFromWidget(object):
    def setupUi(self, AttachFromWidget):
        if not AttachFromWidget.objectName():
            AttachFromWidget.setObjectName(u"AttachFromWidget")
        AttachFromWidget.setWindowModality(Qt.ApplicationModal)
        AttachFromWidget.resize(320, 242)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AttachFromWidget.sizePolicy().hasHeightForWidth())
        AttachFromWidget.setSizePolicy(sizePolicy)
        AttachFromWidget.setMinimumSize(QSize(320, 242))
        AttachFromWidget.setMaximumSize(QSize(320, 242))
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(14)
        AttachFromWidget.setFont(font)
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/audiobook-editor-logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        AttachFromWidget.setWindowIcon(icon)
        AttachFromWidget.setStyleSheet(u"background: #474747;\n"
"box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.28);\n"
"border-radius: 6px;")
        self.label_AttachFrom = QLabel(AttachFromWidget)
        self.label_AttachFrom.setObjectName(u"label_AttachFrom")
        self.label_AttachFrom.setGeometry(QRect(14, 9, 81, 16))
        sizePolicy.setHeightForWidth(self.label_AttachFrom.sizePolicy().hasHeightForWidth())
        self.label_AttachFrom.setSizePolicy(sizePolicy)
        self.label_AttachFrom.setMinimumSize(QSize(81, 16))
        self.label_AttachFrom.setMaximumSize(QSize(81, 16))
        self.label_AttachFrom.setStyleSheet(u"\n"
"position: absolute;\n"
"width: 81px;\n"
"height: 16px;\n"
"left: 14px;\n"
"top: calc(50% - 16px/2);\n"
"\n"
"font-family: Noto Sans TC;\n"
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
        self.pushButton_Add = QPushButton(AttachFromWidget)
        self.pushButton_Add.setObjectName(u"pushButton_Add")
        self.pushButton_Add.setGeometry(QRect(262, 44, 41, 19))
        sizePolicy.setHeightForWidth(self.pushButton_Add.sizePolicy().hasHeightForWidth())
        self.pushButton_Add.setSizePolicy(sizePolicy)
        self.pushButton_Add.setMinimumSize(QSize(41, 19))
        self.pushButton_Add.setMaximumSize(QSize(41, 19))
        font1 = QFont()
        font1.setFamily(u"Noto Sans TC")
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(62)
        self.pushButton_Add.setFont(font1)
        self.pushButton_Add.setStyleSheet(u"position: absolute;\n"
"left: 0px;\n"
"right: 0px;\n"
"top: 0px;\n"
"bottom: 0px;\n"
"\n"
"/* cell/text input background */\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border-radius: 6px;\n"
"\n"
"/* Add */\n"
"\n"
"\n"
"position: static;\n"
"height: 18px;\n"
"left: 8px;\n"
"right: 8px;\n"
"top: calc(50% - 18px/2);\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"/* identical to box height */\n"
"\n"
"/*text-align: right;*/\n"
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
        self.label_Or = QLabel(AttachFromWidget)
        self.label_Or.setObjectName(u"label_Or")
        self.label_Or.setGeometry(QRect(153, 74, 22, 18))
        sizePolicy.setHeightForWidth(self.label_Or.sizePolicy().hasHeightForWidth())
        self.label_Or.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"Noto Sans")
        font2.setPointSize(11)
        self.label_Or.setFont(font2)
        self.frame_LocalFile = QFrame(AttachFromWidget)
        self.frame_LocalFile.setObjectName(u"frame_LocalFile")
        self.frame_LocalFile.setGeometry(QRect(16, 100, 288, 64))
        sizePolicy.setHeightForWidth(self.frame_LocalFile.sizePolicy().hasHeightForWidth())
        self.frame_LocalFile.setSizePolicy(sizePolicy)
        self.frame_LocalFile.setMinimumSize(QSize(288, 64))
        self.frame_LocalFile.setMaximumSize(QSize(288, 64))
        self.frame_LocalFile.setStyleSheet(u"/* Frame 28 */\n"
"\n"
"\n"
"position: static;\n"
"width: 288px;\n"
"height: 64px;\n"
"left: calc(50% - 288px/2);\n"
"top: 8px;\n"
"\n"
"border: 1px dashed rgba(255, 255, 255, 0.4);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"align-self: stretch;\n"
"flex-grow: 1;\n"
"margin: 0px 0px;")
        self.frame_LocalFile.setFrameShape(QFrame.StyledPanel)
        self.frame_LocalFile.setFrameShadow(QFrame.Raised)
        self.pushButton_BrowseLocalFile = QPushButton(self.frame_LocalFile)
        self.pushButton_BrowseLocalFile.setObjectName(u"pushButton_BrowseLocalFile")
        self.pushButton_BrowseLocalFile.setGeometry(QRect(84, 25, 14, 14))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_BrowseLocalFile.sizePolicy().hasHeightForWidth())
        self.pushButton_BrowseLocalFile.setSizePolicy(sizePolicy1)
        self.pushButton_BrowseLocalFile.setMinimumSize(QSize(14, 14))
        font3 = QFont()
        font3.setFamily(u"Noto Sans")
        font3.setPointSize(13)
        self.pushButton_BrowseLocalFile.setFont(font3)
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
        self.pushButton_BrowseLocalFile.setIconSize(QSize(14, 14))
        self.lineEdit_BrowseLocalFile = QLineEdit(self.frame_LocalFile)
        self.lineEdit_BrowseLocalFile.setObjectName(u"lineEdit_BrowseLocalFile")
        self.lineEdit_BrowseLocalFile.setGeometry(QRect(104, 23, 162, 20))
        sizePolicy.setHeightForWidth(self.lineEdit_BrowseLocalFile.sizePolicy().hasHeightForWidth())
        self.lineEdit_BrowseLocalFile.setSizePolicy(sizePolicy)
        self.lineEdit_BrowseLocalFile.setMinimumSize(QSize(126, 20))
        self.lineEdit_BrowseLocalFile.setMaximumSize(QSize(268, 20))
        font4 = QFont()
        font4.setFamily(u"Noto Sans TC")
        font4.setPointSize(8)
        self.lineEdit_BrowseLocalFile.setFont(font4)
        self.lineEdit_BrowseLocalFile.setStyleSheet(u"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #5AB0FF;\n"
"\n"
"\n"
"margin: 0px 0px;")
        self.pushButton_Create = QPushButton(AttachFromWidget)
        self.pushButton_Create.setObjectName(u"pushButton_Create")
        self.pushButton_Create.setEnabled(False)
        self.pushButton_Create.setGeometry(QRect(16, 202, 288, 28))
        sizePolicy.setHeightForWidth(self.pushButton_Create.sizePolicy().hasHeightForWidth())
        self.pushButton_Create.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setFamily(u"Noto Sans TC")
        font5.setPointSize(11)
        self.pushButton_Create.setFont(font5)
        self.pushButton_Create.setStyleSheet(u"/*background: #3095F2;*/\n"
"/*border: 1px solid rgba(255, 255, 255, 0.12);\n"
"box-sizing: border-box;\n"
"border-radius: 5px;\n"
"margin: 0px 0px;*/\n"
"\n"
"QPushButton:disabled {\n"
"border: 1px solid rgba(255, 255, 255, 0.12);\n"
"box-sizing: border-box;\n"
"border-radius: 5px;\n"
"margin: 0px 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:enabled {\n"
"background: #3095F2;\n"
"\n"
"border: 1px solid rgba(255, 255, 255, 0.12);\n"
"box-sizing: border-box;\n"
"border-radius: 5px;\n"
"margin: 0px 0px;\n"
"}\n"
"")
        self.lineEdit_URL = QLineEdit(AttachFromWidget)
        self.lineEdit_URL.setObjectName(u"lineEdit_URL")
        self.lineEdit_URL.setGeometry(QRect(24, 44, 230, 19))
        sizePolicy.setHeightForWidth(self.lineEdit_URL.sizePolicy().hasHeightForWidth())
        self.lineEdit_URL.setSizePolicy(sizePolicy)
        self.lineEdit_URL.setMinimumSize(QSize(230, 19))
        self.lineEdit_URL.setMaximumSize(QSize(230, 19))
        font6 = QFont()
        font6.setFamily(u"Noto Sans TC")
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.lineEdit_URL.setFont(font6)
        self.lineEdit_URL.setStyleSheet(u"/* Rectangle 8 */\n"
"\n"
"\n"
"position: absolute;\n"
"left: 0px;\n"
"right: 0px;\n"
"top: 0px;\n"
"bottom: 0px;\n"
"\n"
"/* cell/text input background */\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border: 1px solid rgba(0, 0, 0, 0.05);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"\n"
"/* https:// */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 230px;\n"
"height: 19px;\n"
"left: 8px;\n"
"top: calc(50% - 19px/2 - 0.5px);\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 19px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"/* cell/text */\n"
"\n"
"color: #FFFFFF;")
        self.label_ErrorMessage = QLabel(AttachFromWidget)
        self.label_ErrorMessage.setObjectName(u"label_ErrorMessage")
        self.label_ErrorMessage.setGeometry(QRect(16, 175, 288, 16))
        sizePolicy.setHeightForWidth(self.label_ErrorMessage.sizePolicy().hasHeightForWidth())
        self.label_ErrorMessage.setSizePolicy(sizePolicy)
        self.label_ErrorMessage.setStyleSheet(u"\n"
"position: static;\n"
"width: 87px;\n"
"height: 16px;\n"
"left: 16px;\n"
"top: 3px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: #E77465;\n"
"\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")

        self.retranslateUi(AttachFromWidget)

        QMetaObject.connectSlotsByName(AttachFromWidget)
    # setupUi

    def retranslateUi(self, AttachFromWidget):
        AttachFromWidget.setWindowTitle(QCoreApplication.translate("AttachFromWidget", u"Form", None))
        self.label_AttachFrom.setText(QCoreApplication.translate("AttachFromWidget", u"Attach from...", None))
        self.pushButton_Add.setText(QCoreApplication.translate("AttachFromWidget", u"Add", None))
        self.label_Or.setText(QCoreApplication.translate("AttachFromWidget", u"or", None))
        self.pushButton_BrowseLocalFile.setText("")
        self.lineEdit_BrowseLocalFile.setText(QCoreApplication.translate("AttachFromWidget", u"Browse local file", None))
        self.pushButton_Create.setText(QCoreApplication.translate("AttachFromWidget", u"Create", None))
        self.lineEdit_URL.setText(QCoreApplication.translate("AttachFromWidget", u"http://", None))
        self.label_ErrorMessage.setText(QCoreApplication.translate("AttachFromWidget", u"Error message.", None))
    # retranslateUi

