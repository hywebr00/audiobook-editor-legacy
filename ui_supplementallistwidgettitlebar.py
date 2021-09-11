# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SupplementalListWidgetTitleBar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_SupplementalListWidgetTitleBar(object):
    def setupUi(self, SupplementalListWidgetTitleBar):
        if not SupplementalListWidgetTitleBar.objectName():
            SupplementalListWidgetTitleBar.setObjectName(u"SupplementalListWidgetTitleBar")
        SupplementalListWidgetTitleBar.resize(256, 36)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SupplementalListWidgetTitleBar.sizePolicy().hasHeightForWidth())
        SupplementalListWidgetTitleBar.setSizePolicy(sizePolicy)
        SupplementalListWidgetTitleBar.setMinimumSize(QSize(256, 36))
        SupplementalListWidgetTitleBar.setMaximumSize(QSize(256, 36))
        SupplementalListWidgetTitleBar.setStyleSheet(u"/* Supplemental List */\n"
"\n"
"\n"
"background: rgba(255, 255, 255, 0.0001);\n"
"box-shadow: inset 0px 1px 0px rgba(0, 0, 0, 0.2);\n"
"\n"
"\n"
"background: #404040;")
        self.label_2 = QLabel(SupplementalListWidgetTitleBar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(28, 6, 113, 24))
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"font-family: Noto Sans TC;\n"
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
        self.pushButton_Add = QPushButton(SupplementalListWidgetTitleBar)
        self.pushButton_Add.setObjectName(u"pushButton_Add")
        self.pushButton_Add.setGeometry(QRect(206, 6, 24, 24))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_Add.sizePolicy().hasHeightForWidth())
        self.pushButton_Add.setSizePolicy(sizePolicy1)
        self.pushButton_Add.setMinimumSize(QSize(24, 24))
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(13)
        self.pushButton_Add.setFont(font)
        self.pushButton_Add.setStyleSheet(u"\n"
"color: rgba(255, 255, 255, 0.5);\n"
"background: rgba(255, 255, 255, 0.0001);\n"
"")
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/common-add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Add.setIcon(icon)
        self.pushButton_Add.setIconSize(QSize(24, 24))
        self.label_3 = QLabel(SupplementalListWidgetTitleBar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(7, 9, 18, 18))
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(18, 18))
        self.label_3.setMaximumSize(QSize(0, 0))
        self.label_3.setBaseSize(QSize(18, 18))
        self.label_3.setStyleSheet(u"/* icon/toc-resource */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 18px;\n"
"height: 18px;\n"
"left: 3px;\n"
"top: 3px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.label_3.setText(u"")
        self.label_3.setPixmap(QPixmap(u":/SVG/svg/icon/toc-resource.svg"))
        self.label_3.setScaledContents(True)

        self.retranslateUi(SupplementalListWidgetTitleBar)

        QMetaObject.connectSlotsByName(SupplementalListWidgetTitleBar)
    # setupUi

    def retranslateUi(self, SupplementalListWidgetTitleBar):
        SupplementalListWidgetTitleBar.setWindowTitle(QCoreApplication.translate("SupplementalListWidgetTitleBar", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("SupplementalListWidgetTitleBar", u"Supplemental List", None))
        self.pushButton_Add.setText("")
    # retranslateUi

