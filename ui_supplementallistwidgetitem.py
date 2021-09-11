# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SupplementalListWidgetItem.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_SupplementalListWidgetItem(object):
    def setupUi(self, SupplementalListWidgetItem):
        if not SupplementalListWidgetItem.objectName():
            SupplementalListWidgetItem.setObjectName(u"SupplementalListWidgetItem")
        SupplementalListWidgetItem.resize(240, 46)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SupplementalListWidgetItem.sizePolicy().hasHeightForWidth())
        SupplementalListWidgetItem.setSizePolicy(sizePolicy)
        SupplementalListWidgetItem.setMinimumSize(QSize(240, 46))
        SupplementalListWidgetItem.setMaximumSize(QSize(240, 46))
        font = QFont()
        font.setFamily(u"Noto Sans")
        SupplementalListWidgetItem.setFont(font)
        SupplementalListWidgetItem.setWindowTitle(u"Form")
        SupplementalListWidgetItem.setStyleSheet(u"background: #404040;\n"
"\n"
"margin: 0px 0px;\n"
"\n"
"QWidget::QFrame {\n"
"	border: 1px solid rgba(255, 255, 255, 0.1);\n"
"	box-sizing: border-box;\n"
"	border-radius: 8px; \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame = QFrame(SupplementalListWidgetItem)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(18, 0, 220, 40))
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(220, 40))
        self.frame.setMaximumSize(QSize(220, 40))
        self.frame.setStyleSheet(u"/*\n"
"display: flex;\n"
"flex-direction: row;\n"
"justify-content: center;\n"
"align-items: center;\n"
"*/\n"
"padding: 2px;\n"
"\n"
"background: rgba(255, 255, 255, 0.005);\n"
"border: 1px solid rgba(255, 255, 255, 0.1);\n"
"box-sizing: border-box;\n"
"border-radius: 8px;\n"
"\n"
"margin: 0px 0px;\n"
"\n"
"QFrame {\n"
"	background: #404040; \n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	background: #474747;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_Add = QPushButton(self.frame)
        self.pushButton_Add.setObjectName(u"pushButton_Add")
        self.pushButton_Add.setGeometry(QRect(154, 8, 24, 24))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_Add.sizePolicy().hasHeightForWidth())
        self.pushButton_Add.setSizePolicy(sizePolicy1)
        self.pushButton_Add.setMinimumSize(QSize(24, 24))
        self.pushButton_Add.setBaseSize(QSize(24, 24))
        font1 = QFont()
        font1.setFamily(u"Noto Sans")
        font1.setPointSize(13)
        self.pushButton_Add.setFont(font1)
        self.pushButton_Add.setStyleSheet(u"border: 0px;\n"
"background: #404040;\n"
"color: #FFFFFF;")
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/reading-order-add-to-list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Add.setIcon(icon)
        self.pushButton_Add.setIconSize(QSize(24, 24))
        self.label_Filetype = QLabel(self.frame)
        self.label_Filetype.setObjectName(u"label_Filetype")
        self.label_Filetype.setGeometry(QRect(6, 8, 24, 24))
        sizePolicy1.setHeightForWidth(self.label_Filetype.sizePolicy().hasHeightForWidth())
        self.label_Filetype.setSizePolicy(sizePolicy1)
        self.label_Filetype.setMinimumSize(QSize(24, 24))
        self.label_Filetype.setMaximumSize(QSize(0, 0))
        self.label_Filetype.setStyleSheet(u"/* icon/resource-image */\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"border: 0px;\n"
"\n"
"QFrame {\n"
"	background: #404040;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	background: #474747;\n"
"}\n"
"\n"
"")
        self.label_Filetype.setText(u"")
        self.label_Filetype.setPixmap(QPixmap(u":/SVG/svg/icon/resource-document.svg"))
        self.label_Filetype.setScaledContents(True)
        self.label_Filetype.setAlignment(Qt.AlignCenter)
        self.pushButton_Remove = QPushButton(self.frame)
        self.pushButton_Remove.setObjectName(u"pushButton_Remove")
        self.pushButton_Remove.setGeometry(QRect(190, 8, 24, 24))
        sizePolicy1.setHeightForWidth(self.pushButton_Remove.sizePolicy().hasHeightForWidth())
        self.pushButton_Remove.setSizePolicy(sizePolicy1)
        self.pushButton_Remove.setMinimumSize(QSize(24, 24))
        self.pushButton_Remove.setBaseSize(QSize(24, 24))
        self.pushButton_Remove.setFont(font1)
        self.pushButton_Remove.setStyleSheet(u"background: #404040;\n"
"border: 0px;\n"
"color: #FFFFFF;")
        self.pushButton_Remove.setText(u"")
        icon1 = QIcon()
        icon1.addFile(u":/SVG/svg/icon/common-remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Remove.setIcon(icon1)
        self.pushButton_Remove.setIconSize(QSize(24, 24))
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(36, 10, 112, 19))
        self.lineEdit.setMinimumSize(QSize(112, 19))
        self.lineEdit.setMaximumSize(QSize(16777215, 19))
        self.lineEdit.setStyleSheet(u"background: #404040;\n"
"border: 0px;\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 19px;\n"
"margin: 0px 0px;\n"
"border: 0px;\n"
"color: #FFFFFF;\n"
"background: #404040;\n"
"border-radius: 0px;\n"
"\n"
"")

        self.retranslateUi(SupplementalListWidgetItem)

        QMetaObject.connectSlotsByName(SupplementalListWidgetItem)
    # setupUi

    def retranslateUi(self, SupplementalListWidgetItem):
#if QT_CONFIG(tooltip)
        self.pushButton_Add.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_Add.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_Remove.setToolTip("")
#endif // QT_CONFIG(tooltip)
        pass
    # retranslateUi

