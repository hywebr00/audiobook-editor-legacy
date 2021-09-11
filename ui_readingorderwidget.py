# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReadingOrderWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_ReadingOrderWidget(object):
    def setupUi(self, ReadingOrderWidget):
        if not ReadingOrderWidget.objectName():
            ReadingOrderWidget.setObjectName(u"ReadingOrderWidget")
        ReadingOrderWidget.resize(436, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ReadingOrderWidget.sizePolicy().hasHeightForWidth())
        ReadingOrderWidget.setSizePolicy(sizePolicy)
        ReadingOrderWidget.setMinimumSize(QSize(436, 0))
        ReadingOrderWidget.setMaximumSize(QSize(436, 16777215))
        ReadingOrderWidget.setStyleSheet(u"background: #333333;\n"
"box-shadow: inset 1px 0px 0px rgba(0, 0, 0, 0.25);")
        self.gridLayout = QGridLayout(ReadingOrderWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(ReadingOrderWidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(420, 40))
        self.widget.setMaximumSize(QSize(420, 40))
        self.widget.setStyleSheet(u"background: #333333;\n"
"/* background: rgba(255, 255, 255, 0.0001); */\n"
"box-shadow: inset 0px 1px 0px rgba(0, 0, 0, 0.2);\n"
"")
        self.pushButton_Add = QPushButton(self.widget)
        self.pushButton_Add.setObjectName(u"pushButton_Add")
        self.pushButton_Add.setGeometry(QRect(380, 0, 40, 40))
        sizePolicy1.setHeightForWidth(self.pushButton_Add.sizePolicy().hasHeightForWidth())
        self.pushButton_Add.setSizePolicy(sizePolicy1)
        self.pushButton_Add.setMinimumSize(QSize(40, 40))
        self.pushButton_Add.setBaseSize(QSize(40, 40))
        self.pushButton_Add.setStyleSheet(u"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"line-height: 20px;\n"
"\n"
"/*\n"
"position: absolute;\n"
"width: 24px;\n"
"height: 24px;\n"
"left: calc(50% - 24px/2);\n"
"top: calc(50% - 24px/2);\n"
"*/\n"
"\n"
"color: rgba(255, 255, 255, 1);\n"
"/* \n"
"background: rgba(255, 255, 255, 0.0001); \n"
"*/\n"
"\n"
"\n"
"background: #333333;\n"
"border: 0px;\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/*\n"
"QToolTip {\n"
"	color: rgba(255, 0, 0, 1);\n"
"	background: rgba(255, 255, 0, 1);\n"
"}\n"
"*/\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/common-add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Add.setIcon(icon)
        self.pushButton_Add.setIconSize(QSize(24, 24))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(166, 5, 160, 26))
        font = QFont()
        font.setFamily(u"Noto Sans TC")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgba(255, 255, 255, 0.5);\n"
"background: rgba(255, 255, 255, 0.0001);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(144, 11, 18, 18))
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"background: rgba(255, 255, 255, 0.0001);")
        self.label.setPixmap(QPixmap(u":/SVG/svg/icon/reading-order-icon.svg"))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.widget)

        self.widget_Board = QWidget(ReadingOrderWidget)
        self.widget_Board.setObjectName(u"widget_Board")
        sizePolicy1.setHeightForWidth(self.widget_Board.sizePolicy().hasHeightForWidth())
        self.widget_Board.setSizePolicy(sizePolicy1)
        self.widget_Board.setMinimumSize(QSize(420, 350))
        self.widget_Board.setMaximumSize(QSize(420, 350))
        self.widget_Board.setAutoFillBackground(False)
        self.widget_Board.setStyleSheet(u"")
        self.label_NoItem = QLabel(self.widget_Board)
        self.label_NoItem.setObjectName(u"label_NoItem")
        self.label_NoItem.setGeometry(QRect(161, 14, 360, 20))
        sizePolicy1.setHeightForWidth(self.label_NoItem.sizePolicy().hasHeightForWidth())
        self.label_NoItem.setSizePolicy(sizePolicy1)
        self.label_NoItem.setMinimumSize(QSize(360, 20))
        self.label_NoItem.setMaximumSize(QSize(360, 20))
        font1 = QFont()
        font1.setFamily(u"Noto Sans TC")
        font1.setBold(False)
        font1.setItalic(True)
        font1.setWeight(50)
        self.label_NoItem.setFont(font1)
        self.label_NoItem.setStyleSheet(u"position: absolute;\n"
"width: 197px;\n"
"height: 18px;\n"
"left: 161px;\n"
"top: 13.89px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: italic;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: right;\n"
"\n"
"/* icon/primary */\n"
"\n"
"color: #5AB0FF;")
        self.label_NoItem.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.widget_Usage = QWidget(self.widget_Board)
        self.widget_Usage.setObjectName(u"widget_Usage")
        self.widget_Usage.setEnabled(True)
        self.widget_Usage.setGeometry(QRect(1, 183, 415, 146))
        sizePolicy1.setHeightForWidth(self.widget_Usage.sizePolicy().hasHeightForWidth())
        self.widget_Usage.setSizePolicy(sizePolicy1)
        self.widget_Usage.setMinimumSize(QSize(415, 146))
        self.widget_Usage.setMaximumSize(QSize(415, 146))
        self.widget_Usage.setStyleSheet(u"/* Group 27 */\n"
"\n"
"/*\n"
"position: absolute;\n"
"width: 243.01px;\n"
"height: 132.25px;\n"
"left: 144px;\n"
"top: 153px;\n"
"*/")
        self.label_4 = QLabel(self.widget_Usage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(115, 0, 415, 20))
        font2 = QFont()
        font2.setFamily(u"Noto Sans TC")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"/*\n"
