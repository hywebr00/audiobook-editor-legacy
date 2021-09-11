# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SupplementalListWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_SupplementalListWidget(object):
    def setupUi(self, SupplementalListWidget):
        if not SupplementalListWidget.objectName():
            SupplementalListWidget.setObjectName(u"SupplementalListWidget")
        SupplementalListWidget.resize(240, 138)
        SupplementalListWidget.setStyleSheet(u"/* Supplemental List */\n"
"\n"
"\n"
"position: absolute;\n"
"left: 0%;\n"
"right: 0%;\n"
"top: 0%;\n"
"bottom: 0%;\n"
"\n"
"background: #404040;")
        self.label_2 = QLabel(SupplementalListWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(28, 6, 113, 24))
        self.label_2.setStyleSheet(u"position: absolute;\n"
"width: 113px;\n"
"left: 28px;\n"
"top: 6px;\n"
"bottom: 6px;\n"
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
"color: rgba(255, 255, 255, 0.5);\n"
"background: rgba(255, 255, 255, 0.0001);")
        self.label_NoItem = QLabel(SupplementalListWidget)
        self.label_NoItem.setObjectName(u"label_NoItem")
        self.label_NoItem.setGeometry(QRect(16, 36, 208, 15))
        self.label_NoItem.setStyleSheet(u"position: absolute;\n"
"height: 15px;\n"
"left: 16px;\n"
"right: 16px;\n"
"top: 36px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 11px;\n"
"line-height: 15px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: rgba(255, 255, 255, 0.45);\n"
"")
        self.listWidget = QListWidget(SupplementalListWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 36, 240, 98))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.label_3 = QLabel(SupplementalListWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(7, 9, 18, 18))
        self.label_3.setMinimumSize(QSize(18, 18))
        self.label_3.setBaseSize(QSize(18, 18))
        self.label_3.setStyleSheet(u"/* icon/resource-image */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 24px;\n"
"height: 24px;\n"
"left: calc(50% - 24px/2);\n"
"top: calc(50% - 24px/2);")
        self.label_3.setPixmap(QPixmap(u":/SVG/svg/icon/toc-resource.svg"))
        self.label_3.setScaledContents(True)
        self.pushButton_Add = QPushButton(SupplementalListWidget)
        self.pushButton_Add.setObjectName(u"pushButton_Add")
        self.pushButton_Add.setGeometry(QRect(206, 6, 24, 24))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_Add.sizePolicy().hasHeightForWidth())
        self.pushButton_Add.setSizePolicy(sizePolicy1)
        self.pushButton_Add.setMinimumSize(QSize(24, 24))
        self.pushButton_Add.setBaseSize(QSize(24, 24))
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(13)
        self.pushButton_Add.setFont(font)
        self.pushButton_Add.setStyleSheet(u"/* icon/reading-order-add-to-list */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 24px;\n"
"height: 24px;\n"
"left: calc(50% - 24px/2);\n"
"top: calc(50% - 24px/2);\n"
"\n"
"border: 0px;\n"
"")
        self.pushButton_Add.setText(u"")
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/common-add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Add.setIcon(icon)
        self.pushButton_Add.setIconSize(QSize(24, 24))
        self.listWidget.raise_()
        self.label_2.raise_()
        self.label_NoItem.raise_()
        self.label_3.raise_()
        self.pushButton_Add.raise_()

        self.retranslateUi(SupplementalListWidget)

        QMetaObject.connectSlotsByName(SupplementalListWidget)
    # setupUi

    def retranslateUi(self, SupplementalListWidget):
        SupplementalListWidget.setWindowTitle(QCoreApplication.translate("SupplementalListWidget", u"SupplementalListWidget", None))
        self.label_2.setText(QCoreApplication.translate("SupplementalListWidget", u"Supplemental List", None))
        self.label_NoItem.setText(QCoreApplication.translate("SupplementalListWidget", u"There is no supplemental item.", None))
        self.label_3.setText("")
    # retranslateUi

