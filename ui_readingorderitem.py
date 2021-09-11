# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReadingOrderItem.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_ReadingOrderItem(object):
    def setupUi(self, ReadingOrderItem):
        if not ReadingOrderItem.objectName():
            ReadingOrderItem.setObjectName(u"ReadingOrderItem")
        ReadingOrderItem.resize(420, 78)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ReadingOrderItem.sizePolicy().hasHeightForWidth())
        ReadingOrderItem.setSizePolicy(sizePolicy)
        ReadingOrderItem.setMinimumSize(QSize(420, 78))
        ReadingOrderItem.setMaximumSize(QSize(420, 78))
        ReadingOrderItem.setStyleSheet(u"background: #333333;\n"
"\n"
"margin: 0px 0px;\n"
"\n"
"QWidget::QFrame {\n"
"	border: 1px solid rgba(255, 255, 255, 0.1);\n"
"	box-sizing: border-box;\n"
"	border-radius: 8px; \n"
"}\n"
"\n"
"/*\n"
"QWidget {\n"
"	left: 0px;\n"
"	right: 0px;\n"
"	top: 0px;\n"
"	bottom: 0px;\n"
"\n"
"	padding: 4px;\n"
"}\n"
"*/\n"
"/*\n"
"QWidget:hover:!pressed\n"
"{\n"
"	background-color: #333333;\n"
"	color: #333333;\n"
"}\n"
"\n"
"\n"
"QWidget:hover\n"
"{\n"
"	background-color: #333333;\n"
"	color: #333333;\n"
"}\n"
"*/\n"
"")
        self.label_Index = QLabel(ReadingOrderItem)
        self.label_Index.setObjectName(u"label_Index")
        self.label_Index.setGeometry(QRect(0, 4, 34, 70))
        font = QFont()
        font.setFamily(u"Noto Sans TC")
        self.label_Index.setFont(font)
        self.label_Index.setStyleSheet(u"font-family: Noto Sans TC;\n"
"font-size: 12px;\n"
"line-height: 17px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: rgba(255, 255, 255, 0.9);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"\n"
"/* margin: 0px 0px; */")
        self.label_Index.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(ReadingOrderItem)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(34, 4, 366, 70))
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"QFrame {\n"
"	background: #404040;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	background: #474747;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_Drag = QLabel(self.frame)
        self.label_Drag.setObjectName(u"label_Drag")
        self.label_Drag.setGeometry(QRect(0, 23, 24, 24))
        self.label_Drag.setPixmap(QPixmap(u":/SVG/svg/icon/common-drag.svg"))
        self.label_Drag.setScaledContents(True)
        self.pushButton_Add = QPushButton(self.frame)
        self.pushButton_Add.setObjectName(u"pushButton_Add")
        self.pushButton_Add.setGeometry(QRect(288, 6, 24, 24))
        self.pushButton_Add.setStyleSheet(u"\n"
"background: #404040;\n"
"border: 0px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/reading-order-add-to-list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Add.setIcon(icon)
        self.pushButton_Add.setIconSize(QSize(24, 24))
        self.pushButton_Remove = QPushButton(self.frame)
        self.pushButton_Remove.setObjectName(u"pushButton_Remove")
        self.pushButton_Remove.setGeometry(QRect(324, 6, 24, 24))
        self.pushButton_Remove.setStyleSheet(u"background: #404040;\n"
"border: 0px;\n"
"\n"
"color: #FFFFFF;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/SVG/svg/icon/common-remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Remove.setIcon(icon1)
        self.pushButton_Remove.setIconSize(QSize(24, 24))
        self.label_Duration = QLabel(self.frame)
        self.label_Duration.setObjectName(u"label_Duration")
        self.label_Duration.setGeometry(QRect(290, 38, 56, 20))
        self.label_Duration.setMinimumSize(QSize(56, 20))
        self.label_Duration.setStyleSheet(u"/* 00:10:05 */\n"
"\n"
"\n"
"position: static;\n"
"width: 52px;\n"
"height: 16px;\n"
"right: 0px;\n"
"top: calc(50% - 16px/2);\n"
"\n"
"font-family: Noto Sans;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 19px;\n"
"text-align: right;\n"
"\n"
"color: rgba(255, 255, 255, 0.6);\n"
"\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 1;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;\n"
"\n"
"/* cell/text */\n"
"\n"
"color: #FFFFFF;")
        self.label_Duration.setText(u"00:00:00")
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(58, 62, 288, 2))
        self.progressBar.setStyleSheet(u"/* Rectangle 48 */\n"
"\n"
"\n"
"position: absolute;\n"
"height: 2px;\n"
"left: 0px;\n"
"right: 0px;\n"
"top: 0px;\n"
"\n"
"background: #666666;")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(28, 6, 258, 24))
        self.lineEdit.setMinimumSize(QSize(258, 24))
        self.lineEdit.setMaximumSize(QSize(258, 24))
        font1 = QFont()
        font1.setFamily(u"Noto Sans TC")
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: #FFFFFF;\n"
"\n"
"	font-family: Noto Sans TC;\n"
"	font-style: normal;\n"
"	font-weight: 400;\n"
"	font-size: 17px;\n"
"	line-height: 24px;\n"
"\n"
"	background: #404040;\n"
"	border: none;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	background: #393939;\n"
"}\n"
"")
        self.lineEdit.setInputMask(u"")
        self.lineEdit.setFrame(True)
        self.pushButton_Play = QPushButton(self.frame)
        self.pushButton_Play.setObjectName(u"pushButton_Play")
        self.pushButton_Play.setGeometry(QRect(32, 40, 16, 16))
        sizePolicy.setHeightForWidth(self.pushButton_Play.sizePolicy().hasHeightForWidth())
        self.pushButton_Play.setSizePolicy(sizePolicy)
        self.pushButton_Play.setMinimumSize(QSize(16, 16))
        self.pushButton_Play.setStyleSheet(u"background: #404040;\n"
"border: 0px;\n"
"color: #FFFFFF;")
        icon2 = QIcon()
        icon2.addFile(u":/SVG/svg/icon/reading-order-play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Play.setIcon(icon2)
        self.pushButton_Play.setIconSize(QSize(16, 16))
        self.label_Href = QLabel(self.frame)
        self.label_Href.setObjectName(u"label_Href")
        self.label_Href.setGeometry(QRect(58, 38, 224, 20))
        self.label_Href.setMinimumSize(QSize(224, 20))
        self.label_Href.setFont(font1)
        self.label_Href.setStyleSheet(u"align-items: center;\n"
"margin: 0px 0px;\n"
"color: #FFFFFF;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"line-height: 20px;")
        self.label_Href.setScaledContents(False)

        self.retranslateUi(ReadingOrderItem)

        QMetaObject.connectSlotsByName(ReadingOrderItem)
    # setupUi

    def retranslateUi(self, ReadingOrderItem):
        ReadingOrderItem.setWindowTitle(QCoreApplication.translate("ReadingOrderItem", u"Form", None))
        self.label_Index.setText(QCoreApplication.translate("ReadingOrderItem", u"0", None))
        self.label_Drag.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_Add.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_Add.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_Remove.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_Remove.setText("")
        self.progressBar.setFormat("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ReadingOrderItem", u"Please input title...", None))
        self.pushButton_Play.setText("")
        self.label_Href.setText(QCoreApplication.translate("ReadingOrderItem", u"*.mp3", None))
    # retranslateUi