"position: absolute;\n"
"width: 178px;\n"
"height: 20px;\n"
"left: calc(50% - 178px/2 - 6px);\n"
"top: calc(50% - 20px/2 - 56px);\n"
"*/\n"
"\n"
"/*\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 15px;\n"
"line-height: 20px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"*/\n"
"\n"
"color: rgba(255, 255, 255, 0.9);\n"
"opacity: 0.8;")
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_5 = QLabel(self.widget_Usage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(104, 42, 300, 18))
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(300, 18))
        font3 = QFont()
        font3.setFamily(u"Noto Sans TC")
        font3.setPointSize(13)
        font3.setItalic(False)
        font3.setKerning(True)
        self.label_5.setFont(font3)
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.label_5.setStyleSheet(u"/*\n"
"position: absolute;\n"
"width: 221px;\n"
"height: 18px;\n"
"left: calc(50% - 221px/2 + 4.5px);\n"
"top: calc(50% - 18px/2 - 14.75px);\n"
"*/\n"
"/*\n"
"font-family: Noto Sans TC;\n"
"font-style: italic;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"*/\n"
"/* identical to box height */\n"
"\n"
"/*\n"
"display: flex;\n"
"align-items: center;\n"
"*/\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.5);")
        self.label_5.setLineWidth(0)
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_6 = QLabel(self.widget_Usage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(104, 78, 300, 18))
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(300, 18))
        self.label_6.setFont(font3)
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.label_6.setStyleSheet(u"/* Preview and validate */\n"
"\n"
"/*\n"
"position: absolute;\n"
"width: 119px;\n"
"height: 18px;\n"
"left: calc(50% - 119px/2 - 46.5px);\n"
"top: calc(50% - 18px/2 + 21.25px);\n"
"\n"
"font-family: Noto Sans;\n"
"font-style: italic;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"*/\n"
"/* identical to box height */\n"
"/*\n"
"display: flex;\n"
"align-items: center;\n"
"*/\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.5);")
        self.label_7 = QLabel(self.widget_Usage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(104, 111, 300, 22))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMinimumSize(QSize(300, 22))
        self.label_7.setMaximumSize(QSize(16777215, 22))
        self.label_7.setBaseSize(QSize(0, 0))
        self.label_7.setFont(font3)
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.label_7.setStyleSheet(u"/* Preview and validate */\n"
"\n"
"/*\n"
"position: absolute;\n"
"width: 119px;\n"
"height: 18px;\n"
"left: calc(50% - 119px/2 - 46.5px);\n"
"top: calc(50% - 18px/2 + 21.25px);\n"
"\n"
"font-family: Noto Sans;\n"
"font-style: italic;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 18px;\n"
"*/\n"
"/* identical to box height */\n"
"/*\n"
"display: flex;\n"
"align-items: center;\n"
"*/\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.5);")
        self.label_7.setLineWidth(1)
        self.label_8 = QLabel(self.widget_Usage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(82, 48, 6, 6))
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setStyleSheet(u"/* Ellipse 38 */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 6px;\n"
"height: 6px;\n"
"left: calc(50% - 6px/2 - 125px);\n"
"top: calc(50% - 6px/2 - 14.75px);\n"
"\n"
"background: #999999;\n"
"\n"
"border-radius: 3px;")
        self.label_8.setText(u"")
        self.label_9 = QLabel(self.widget_Usage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(84, 60, 2, 2))
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setStyleSheet(u"/* Ellipse 38 */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 6px;\n"
"height: 6px;\n"
"left: calc(50% - 6px/2 - 125px);\n"
"top: calc(50% - 6px/2 - 14.75px);\n"
"\n"
"background: #999999;\n"
"\n"
"border-radius: 1px;")
        self.label_9.setText(u"")
        self.label_10 = QLabel(self.widget_Usage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(84, 68, 2, 2))
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setStyleSheet(u"/* Ellipse 38 */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 6px;\n"
"height: 6px;\n"
"left: calc(50% - 6px/2 - 125px);\n"
"top: calc(50% - 6px/2 - 14.75px);\n"
"\n"
"background: #999999;\n"
"\n"
"border-radius: 1px;")
        self.label_10.setText(u"")
        self.label_12 = QLabel(self.widget_Usage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(84, 76, 2, 2))
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setStyleSheet(u"/* Ellipse 38 */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 6px;\n"
"height: 6px;\n"
"left: calc(50% - 6px/2 - 125px);\n"
"top: calc(50% - 6px/2 - 14.75px);\n"
"\n"
"background: #999999;\n"
"\n"
"border-radius: 1px;")
        self.label_12.setText(u"")
        self.label_13 = QLabel(self.widget_Usage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(82, 84, 6, 6))
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setStyleSheet(u"/* Ellipse 38 */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 6px;\n"
"height: 6px;\n"
"left: calc(50% - 6px/2 - 125px);\n"
"top: calc(50% - 6px/2 - 14.75px);\n"
"\n"
"background: #999999;\n"
"\n"
"border-radius: 3px;")
        self.label_13.setText(u"")
        self.label_14 = QLabel(self.widget_Usage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(82, 120, 6, 6))
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setStyleSheet(u"/* Ellipse 38 */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 6px;\n"
"height: 6px;\n"
"left: calc(50% - 6px/2 - 125px);\n"
"top: calc(50% - 6px/2 - 14.75px);\n"
"\n"
"background: #999999;\n"
"\n"
"border-radius: 3px;")
        self.label_14.setText(u"")
        self.label_15 = QLabel(self.widget_Usage)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(84, 96, 2, 2))
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setStyleSheet(u"/* Ellipse 38 */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 6px;\n"
"height: 6px;\n"
"left: calc(50% - 6px/2 - 125px);\n"
"top: calc(50% - 6px/2 - 14.75px);\n"
"\n"
"background: #999999;\n"
"\n"
"border-radius: 1px;")
        self.label_15.setText(u"")
        self.label_16 = QLabel(self.widget_Usage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(84, 104, 2, 2))
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setStyleSheet(u"/* Ellipse 38 */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 6px;\n"
"height: 6px;\n"
"left: calc(50% - 6px/2 - 125px);\n"
"top: calc(50% - 6px/2 - 14.75px);\n"
"\n"
"background: #999999;\n"
"\n"
"border-radius: 1px;")
        self.label_16.setText(u"")
        self.label_17 = QLabel(self.widget_Usage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(84, 112, 2, 2))
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setStyleSheet(u"/* Ellipse 38 */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 6px;\n"
"height: 6px;\n"
"left: calc(50% - 6px/2 - 125px);\n"
"top: calc(50% - 6px/2 - 14.75px);\n"
"\n"
"background: #999999;\n"
"\n"
"border-radius: 1px;")
        self.label_17.setText(u"")
        self.label_Arrow = QLabel(self.widget_Board)
        self.label_Arrow.setObjectName(u"label_Arrow")
        self.label_Arrow.setGeometry(QRect(370, 0, 50, 50))
        sizePolicy1.setHeightForWidth(self.label_Arrow.sizePolicy().hasHeightForWidth())
        self.label_Arrow.setSizePolicy(sizePolicy1)
        self.label_Arrow.setMinimumSize(QSize(50, 50))
        self.label_Arrow.setMaximumSize(QSize(50, 50))
        self.label_Arrow.setBaseSize(QSize(50, 50))
        font4 = QFont()
        font4.setFamily(u"Noto Sans")
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setItalic(True)
        font4.setWeight(50)
        self.label_Arrow.setFont(font4)
        self.label_Arrow.setStyleSheet(u"")
        self.label_Arrow.setText(u"")
        self.label_Arrow.setPixmap(QPixmap(u":/SVG/svg/icon/ftu-add-reading-order-arrow.svg"))
        self.label_Arrow.setScaledContents(True)
        self.label_Arrow.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.widget_Board)

        self.label_Book = QLabel(ReadingOrderWidget)
        self.label_Book.setObjectName(u"label_Book")
        self.label_Book.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.label_Book.sizePolicy().hasHeightForWidth())
        self.label_Book.setSizePolicy(sizePolicy1)
        self.label_Book.setMinimumSize(QSize(420, 200))
        self.label_Book.setMaximumSize(QSize(420, 200))
        self.label_Book.setBaseSize(QSize(0, 0))
        self.label_Book.setFont(font4)
        self.label_Book.setStyleSheet(u"/* Start by adding an audio file here. */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 197px;\n"
"height: 18px;\n"
"\n"
"\n"
"font-style: italic;\n"
"font-weight: normal;\n"
"\n"
"\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: right;\n"
"\n"
"/* icon/primary */\n"
"\n"
"color: #5AB0FF;")
        self.label_Book.setText(u"")
        self.label_Book.setPixmap(QPixmap(u":/SVG/svg/icon/ftu-background-pattern.svg"))
        self.label_Book.setScaledContents(True)
        self.label_Book.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_Book.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.label_Book)

        self.listWidget = QListWidget(ReadingOrderWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QSize(420, 0))
        self.listWidget.setMaximumSize(QSize(420, 16777215))
        self.listWidget.setAcceptDrops(False)
