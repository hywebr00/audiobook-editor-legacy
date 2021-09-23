# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MetadataWidgetWithScrollArea.ui'
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
        MetadataWidget.resize(256, 526)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MetadataWidget.sizePolicy().hasHeightForWidth())
        MetadataWidget.setSizePolicy(sizePolicy)
        MetadataWidget.setMinimumSize(QSize(256, 0))
        MetadataWidget.setMaximumSize(QSize(256, 526))
        MetadataWidget.setStyleSheet(u"\n"
"top: 0px;\n"
"\n"
"background: #404040;\n"
"box-shadow: inset -1px 0px 1px rgba(0, 0, 0, 0.25);\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    outline: none;\n"
"}")
        self.gridLayout = QGridLayout(MetadataWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(MetadataWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(256, 0))
        self.scrollArea.setMaximumSize(QSize(256, 16777215))
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 254, 524))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(254, 0))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(254, 16777215))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(6, 0, 0, 10)
        self.dateEdit_DatePublished = QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_DatePublished.setObjectName(u"dateEdit_DatePublished")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dateEdit_DatePublished.sizePolicy().hasHeightForWidth())
        self.dateEdit_DatePublished.setSizePolicy(sizePolicy2)
        self.dateEdit_DatePublished.setMinimumSize(QSize(110, 28))
        self.dateEdit_DatePublished.setMaximumSize(QSize(110, 28))
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateEdit_DatePublished.setFont(font)
        self.dateEdit_DatePublished.setStyleSheet(u"/* cell/text input background */\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border-radius: 6px;\n"
"\n"
"/* cell/text */\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        self.dateEdit_DatePublished.setDateTime(QDateTime(QDate(2021, 1, 1), QTime(0, 0, 0)))
        self.dateEdit_DatePublished.setDisplayFormat(u"yyyy-MM-dd")
        self.dateEdit_DatePublished.setCalendarPopup(True)
        self.dateEdit_DatePublished.setTimeSpec(Qt.LocalTime)
        self.dateEdit_DatePublished.setDate(QDate(2021, 1, 1))

        self.gridLayout_2.addWidget(self.dateEdit_DatePublished, 17, 0, 1, 4)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(220, 15))
        self.label.setMaximumSize(QSize(220, 15))
        font1 = QFont()
        font1.setFamily(u"Noto Sans TC")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgba(255, 255, 255, 0.7);\n"
"")

        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 6)

        self.label_Duration = QLabel(self.scrollAreaWidgetContents)
        self.label_Duration.setObjectName(u"label_Duration")
        sizePolicy2.setHeightForWidth(self.label_Duration.sizePolicy().hasHeightForWidth())
        self.label_Duration.setSizePolicy(sizePolicy2)
        self.label_Duration.setMinimumSize(QSize(110, 22))
        self.label_Duration.setMaximumSize(QSize(110, 22))
        font2 = QFont()
        font2.setFamily(u"Noto Sans")
        font2.setPointSize(14)
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

        self.gridLayout_2.addWidget(self.label_Duration, 15, 0, 1, 4)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMinimumSize(QSize(110, 16))
        self.label_9.setMaximumSize(QSize(110, 16))
        font3 = QFont()
        font3.setFamily(u"Noto Sans TC")
        font3.setPointSize(12)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color: rgba(255, 255, 255, 0.7);\n"
