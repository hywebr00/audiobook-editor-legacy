# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TOCListWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TOCListWidget(object):
    def setupUi(self, TOCListWidget):
        if not TOCListWidget.objectName():
            TOCListWidget.setObjectName(u"TOCListWidget")
        TOCListWidget.resize(256, 366)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TOCListWidget.sizePolicy().hasHeightForWidth())
        TOCListWidget.setSizePolicy(sizePolicy)
        TOCListWidget.setMinimumSize(QSize(256, 0))
        TOCListWidget.setMaximumSize(QSize(256, 16777215))
        TOCListWidget.setAcceptDrops(True)
        TOCListWidget.setStyleSheet(u"background: #404040;\n"
"\n"
"")
        self.gridLayout = QGridLayout(TOCListWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_NoItem = QWidget(TOCListWidget)
        self.widget_NoItem.setObjectName(u"widget_NoItem")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_NoItem.sizePolicy().hasHeightForWidth())
        self.widget_NoItem.setSizePolicy(sizePolicy1)
        self.widget_NoItem.setMinimumSize(QSize(256, 36))
        self.widget_NoItem.setMaximumSize(QSize(256, 36))
        self.label_NoItem = QLabel(self.widget_NoItem)
        self.label_NoItem.setObjectName(u"label_NoItem")
        self.label_NoItem.setGeometry(QRect(16, 6, 208, 30))
        sizePolicy1.setHeightForWidth(self.label_NoItem.sizePolicy().hasHeightForWidth())
        self.label_NoItem.setSizePolicy(sizePolicy1)
        self.label_NoItem.setMinimumSize(QSize(208, 30))
        self.label_NoItem.setMaximumSize(QSize(208, 30))
        font = QFont()
        font.setFamily(u"Noto Sans TC")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_NoItem.setFont(font)
        self.label_NoItem.setStyleSheet(u"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 11px;\n"
"line-height: 15px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: rgba(255, 255, 255, 0.45);\n"
"\n"
"\n"
"background: #404040;\n"
"")
        self.label_NoItem.setWordWrap(True)

        self.verticalLayout.addWidget(self.widget_NoItem)

        self.listWidget = QListWidget(TOCListWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)
        self.listWidget.setMinimumSize(QSize(256, 0))
        self.listWidget.setMaximumSize(QSize(256, 16777215))
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	padding: 0px;\n"
"	border: 0px;\n"
"	background: #404040;\n"
"}\n"
"\n"
"// \u8bbe\u7f6e\u5782\u76f4\u6eda\u52a8\u6761\u57fa\u672c\u6837\u5f0f\n"
"QScrollBar:vertical\n"
"{\n"
"    width:8px;\n"
"    background:rgba(0,0,0,0%);\n"
"    margin:0px,0px,0px,0px;\n"
"    padding-top:9px;   // \u7559\u51fa9px\u7ed9\u4e0a\u9762\u548c\u4e0b\u9762\u7684\u7bad\u5934\n"
"    padding-bottom:9px;\n"
"}\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    width:8px;\n"
"    background:rgba(0,0,0,25%);\n"
"    border-radius:4px;   // \u6eda\u52a8\u6761\u4e24\u7aef\u53d8\u6210\u692d\u5706\n"
"    min-height:20;\n"
"}\n"
"QScrollBar::handle:vertical:hover\n"
"{\n"
"    width:8px;\n"
"    background:rgba(0,0,0,50%);   // \u9f20\u6807\u653e\u5230\u6eda\u52a8\u6761\u4e0a\u7684\u65f6\u5019\uff0c\u989c\u8272\u53d8\u6df1\n"
"    border-radius:4px;\n"
"    min-height:20;\n"
"}\n"
"QScrollBar::add-line:vertical   // \u8fd9\u4e2a\u5e94\u8be5\u662f\u8bbe\u7f6e\u4e0b\u7bad\u5934\u7684\uff0c3.png\u5c31\u662f\u7bad\u5934\n"
"{\n"
""
                        "    height:9px;width:8px;\n"
"    subcontrol-position:bottom;\n"
"}\n"
"QScrollBar::sub-line:vertical   // \u8bbe\u7f6e\u4e0a\u7bad\u5934\n"
"{\n"
"    height:9px;width:8px;\n"
"    subcontrol-position:top;\n"
"}\n"
"QScrollBar::add-line:vertical:hover   // \u5f53\u9f20\u6807\u653e\u5230\u4e0b\u7bad\u5934\u4e0a\u7684\u65f6\u5019\n"
"{\n"
"    height:9px;width:8px;\n"
"    subcontrol-position:bottom;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover  // \u5f53\u9f20\u6807\u653e\u5230\u4e0b\u7bad\u5934\u4e0a\u7684\u65f6\u5019\n"
"{\n"
"    height:9px;width:8px;\n"
"    subcontrol-position:top;\n"
"}\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical   // \u5f53\u6eda\u52a8\u6761\u6eda\u52a8\u7684\u65f6\u5019\uff0c\u4e0a\u9762\u7684\u90e8\u5206\u548c\u4e0b\u9762\u7684\u90e8\u5206\n"
"{\n"
"    background:rgba(0,0,0,10%);\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.listWidget.setFrameShadow(QFrame.Sunken)
        self.listWidget.setLineWidth(0)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setAutoScrollMargin(0)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.listWidget.setDefaultDropAction(Qt.CopyAction)
        self.listWidget.setSpacing(0)
        self.listWidget.setItemAlignment(Qt.AlignLeading)

        self.verticalLayout.addWidget(self.listWidget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(TOCListWidget)

        QMetaObject.connectSlotsByName(TOCListWidget)
    # setupUi

    def retranslateUi(self, TOCListWidget):
        TOCListWidget.setWindowTitle(QCoreApplication.translate("TOCListWidget", u"Form", None))
        self.label_NoItem.setText(QCoreApplication.translate("TOCListWidget", u"Please add items from the reading order or supplemental list.", None))
    # retranslateUi

