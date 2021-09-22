# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TOCListWidgetItem.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_TOCListWidgetItem(object):
    def setupUi(self, TOCListWidgetItem):
        if not TOCListWidgetItem.objectName():
            TOCListWidgetItem.setObjectName(u"TOCListWidgetItem")
        TOCListWidgetItem.resize(240, 82)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TOCListWidgetItem.sizePolicy().hasHeightForWidth())
        TOCListWidgetItem.setSizePolicy(sizePolicy)
        TOCListWidgetItem.setMinimumSize(QSize(240, 82))
        TOCListWidgetItem.setMaximumSize(QSize(240, 82))
        TOCListWidgetItem.setStyleSheet(u"background: #404040;\n"
"box-shadow: inset 0px -1px 1px rgba(0, 0, 0, 0.15);\n"
"margin: 0px 0px;\n"
"\n"
"")
        self.label_Title = QLabel(TOCListWidgetItem)
        self.label_Title.setObjectName(u"label_Title")
        self.label_Title.setGeometry(QRect(22, 27, 18, 18))
        self.label_Title.setBaseSize(QSize(18, 18))
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Title.setFont(font)
        self.label_Title.setStyleSheet(u"")
        self.label_Title.setPixmap(QPixmap(u":/SVG/svg/icon/toc-reading-order.svg"))
        self.label_Title.setScaledContents(True)
        self.label_Href = QLabel(TOCListWidgetItem)
        self.label_Href.setObjectName(u"label_Href")
        self.label_Href.setGeometry(QRect(40, 26, 160, 18))
        sizePolicy.setHeightForWidth(self.label_Href.sizePolicy().hasHeightForWidth())
        self.label_Href.setSizePolicy(sizePolicy)
        self.label_Href.setMinimumSize(QSize(160, 18))
        self.label_Href.setMaximumSize(QSize(160, 18))
        font1 = QFont()
        font1.setFamily(u"Noto Sans TC")
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_Href.setFont(font1)
        self.label_Href.setStyleSheet(u"\n"
"	font-family: Noto Sans TC;\n"
"	font-style: normal;\n"
"	font-weight: normal;\n"
"	font-size: 15px;\n"
"	line-height: 20px;\n"
"\n"
"	color: #FFFFFF;\n"
"\n"
"\n"
"")
        self.lineEdit_Title = QLineEdit(TOCListWidgetItem)
        self.lineEdit_Title.setObjectName(u"lineEdit_Title")
        self.lineEdit_Title.setGeometry(QRect(20, 4, 180, 20))
        self.lineEdit_Title.setMinimumSize(QSize(180, 20))
        self.lineEdit_Title.setMaximumSize(QSize(180, 20))
        self.lineEdit_Title.setFont(font1)
        self.lineEdit_Title.setAcceptDrops(False)
        self.lineEdit_Title.setStyleSheet(u"QLineEdit {\n"
"	color: #FFFFFF;\n"
"\n"
"	font-family: Noto Sans TC;\n"
"	font-style: normal;\n"
"	font-weight: normal;\n"
"	font-size: 15px;\n"
"	line-height: 20px;\n"
"	background: #404040;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	background: #393939;\n"
"}\n"
"\n"
"QLineEdit:disabled\n"
"{\n"
"	border: 3px solid rgba(255, 0, 0, 1);\n"
"	background: rgba(0, 0, 0, 0.2);\n"
"	box-sizing: border-box;\n"
"	border-radius: 6px;\n"
"	color: #FFFFFF;\n"
"}")
        self.lineEdit_Title.setFrame(True)
        self.pushButton_Remove = QPushButton(TOCListWidgetItem)
        self.pushButton_Remove.setObjectName(u"pushButton_Remove")
        self.pushButton_Remove.setGeometry(QRect(208, 12, 24, 24))
        self.pushButton_Remove.setMinimumSize(QSize(24, 24))
        self.pushButton_Remove.setBaseSize(QSize(24, 24))
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/common-remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Remove.setIcon(icon)
        self.pushButton_Remove.setIconSize(QSize(24, 24))
        self.label = QLabel(TOCListWidgetItem)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(22, 53, 18, 18))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(18, 18))
        self.label.setBaseSize(QSize(18, 18))
        self.label.setLineWidth(0)
        self.label.setText(u"")
        self.label.setPixmap(QPixmap(u":/SVG/svg/icon/toc-start-time.svg"))
        self.label.setScaledContents(True)
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)
        self.timeEdit_Start = QTimeEdit(TOCListWidgetItem)
        self.timeEdit_Start.setObjectName(u"timeEdit_Start")
        self.timeEdit_Start.setGeometry(QRect(42, 48, 111, 28))
        sizePolicy.setHeightForWidth(self.timeEdit_Start.sizePolicy().hasHeightForWidth())
        self.timeEdit_Start.setSizePolicy(sizePolicy)
        self.timeEdit_Start.setFont(font)
        self.timeEdit_Start.setStyleSheet(u"color: #FFFFFF;\n"
"\n"
"font-family: Noto Sans;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 19px;\n"
"\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border-radius: 6px;\n"
"\n"
"padding-left: 2px;")
        self.timeEdit_Start.setMinimumTime(QTime(0, 0, 0))
        self.timeEdit_Start.setCurrentSection(QDateTimeEdit.HourSection)
        self.timeEdit_Start.setDisplayFormat(u"hh:mm:ss.zzz")
        self.timeEdit_Start.setTime(QTime(0, 0, 0))
        self.line = QFrame(TOCListWidgetItem)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(16, 0, 300, 1))
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setStyleSheet(u"background: #333333;")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)
        self.label_Drag = QLabel(TOCListWidgetItem)
        self.label_Drag.setObjectName(u"label_Drag")
        self.label_Drag.setGeometry(QRect(0, 32, 24, 24))
        self.label_Drag.setMinimumSize(QSize(24, 24))
        self.label_Drag.setBaseSize(QSize(24, 24))
        self.label_Drag.setPixmap(QPixmap(u":/SVG/svg/icon/common-drag.svg"))
        self.label_Drag.setScaledContents(True)

        self.retranslateUi(TOCListWidgetItem)

        QMetaObject.connectSlotsByName(TOCListWidgetItem)
    # setupUi

    def retranslateUi(self, TOCListWidgetItem):
        TOCListWidgetItem.setWindowTitle(QCoreApplication.translate("TOCListWidgetItem", u"Form", None))
        self.label_Title.setText("")
        self.label_Href.setText("")
        self.lineEdit_Title.setInputMask("")
        self.lineEdit_Title.setText("")
        self.lineEdit_Title.setPlaceholderText(QCoreApplication.translate("TOCListWidgetItem", u"Type here...", None))
        self.pushButton_Remove.setText("")
        self.label_Drag.setText("")
    # retranslateUi