"")

        self.gridLayout_2.addWidget(self.label_9, 14, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 15, 6, 1, 1)

        self.lineEdit_Publisher = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_Publisher.setObjectName(u"lineEdit_Publisher")
        sizePolicy2.setHeightForWidth(self.lineEdit_Publisher.sizePolicy().hasHeightForWidth())
        self.lineEdit_Publisher.setSizePolicy(sizePolicy2)
        self.lineEdit_Publisher.setMinimumSize(QSize(220, 28))
        self.lineEdit_Publisher.setMaximumSize(QSize(220, 28))
        font4 = QFont()
        font4.setFamily(u"Noto Sans TC")
        font4.setPointSize(14)
        self.lineEdit_Publisher.setFont(font4)
        self.lineEdit_Publisher.setAcceptDrops(False)
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

        self.gridLayout_2.addWidget(self.lineEdit_Publisher, 11, 0, 1, 6)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setStyleSheet(u"background: #333333;")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line, 0, 0, 1, 6)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 17, 6, 1, 1)

        self.dateEdit_DateModified = QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_DateModified.setObjectName(u"dateEdit_DateModified")
        sizePolicy2.setHeightForWidth(self.dateEdit_DateModified.sizePolicy().hasHeightForWidth())
        self.dateEdit_DateModified.setSizePolicy(sizePolicy2)
        self.dateEdit_DateModified.setMinimumSize(QSize(110, 28))
        self.dateEdit_DateModified.setMaximumSize(QSize(110, 28))
        self.dateEdit_DateModified.setFont(font)
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
"")
        self.dateEdit_DateModified.setDateTime(QDateTime(QDate(2021, 1, 1), QTime(0, 0, 0)))
        self.dateEdit_DateModified.setCalendarPopup(True)
        self.dateEdit_DateModified.setDate(QDate(2021, 1, 1))

        self.gridLayout_2.addWidget(self.dateEdit_DateModified, 17, 5, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setMinimumSize(QSize(110, 16))
        self.label_16.setMaximumSize(QSize(110, 16))
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"color: rgba(255, 255, 255, 0.7);\n"
"")

        self.gridLayout_2.addWidget(self.label_16, 16, 5, 1, 1)

        self.comboBox_inLanguage = QComboBox(self.scrollAreaWidgetContents)
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
        sizePolicy2.setHeightForWidth(self.comboBox_inLanguage.sizePolicy().hasHeightForWidth())
        self.comboBox_inLanguage.setSizePolicy(sizePolicy2)
        self.comboBox_inLanguage.setMinimumSize(QSize(110, 28))
        self.comboBox_inLanguage.setMaximumSize(QSize(110, 28))
        font5 = QFont()
        font5.setFamily(u"Noto Sans")
        font5.setPointSize(14)
        self.comboBox_inLanguage.setFont(font5)
        self.comboBox_inLanguage.setStyleSheet(u"/* cell/text input background */\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border-radius: 6px;\n"
"\n"
"/* cell/text */\n"
"\n"
"color: #FFFFFF;\n"
"\n"
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

        self.gridLayout_2.addWidget(self.comboBox_inLanguage, 15, 5, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMinimumSize(QSize(0, 16))
        self.label_7.setMaximumSize(QSize(16777215, 16))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgba(255, 255, 255, 0.7);\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.label_7, 10, 0, 1, 3)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(130, 16))
        self.frame_2.setMaximumSize(QSize(130, 16))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 0, 55, 18))
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setMinimumSize(QSize(0, 18))
        self.label_11.setMaximumSize(QSize(115, 18))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color: rgba(255, 255, 255, 0.7);\n"
"")
        self.label_11.setTextFormat(Qt.PlainText)
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(60, 0, 7, 18))
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setMinimumSize(QSize(7, 18))
        self.label_18.setMaximumSize(QSize(7, 18))
        self.label_18.setPixmap(QPixmap(u":/SVG/svg/icon/common-text-field-required.svg"))
        self.label_18.setScaledContents(True)

        self.gridLayout_2.addWidget(self.frame_2, 7, 0, 1, 1)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(130, 16))
        self.frame.setMaximumSize(QSize(130, 16))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 0, 45, 18))
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)
        self.label_15.setMinimumSize(QSize(0, 18))
        self.label_15.setMaximumSize(QSize(115, 18))
        font6 = QFont()
        font6.setFamily(u"Noto Sans TC")
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.label_15.setFont(font6)
        self.label_15.setMouseTracking(False)
        self.label_15.setStyleSheet(u"color: rgba(255, 255, 255, 0.7);\n"
"")
        self.label_15.setTextFormat(Qt.PlainText)
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 0, 7, 18))
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)
        self.label_17.setMinimumSize(QSize(7, 18))
        self.label_17.setMaximumSize(QSize(7, 18))
        self.label_17.setPixmap(QPixmap(u":/SVG/svg/icon/common-text-field-required.svg"))
        self.label_17.setScaledContents(True)

        self.gridLayout_2.addWidget(self.frame, 3, 0, 1, 1)

        self.lineEdit_Website = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_Website.setObjectName(u"lineEdit_Website")
        sizePolicy2.setHeightForWidth(self.lineEdit_Website.sizePolicy().hasHeightForWidth())
        self.lineEdit_Website.setSizePolicy(sizePolicy2)
        self.lineEdit_Website.setMinimumSize(QSize(220, 28))
        self.lineEdit_Website.setMaximumSize(QSize(220, 28))
        self.lineEdit_Website.setFont(font4)
        self.lineEdit_Website.setAcceptDrops(False)
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

        self.gridLayout_2.addWidget(self.lineEdit_Website, 13, 0, 1, 6)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setMinimumSize(QSize(0, 16))
        self.label_8.setMaximumSize(QSize(16777215, 16))
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"color: rgba(255, 255, 255, 0.7);\n"
"")

        self.gridLayout_2.addWidget(self.label_8, 12, 0, 1, 2)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setMinimumSize(QSize(110, 16))
        self.label_13.setMaximumSize(QSize(115, 16))
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"color: rgba(255, 255, 255, 0.7);\n"
"")

        self.gridLayout_2.addWidget(self.label_13, 14, 5, 1, 1)

        self.lineEdit_BookTitle = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_BookTitle.setObjectName(u"lineEdit_BookTitle")
        sizePolicy2.setHeightForWidth(self.lineEdit_BookTitle.sizePolicy().hasHeightForWidth())
        self.lineEdit_BookTitle.setSizePolicy(sizePolicy2)
        self.lineEdit_BookTitle.setMinimumSize(QSize(220, 28))
        self.lineEdit_BookTitle.setMaximumSize(QSize(220, 28))
        self.lineEdit_BookTitle.setFont(font4)
        self.lineEdit_BookTitle.setAcceptDrops(False)
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

        self.gridLayout_2.addWidget(self.lineEdit_BookTitle, 2, 0, 1, 6)

        self.lineEdit_ReadBy = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_ReadBy.setObjectName(u"lineEdit_ReadBy")
        sizePolicy2.setHeightForWidth(self.lineEdit_ReadBy.sizePolicy().hasHeightForWidth())
        self.lineEdit_ReadBy.setSizePolicy(sizePolicy2)
        self.lineEdit_ReadBy.setMinimumSize(QSize(220, 28))
        self.lineEdit_ReadBy.setMaximumSize(QSize(220, 28))
        self.lineEdit_ReadBy.setFont(font4)
        self.lineEdit_ReadBy.setAcceptDrops(False)
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

        self.gridLayout_2.addWidget(self.lineEdit_ReadBy, 8, 0, 1, 6)

        self.lineEdit_Author = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_Author.setObjectName(u"lineEdit_Author")
        sizePolicy2.setHeightForWidth(self.lineEdit_Author.sizePolicy().hasHeightForWidth())
        self.lineEdit_Author.setSizePolicy(sizePolicy2)
        self.lineEdit_Author.setMinimumSize(QSize(220, 28))
        self.lineEdit_Author.setMaximumSize(QSize(220, 28))
        self.lineEdit_Author.setFont(font4)
        self.lineEdit_Author.setAcceptDrops(False)
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

        self.gridLayout_2.addWidget(self.lineEdit_Author, 4, 0, 1, 6)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(220, 15))
        self.label_2.setMaximumSize(QSize(220, 15))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgba(255, 255, 255, 0.7);\n"
