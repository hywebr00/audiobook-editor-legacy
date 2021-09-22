# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MetadataWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MetadataWidget(object):
    def setupUi(self, MetadataWidget):
        if not MetadataWidget.objectName():
            MetadataWidget.setObjectName(u"MetadataWidget")
        MetadataWidget.resize(256, 460)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MetadataWidget.sizePolicy().hasHeightForWidth())
        MetadataWidget.setSizePolicy(sizePolicy)
        MetadataWidget.setMinimumSize(QSize(256, 460))
        MetadataWidget.setMaximumSize(QSize(256, 460))
        MetadataWidget.setStyleSheet(u"/* left panel */\n"
"\n"
"/*\n"
"position: absolute;\n"
"width: 240px;\n"
"height: 492px;\n"
"left: 360px;\n"
"*/\n"
"/*top: calc(50% - 492px/2);*/\n"
"top: 0px;\n"
"\n"
"/* panel/background */\n"
"\n"
"background: #404040;\n"
"box-shadow: inset -1px 0px 1px rgba(0, 0, 0, 0.25);\n"
"\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    outline: none;\n"
"}")
        self.lineEdit_BookTitle = QLineEdit(MetadataWidget)
        self.lineEdit_BookTitle.setObjectName(u"lineEdit_BookTitle")
        self.lineEdit_BookTitle.setGeometry(QRect(18, 27, 220, 28))
        font = QFont()
        font.setFamily(u"Noto Sans TC")
        font.setPointSize(14)
        self.lineEdit_BookTitle.setFont(font)
        self.lineEdit_BookTitle.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: rgba(0, 0, 0, 0.2);\n"
"	border: 1px solid rgba(0, 0, 0, 0.05);\n"
"	box-sizing: border-box;\n"
"	border-radius: 6px;\n"
"	color: #FFFFFF;\n"
"/*\n"
"	font-size: 14px;\n"
"	line-height: 19px;\n"
"*/\n"
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
        self.lineEdit_BookTitle.setReadOnly(False)
        self.label_4 = QLabel(MetadataWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 7, 56, 16))
        self.label_4.setStyleSheet(u"position: static;\n"
"width: 56px;\n"
"height: 20px;\n"
"left: 2px;\n"
"top: calc(50% - 20px/2);\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.7);\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"align-self: stretch;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.label_10 = QLabel(MetadataWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(80, 8, 7, 18))
        self.label_10.setPixmap(QPixmap(u":/SVG/svg/icon/common-text-field-required.svg"))
        self.label_10.setScaledContents(True)
        self.lineEdit_Author = QLineEdit(MetadataWidget)
        self.lineEdit_Author.setObjectName(u"lineEdit_Author")
        self.lineEdit_Author.setGeometry(QRect(18, 85, 220, 28))
        self.lineEdit_Author.setFont(font)
        self.lineEdit_Author.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: rgba(0, 0, 0, 0.2);\n"
"	border: 1px solid rgba(0, 0, 0, 0.05);\n"
"	box-sizing: border-box;\n"
"	border-radius: 6px;\n"
"	color: #FFFFFF;\n"
"/*\n"
"	font-size: 14px;\n"
"	line-height: 19px;\n"
"*/\n"
"}\n"
"\n"
"QLineEdit:disabled\n"
"{\n"
"	border: 3px solid rgba(255, 0, 0, 1);\n"
"	background: rgba(0, 0, 0, 0.2);\n"
"	box-sizing: border-box;\n"
"	border-radius: 6px;\n"
"	color: #FFFFFF;\n"
"\n"
"}")
        self.label_5 = QLabel(MetadataWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 67, 40, 16))
        self.label_5.setStyleSheet(u"position: static;\n"
"width: 40px;\n"
"left: 2px;\n"
"top: 2px;\n"
"bottom: 2px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.7);\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.label = QLabel(MetadataWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 114, 198, 15))
        font1 = QFont()
        font1.setFamily(u"Noto Sans TC")
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"/* Tip: Sepatate authers with a comma. */\n"
"\n"
"\n"
"position: static;\n"
"width: 198px;\n"
"height: 15px;\n"
"left: 2px;\n"
"top: calc(50% - 15px/2);\n"
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
"\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.label_6 = QLabel(MetadataWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 140, 46, 16))
        self.label_6.setStyleSheet(u"position: static;\n"
"width: 46px;\n"
"left: 2px;\n"
"top: 2px;\n"
"bottom: 2px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.7);\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.lineEdit_ReadBy = QLineEdit(MetadataWidget)
        self.lineEdit_ReadBy.setObjectName(u"lineEdit_ReadBy")
        self.lineEdit_ReadBy.setGeometry(QRect(18, 158, 220, 28))
        self.lineEdit_ReadBy.setFont(font)
        self.lineEdit_ReadBy.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background: rgba(0, 0, 0, 0.2);\n"
"	border: 1px solid rgba(0, 0, 0, 0.05);\n"
"	box-sizing: border-box;\n"
"	border-radius: 6px;\n"
"	color: #FFFFFF;\n"
"/*\n"
"	font-size: 14px;\n"
"	line-height: 19px;\n"
"*/\n"
"}\n"
"\n"
"QLineEdit:disabled\n"
"{\n"
"	border: 3px solid rgba(255, 0, 0, 1);\n"
"	background: rgba(0, 0, 0, 0.2);\n"
"	box-sizing: border-box;\n"
"	border-radius: 6px;\n"
"	color: #FFFFFF;\n"
"\n"
"}")
        self.label_11 = QLabel(MetadataWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(64, 66, 7, 18))
        self.label_11.setPixmap(QPixmap(u":/SVG/svg/icon/common-text-field-required.svg"))
        self.label_11.setScaledContents(True)
        self.label_12 = QLabel(MetadataWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 139, 7, 18))
        self.label_12.setPixmap(QPixmap(u":/SVG/svg/icon/common-text-field-required.svg"))
        self.label_12.setScaledContents(True)
        self.label_2 = QLabel(MetadataWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 187, 198, 15))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"/* Tip: Sepatate authers with a comma. */\n"
