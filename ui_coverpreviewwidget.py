# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CoverPreviewWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_CoverPreviewWidget(object):
    def setupUi(self, CoverPreviewWidget):
        if not CoverPreviewWidget.objectName():
            CoverPreviewWidget.setObjectName(u"CoverPreviewWidget")
        CoverPreviewWidget.resize(256, 216)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CoverPreviewWidget.sizePolicy().hasHeightForWidth())
        CoverPreviewWidget.setSizePolicy(sizePolicy)
        CoverPreviewWidget.setMinimumSize(QSize(256, 216))
        CoverPreviewWidget.setMaximumSize(QSize(256, 216))
        CoverPreviewWidget.setStyleSheet(u"/* cover preview */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 240px;\n"
"height: 216px;\n"
"left: 89px;\n"
"top: 127px;\n"
"\n"
"background: #404040;")
        self.label = QLabel(CoverPreviewWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(7, 9, 18, 18))
        self.label.setStyleSheet(u"/* icon/cover-icon */\n"
"\n"
"/*\n"
"position: absolute;\n"
"width: 18px;\n"
"height: 18px;\n"
"left: 3px;\n"
"top: 3px;\n"
"*/\n"
"background: rgba(255, 255, 255, 0.0001);\n"
"")
        self.label.setPixmap(QPixmap(u":/SVG/svg/icon/cover-icon.svg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(CoverPreviewWidget)
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
        self.label_Cover = QLabel(CoverPreviewWidget)
        self.label_Cover.setObjectName(u"label_Cover")
        self.label_Cover.setGeometry(QRect(68, 40, 120, 120))
        self.label_Cover.setMinimumSize(QSize(120, 120))
        font = QFont()
        font.setFamily(u"Noto Sans Adlam")
        font.setPointSize(13)
        self.label_Cover.setFont(font)
        self.label_Cover.setStyleSheet(u"/* Frame 53 */\n"
"\n"
"/*\n"
"position: absolute;\n"
"width: 120px;\n"
"height: 120px;\n"
"left: 149px;\n"
"top: 167px;\n"
"*/\n"
"background: rgba(255, 113, 224, 0.4);")
        self.label_Cover.setPixmap(QPixmap(u":/SVG/svg/icon/cover-preview-empty.svg"))
        self.label_Cover.setScaledContents(True)
        self.label_Cover.setTextInteractionFlags(Qt.NoTextInteraction)
        self.pushButton_AddCover = QPushButton(CoverPreviewWidget)
        self.pushButton_AddCover.setObjectName(u"pushButton_AddCover")
        self.pushButton_AddCover.setEnabled(True)
        self.pushButton_AddCover.setGeometry(QRect(85, 174, 87, 28))
        font1 = QFont()
        font1.setFamily(u"Noto Sans TC")
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.pushButton_AddCover.setFont(font1)
        self.pushButton_AddCover.setStyleSheet(u"/* common/button */\n"
"\n"
"/* button/border */\n"
"\n"
"border: 1px solid rgba(255, 255, 255, 0.4);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"\n"
"/* Browse */\n"
"\n"
"position: static;\n"
"width: 63px;\n"
"height: 18px;\n"
"left: 12px;\n"
"top: 5px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"/* button/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.9);\n"
"\n"
"")
        self.pushButton_AddCover.setCheckable(False)
        self.pushButton_AddCover.setFlat(False)
        self.pushButton_Remove = QPushButton(CoverPreviewWidget)
        self.buttonGroup_RemoveReplace = QButtonGroup(CoverPreviewWidget)
        self.buttonGroup_RemoveReplace.setObjectName(u"buttonGroup_RemoveReplace")
        self.buttonGroup_RemoveReplace.addButton(self.pushButton_Remove)
        self.pushButton_Remove.setObjectName(u"pushButton_Remove")
        self.pushButton_Remove.setEnabled(True)
        self.pushButton_Remove.setGeometry(QRect(51, 174, 74, 28))
        self.pushButton_Remove.setFont(font1)
        self.pushButton_Remove.setStyleSheet(u"display: flex;\n"
"flex-direction: row;\n"
"justify-content: center;\n"
"align-items: center;\n"
"padding: 4px 12px;\n"
"\n"
"position: absolute;\n"
"height: 28px;\n"
"left: 17.71%;\n"
"right: 51.46%;\n"
"top: 0px;\n"
"\n"
"/* button/border */\n"
"\n"
"border: 1px solid rgba(255, 255, 255, 0.4);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"\n"
"\n"
"/* Remove */\n"
"\n"
"\n"
"position: static;\n"
"width: 50px;\n"
"height: 18px;\n"
"left: 12px;\n"
"top: 5px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"/* button/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.9);\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;\n"
"\n"
"QToolTip {\n"
"	border:0px;\n"
"	background: #404040;\n"
"}")
        self.pushButton_Remove.setCheckable(False)
        self.pushButton_Remove.setFlat(False)
        self.pushButton_Replace = QPushButton(CoverPreviewWidget)
        self.buttonGroup_RemoveReplace.addButton(self.pushButton_Replace)
        self.pushButton_Replace.setObjectName(u"pushButton_Replace")
        self.pushButton_Replace.setEnabled(True)
        self.pushButton_Replace.setGeometry(QRect(133, 174, 72, 28))
        self.pushButton_Replace.setFont(font1)
        self.pushButton_Replace.setStyleSheet(u"display: flex;\n"
"flex-direction: row;\n"
"justify-content: center;\n"
"align-items: center;\n"
"padding: 4px 12px;\n"
"\n"
"position: absolute;\n"
"height: 28px;\n"
"left: 51.88%;\n"
"right: 18.12%;\n"
"top: 0px;\n"
"\n"
"/* button/border */\n"
"\n"
"border: 1px solid rgba(255, 255, 255, 0.4);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"\n"
"\n"
"/* Replace */\n"
"\n"
"\n"
"position: static;\n"
"width: 48px;\n"
"height: 18px;\n"
"left: 12px;\n"
"top: 5px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"/* button/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.9);\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;\n"
"\n"
"QToolTip {\n"
"	border:0px;\n"
"	background: #404040;\n"
"}")
        self.pushButton_Replace.setCheckable(False)
        self.pushButton_Replace.setFlat(False)
        self.pushButton_Replace.raise_()
        self.pushButton_Remove.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_Cover.raise_()
        self.pushButton_AddCover.raise_()

        self.retranslateUi(CoverPreviewWidget)

        QMetaObject.connectSlotsByName(CoverPreviewWidget)
    # setupUi

    def retranslateUi(self, CoverPreviewWidget):
        CoverPreviewWidget.setWindowTitle(QCoreApplication.translate("CoverPreviewWidget", u"Cover Preview Widget", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("CoverPreviewWidget", u"Cover Preview", None))
        self.label_Cover.setText("")
        self.pushButton_AddCover.setText(QCoreApplication.translate("CoverPreviewWidget", u"Add Cover", None))
        self.pushButton_Remove.setText(QCoreApplication.translate("CoverPreviewWidget", u"Remove", None))
        self.pushButton_Replace.setText(QCoreApplication.translate("CoverPreviewWidget", u"Replace", None))
    # retranslateUi