"")

        self.gridLayout_2.addWidget(self.label_2, 9, 0, 1, 6)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setMinimumSize(QSize(110, 16))
        self.label_14.setMaximumSize(QSize(110, 16))
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"color: rgba(255, 255, 255, 0.7);\n"
"")

        self.gridLayout_2.addWidget(self.label_14, 16, 0, 1, 4)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setMinimumSize(QSize(130, 16))
        self.frame_3.setMaximumSize(QSize(130, 16))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 0, 7, 18))
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMinimumSize(QSize(7, 18))
        self.label_12.setMaximumSize(QSize(7, 18))
        self.label_12.setPixmap(QPixmap(u":/SVG/svg/icon/common-text-field-required.svg"))
        self.label_12.setScaledContents(True)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 65, 18))
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMinimumSize(QSize(0, 18))
        self.label_5.setMaximumSize(QSize(115, 18))
        self.label_5.setFont(font3)
#if QT_CONFIG(whatsthis)
        self.label_5.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.label_5.setStyleSheet(u"color: rgba(255, 255, 255, 0.7);\n"
"\n"
"")
        self.label_5.setTextFormat(Qt.PlainText)

        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(MetadataWidget)

        QMetaObject.connectSlotsByName(MetadataWidget)
    # setupUi

    def retranslateUi(self, MetadataWidget):
        MetadataWidget.setWindowTitle(QCoreApplication.translate("MetadataWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("MetadataWidget", u"Sepatate the authers with a comma.", None))
        self.label_9.setText(QCoreApplication.translate("MetadataWidget", u"Duration", None))
        self.dateEdit_DateModified.setDisplayFormat(QCoreApplication.translate("MetadataWidget", u"yyyy-MM-dd", None))
        self.label_16.setText(QCoreApplication.translate("MetadataWidget", u"Date Modified", None))
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

        self.label_7.setText(QCoreApplication.translate("MetadataWidget", u"Publisher", None))
        self.label_11.setText(QCoreApplication.translate("MetadataWidget", u"Read By", None))
        self.label_18.setText("")
        self.label_15.setText(QCoreApplication.translate("MetadataWidget", u"Author", None))
        self.label_17.setText("")
        self.label_8.setText(QCoreApplication.translate("MetadataWidget", u"Website", None))
        self.label_13.setText(QCoreApplication.translate("MetadataWidget", u"Language", None))
        self.label_2.setText(QCoreApplication.translate("MetadataWidget", u"Sepatate the authers with a comma.", None))
        self.label_14.setText(QCoreApplication.translate("MetadataWidget", u"Date Published", None))
        self.label_12.setText("")
        self.label_5.setText(QCoreApplication.translate("MetadataWidget", u"Book Title", None))
    # retranslateUi