"\n"
"\n"
"position: static;\n"
"width: 198px;\n"
"height: 15px;\n"
"left: 2px;\n"
"top: calc(50% - 15px/2);\n"
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
"\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.lineEdit_Publisher = QLineEdit(MetadataWidget)
        self.lineEdit_Publisher.setObjectName(u"lineEdit_Publisher")
        self.lineEdit_Publisher.setGeometry(QRect(18, 231, 220, 28))
        self.lineEdit_Publisher.setFont(font)
        self.lineEdit_Publisher.setStyleSheet(u"height: 19px;\n"
"left: 8px;\n"
"\n"
"/* cell/text input background */\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border: 1px solid rgba(0, 0, 0, 0.05);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"/*\n"
"font-size: 14px;\n"
"line-height: 19px;\n"
"*/\n"
"/* cell/text */\n"
"\n"
"color: #FFFFFF;")
        self.label_7 = QLabel(MetadataWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 213, 54, 16))
        self.label_7.setStyleSheet(u"position: static;\n"
"width: 46px;\n"
"left: 2px;\n"
"top: 2px;\n"
"bottom: 2px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.7);\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.label_8 = QLabel(MetadataWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 271, 46, 16))
        self.label_8.setStyleSheet(u"position: static;\n"
"width: 46px;\n"
"left: 2px;\n"
"top: 2px;\n"
"bottom: 2px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.7);\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.lineEdit_Website = QLineEdit(MetadataWidget)
        self.lineEdit_Website.setObjectName(u"lineEdit_Website")
        self.lineEdit_Website.setGeometry(QRect(18, 289, 220, 28))
        self.lineEdit_Website.setFont(font)
        self.lineEdit_Website.setStyleSheet(u"height: 19px;\n"
"left: 8px;\n"
"\n"
"/* cell/text input background */\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border: 1px solid rgba(0, 0, 0, 0.05);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"/*\n"
"font-size: 14px;\n"
"line-height: 19px;\n"
"*/\n"
"/* cell/text */\n"
"\n"
"color: #FFFFFF;")
        self.label_9 = QLabel(MetadataWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 327, 50, 20))
        self.label_9.setStyleSheet(u"position: static;\n"
"width: 46px;\n"
"left: 2px;\n"
"top: 2px;\n"
"bottom: 2px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.7);\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.label_13 = QLabel(MetadataWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(132, 327, 57, 20))
        self.label_13.setStyleSheet(u"position: static;\n"
"width: 46px;\n"
"left: 2px;\n"
"top: 2px;\n"
"bottom: 2px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.7);\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.label_Duration = QLabel(MetadataWidget)
        self.label_Duration.setObjectName(u"label_Duration")
        self.label_Duration.setGeometry(QRect(20, 349, 104, 22))
        font2 = QFont()
        font2.setFamily(u"Noto Sans")
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.label_Duration.setFont(font2)
        self.label_Duration.setStyleSheet(u"color: #FFFFFF;\n"
"\n"
"left: 8px;\n"
"top: 5px;\n"
"\n"
"/*font-size: 15px;*/\n"
"line-height: 20px;")
        self.label_Duration.setText(u"00:00:00")
        self.label_Duration.setTextInteractionFlags(Qt.NoTextInteraction)
        self.comboBox_inLanguage = QComboBox(MetadataWidget)
        self.comboBox_inLanguage.addItem("")
        self.comboBox_inLanguage.addItem("")
        self.comboBox_inLanguage.addItem("")
        self.comboBox_inLanguage.addItem("")
        self.comboBox_inLanguage.addItem("")
        self.comboBox_inLanguage.addItem("")
        self.comboBox_inLanguage.addItem("")
        self.comboBox_inLanguage.addItem("")
        self.comboBox_inLanguage.addItem("")
        self.comboBox_inLanguage.addItem("")
        self.comboBox_inLanguage.setObjectName(u"comboBox_inLanguage")
        self.comboBox_inLanguage.setGeometry(QRect(134, 347, 104, 28))
        font3 = QFont()
        font3.setFamily(u"Noto Sans")
        font3.setPointSize(14)
        self.comboBox_inLanguage.setFont(font3)
        self.comboBox_inLanguage.setStyleSheet(u"/* cell/text input background */\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border-radius: 6px;\n"
"\n"
"/* cell/text */\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"left: 8px;\n"
"top: 5px;\n"
"\n"
"/*font-size: 14px;*/\n"
"line-height: 19px;\n"
"\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    outline: none;\n"
"}\n"
"\n"
" QComboBox::drop-down {subcontrol-origin: padding;  subcontrol-position: top right;;border: 0px ;}\n"
"\n"
"\n"
"")
        self.comboBox_inLanguage.setCurrentText(u"zh-TW")
        self.comboBox_inLanguage.setMaxVisibleItems(12)
        self.comboBox_inLanguage.setInsertPolicy(QComboBox.InsertAtBottom)
        self.comboBox_inLanguage.setIconSize(QSize(0, 0))
        self.comboBox_inLanguage.setFrame(False)
        self.label_14 = QLabel(MetadataWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 388, 86, 16))
        self.label_14.setStyleSheet(u"position: static;\n"
"width: 46px;\n"
"left: 2px;\n"
"top: 2px;\n"
"bottom: 2px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.7);\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.dateEdit_DatePublished = QDateEdit(MetadataWidget)
        self.dateEdit_DatePublished.setObjectName(u"dateEdit_DatePublished")
        self.dateEdit_DatePublished.setGeometry(QRect(18, 406, 104, 28))
        sizePolicy.setHeightForWidth(self.dateEdit_DatePublished.sizePolicy().hasHeightForWidth())
        self.dateEdit_DatePublished.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamily(u"Noto Sans")
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.dateEdit_DatePublished.setFont(font4)
        self.dateEdit_DatePublished.setStyleSheet(u"/* cell/text input background */\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border-radius: 6px;\n"
"\n"
"/* cell/text */\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"left: 8px;\n"
"top: 5px;\n"
"\n"
"font-size: 14px;\n"
"line-height: 19px;\n"
"")
        self.dateEdit_DatePublished.setDateTime(QDateTime(QDate(2021, 1, 1), QTime(0, 0, 0)))
        self.dateEdit_DatePublished.setDisplayFormat(u"yyyy-MM-dd")
        self.dateEdit_DatePublished.setCalendarPopup(True)
        self.dateEdit_DatePublished.setTimeSpec(Qt.LocalTime)
        self.dateEdit_DatePublished.setDate(QDate(2021, 1, 1))
        self.label_16 = QLabel(MetadataWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(132, 388, 80, 16))
        self.label_16.setStyleSheet(u"position: static;\n"
"width: 46px;\n"
"left: 2px;\n"
"top: 2px;\n"
"bottom: 2px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.7);\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.dateEdit_DateModified = QDateEdit(MetadataWidget)
        self.dateEdit_DateModified.setObjectName(u"dateEdit_DateModified")
        self.dateEdit_DateModified.setGeometry(QRect(134, 406, 104, 28))
        sizePolicy.setHeightForWidth(self.dateEdit_DateModified.sizePolicy().hasHeightForWidth())
        self.dateEdit_DateModified.setSizePolicy(sizePolicy)
        self.dateEdit_DateModified.setFont(font4)
        self.dateEdit_DateModified.setStyleSheet(u"/* cell/text input background */\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border-radius: 6px;\n"
"\n"
"/* cell/text */\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"\n"
"left: 8px;\n"
"top: 5px;\n"
"\n"
"font-size: 14px;\n"
"line-height: 19px;\n"
"\n"
"")
        self.dateEdit_DateModified.setDateTime(QDateTime(QDate(2021, 1, 1), QTime(0, 0, 0)))
        self.dateEdit_DateModified.setCalendarPopup(True)
        self.dateEdit_DateModified.setDate(QDate(2021, 1, 1))
        self.line = QFrame(MetadataWidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(18, 0, 220, 1))
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setStyleSheet(u"background: #333333;")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.retranslateUi(MetadataWidget)

        QMetaObject.connectSlotsByName(MetadataWidget)
    # setupUi

    def retranslateUi(self, MetadataWidget):
        MetadataWidget.setWindowTitle(QCoreApplication.translate("MetadataWidget", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("MetadataWidget", u"Book Title", None))
        self.label_10.setText("")
        self.label_5.setText(QCoreApplication.translate("MetadataWidget", u"Author", None))
        self.label.setText(QCoreApplication.translate("MetadataWidget", u"Sepatate the authers with a comma.", None))
        self.label_6.setText(QCoreApplication.translate("MetadataWidget", u"Read By", None))
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_2.setText(QCoreApplication.translate("MetadataWidget", u"Sepatate the authers with a comma.", None))
        self.label_7.setText(QCoreApplication.translate("MetadataWidget", u"Publisher", None))
        self.label_8.setText(QCoreApplication.translate("MetadataWidget", u"Website", None))
        self.label_9.setText(QCoreApplication.translate("MetadataWidget", u"Duration", None))
        self.label_13.setText(QCoreApplication.translate("MetadataWidget", u"Language", None))
        self.comboBox_inLanguage.setItemText(0, QCoreApplication.translate("MetadataWidget", u"zh-TW", None))
        self.comboBox_inLanguage.setItemText(1, QCoreApplication.translate("MetadataWidget", u"zh-CN", None))
        self.comboBox_inLanguage.setItemText(2, QCoreApplication.translate("MetadataWidget", u"da-DK", None))
        self.comboBox_inLanguage.setItemText(3, QCoreApplication.translate("MetadataWidget", u"en-GB", None))
        self.comboBox_inLanguage.setItemText(4, QCoreApplication.translate("MetadataWidget", u"en-US", None))
        self.comboBox_inLanguage.setItemText(5, QCoreApplication.translate("MetadataWidget", u"es-ES", None))
        self.comboBox_inLanguage.setItemText(6, QCoreApplication.translate("MetadataWidget", u"fr-CA", None))
        self.comboBox_inLanguage.setItemText(7, QCoreApplication.translate("MetadataWidget", u"fr-FR", None))
        self.comboBox_inLanguage.setItemText(8, QCoreApplication.translate("MetadataWidget", u"ja-JP", None))
        self.comboBox_inLanguage.setItemText(9, QCoreApplication.translate("MetadataWidget", u"ko-KR", None))

        self.label_14.setText(QCoreApplication.translate("MetadataWidget", u"Date Published", None))
        self.label_16.setText(QCoreApplication.translate("MetadataWidget", u"Date Modified", None))
        self.dateEdit_DateModified.setDisplayFormat(QCoreApplication.translate("MetadataWidget", u"yyyy-MM-dd", None))
    # retranslateUi