#if QT_CONFIG(tooltip)
        self.listWidget.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet(u"/*\n"
"QListWidget {\n"
"	border: 0px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"	background: #333333;\n"
"}\n"
"*/\n"
"\n"
"border:0px;\n"
"\n"
"color: rgba(255, 255, 255, 0.5);\n"
"background: rgba(255, 255, 255, 0.0001);\n"
"\n"
"margin: 0px;\n"
"spacing: 0px;\n"
"/*\n"
"QListWidget::item:hover,\n"
"QListWidget::item:disabled:hover,\n"
"QListWidget::item:hover:!active,\n"
"{background: #333333;}\n"
"*/")
        self.listWidget.setLineWidth(0)
        self.listWidget.setMidLineWidth(0)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setAutoScrollMargin(0)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setDragDropOverwriteMode(False)
        self.listWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.listWidget.setDefaultDropAction(Qt.MoveAction)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget.setMovement(QListView.Free)
        self.listWidget.setSpacing(0)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.listWidget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(ReadingOrderWidget)

        QMetaObject.connectSlotsByName(ReadingOrderWidget)
    # setupUi

    def retranslateUi(self, ReadingOrderWidget):
        ReadingOrderWidget.setWindowTitle(QCoreApplication.translate("ReadingOrderWidget", u"Form", None))
        self.pushButton_Add.setText("")
        self.label_2.setText(QCoreApplication.translate("ReadingOrderWidget", u"Reading Order", None))
        self.label.setText("")
        self.label_NoItem.setText(QCoreApplication.translate("ReadingOrderWidget", u"Start by adding an audio file here.", None))
        self.label_4.setText(QCoreApplication.translate("ReadingOrderWidget", u"Let's create an audiobook!", None))
        self.label_5.setText(QCoreApplication.translate("ReadingOrderWidget", u"Add audio files and edit the metadata. ", None))
        self.label_6.setText(QCoreApplication.translate("ReadingOrderWidget", u"Preview and validate ", None))
        self.label_7.setText(QCoreApplication.translate("ReadingOrderWidget", u"Pack! And get a unique audiobook!", None))
    # retranslateUi

