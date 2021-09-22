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
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(7, 18))
        self.label_11.setMaximumSize(QSize(7, 18))
        self.label_11.setPixmap(QPixmap(u":/SVG/svg/icon/common-text-field-required.svg"))
        self.label_11.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_11, 3, 1, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMinimumSize(QSize(7, 18))
        self.label_12.setMaximumSize(QSize(7, 18))
        self.label_12.setPixmap(QPixmap(u":/SVG/svg/icon/common-text-field-required.svg"))
        self.label_12.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_12, 6, 2, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMinimumSize(QSize(7, 18))
        self.label_10.setMaximumSize(QSize(7, 18))
        self.label_10.setPixmap(QPixmap(u":/SVG/svg/icon/common-text-field-required.svg"))
        self.label_10.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_10, 1, 3, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMinimumSize(QSize(0, 16))
        self.label_6.setMaximumSize(QSize(16777215, 16))
        font = QFont()
        font.setFamily(u"Noto Sans TC")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"/*\n"
"position: static;\n"
"width: 46px;\n"
"left: 2px;\n"
"top: 2px;\n"
"bottom: 2px;\n"
"*/\n"
"/*\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"*/\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.7);\n"
"\n"
"/* Inside Auto Layout */\n"
"/*\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;\n"
"*/")

        self.gridLayout_2.addWidget(self.label_6, 6, 0, 1, 2)

        self.dateEdit_DatePublished = QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_DatePublished.setObjectName(u"dateEdit_DatePublished")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.dateEdit_DatePublished.sizePolicy().hasHeightForWidth())
        self.dateEdit_DatePublished.setSizePolicy(sizePolicy4)
        self.dateEdit_DatePublished.setMinimumSize(QSize(0, 28))
        self.dateEdit_DatePublished.setMaximumSize(QSize(16777215, 28))
        font1 = QFont()
        font1.setFamily(u"Noto Sans")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.dateEdit_DatePublished.setFont(font1)
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

        self.gridLayout_2.addWidget(self.dateEdit_DatePublished, 16, 0, 1, 4)

        self.lineEdit_Publisher = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_Publisher.setObjectName(u"lineEdit_Publisher")
        sizePolicy2.setHeightForWidth(self.lineEdit_Publisher.sizePolicy().hasHeightForWidth())
        self.lineEdit_Publisher.setSizePolicy(sizePolicy2)
        self.lineEdit_Publisher.setMinimumSize(QSize(220, 28))
        self.lineEdit_Publisher.setMaximumSize(QSize(220, 28))
        font2 = QFont()
        font2.setFamily(u"Noto Sans TC")
        font2.setPointSize(14)
        self.lineEdit_Publisher.setFont(font2)
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

        self.gridLayout_2.addWidget(self.lineEdit_Publisher, 10, 0, 1, 5)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMinimumSize(QSize(0, 16))
        self.label_4.setMaximumSize(QSize(16777215, 16))
        self.label_4.setFont(font)
#if QT_CONFIG(whatsthis)
        self.label_4.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.label_4.setStyleSheet(u"/*\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"display: flex;\n"
"align-items: center;\n"
"*/\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.7);\n"
"\n"
"/* Inside Auto Layout */\n"
"/*\n"
"flex: none;\n"
"order: 0;\n"
"align-self: stretch;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;\n"
"*/")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 3)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(198, 15))
        self.label_2.setMaximumSize(QSize(198, 15))
        font3 = QFont()
        font3.setFamily(u"Noto Sans TC")
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.label_2.setFont(font3)
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

        self.gridLayout_2.addWidget(self.label_2, 8, 0, 1, 5)

        self.lineEdit_Website = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_Website.setObjectName(u"lineEdit_Website")
        sizePolicy2.setHeightForWidth(self.lineEdit_Website.sizePolicy().hasHeightForWidth())
        self.lineEdit_Website.setSizePolicy(sizePolicy2)
        self.lineEdit_Website.setMinimumSize(QSize(220, 28))
        self.lineEdit_Website.setMaximumSize(QSize(220, 28))
        self.lineEdit_Website.setFont(font2)
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

        self.gridLayout_2.addWidget(self.lineEdit_Website, 12, 0, 1, 5)

        self.dateEdit_DateModified = QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_DateModified.setObjectName(u"dateEdit_DateModified")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.dateEdit_DateModified.sizePolicy().hasHeightForWidth())
        self.dateEdit_DateModified.setSizePolicy(sizePolicy5)
        self.dateEdit_DateModified.setMinimumSize(QSize(0, 28))
        self.dateEdit_DateModified.setMaximumSize(QSize(16777215, 28))
        self.dateEdit_DateModified.setFont(font1)
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

        self.gridLayout_2.addWidget(self.dateEdit_DateModified, 16, 4, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(198, 15))
        self.label.setMaximumSize(QSize(198, 15))
        self.label.setFont(font3)
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

        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 5)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setStyleSheet(u"background: #333333;")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line, 0, 0, 1, 5)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setMinimumSize(QSize(0, 16))
        self.label_14.setMaximumSize(QSize(16777215, 16))
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

        self.gridLayout_2.addWidget(self.label_14, 15, 0, 1, 4)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setMinimumSize(QSize(0, 16))
        self.label_16.setMaximumSize(QSize(16777215, 16))
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

        self.gridLayout_2.addWidget(self.label_16, 15, 4, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMinimumSize(QSize(0, 16))
        self.label_5.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamily(u"Noto Sans TC")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.label_5.setFont(font4)
        self.label_5.setMouseTracking(False)
        self.label_5.setStyleSheet(u"/*\n"
"position: static;\n"
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
"*/\n"
"/* cell/label */\n"
"\n"
"color: rgba(255, 255, 255, 0.7);\n"
"\n"
"/* Inside Auto Layout */\n"
"/*\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;\n"
"*/")
        self.label_5.setTextFormat(Qt.PlainText)

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_Duration = QLabel(self.scrollAreaWidgetContents)
        self.label_Duration.setObjectName(u"label_Duration")
        sizePolicy5.setHeightForWidth(self.label_Duration.sizePolicy().hasHeightForWidth())
        self.label_Duration.setSizePolicy(sizePolicy5)
        self.label_Duration.setMinimumSize(QSize(0, 22))
        self.label_Duration.setMaximumSize(QSize(16777215, 22))
        font5 = QFont()
        font5.setFamily(u"Noto Sans")
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.label_Duration.setFont(font5)
        self.label_Duration.setStyleSheet(u"color: #FFFFFF;\n"
"\n"
"left: 8px;\n"
"top: 5px;\n"
"\n"
"/*font-size: 15px;*/\n"
"line-height: 20px;")
        self.label_Duration.setText(u"00:00:00")
        self.label_Duration.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_2.addWidget(self.label_Duration, 14, 0, 1, 4)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setMinimumSize(QSize(0, 16))
        self.label_8.setMaximumSize(QSize(16777215, 16))
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

        self.gridLayout_2.addWidget(self.label_8, 11, 0, 1, 2)

        self.lineEdit_BookTitle = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_BookTitle.setObjectName(u"lineEdit_BookTitle")
        sizePolicy2.setHeightForWidth(self.lineEdit_BookTitle.sizePolicy().hasHeightForWidth())
        self.lineEdit_BookTitle.setSizePolicy(sizePolicy2)
        self.lineEdit_BookTitle.setMinimumSize(QSize(220, 28))
        self.lineEdit_BookTitle.setMaximumSize(QSize(220, 28))
        self.lineEdit_BookTitle.setFont(font2)
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

        self.gridLayout_2.addWidget(self.lineEdit_BookTitle, 2, 0, 1, 5)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMinimumSize(QSize(0, 16))
        self.label_9.setMaximumSize(QSize(16777215, 16))
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

        self.gridLayout_2.addWidget(self.label_9, 13, 0, 1, 2)

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
        sizePolicy5.setHeightForWidth(self.comboBox_inLanguage.sizePolicy().hasHeightForWidth())
        self.comboBox_inLanguage.setSizePolicy(sizePolicy5)
        self.comboBox_inLanguage.setMinimumSize(QSize(0, 28))
        self.comboBox_inLanguage.setMaximumSize(QSize(16777215, 28))
        font6 = QFont()
        font6.setFamily(u"Noto Sans")
        font6.setPointSize(14)
        self.comboBox_inLanguage.setFont(font6)
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

        self.gridLayout_2.addWidget(self.comboBox_inLanguage, 14, 4, 1, 1)

        self.lineEdit_ReadBy = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_ReadBy.setObjectName(u"lineEdit_ReadBy")
        sizePolicy2.setHeightForWidth(self.lineEdit_ReadBy.sizePolicy().hasHeightForWidth())
        self.lineEdit_ReadBy.setSizePolicy(sizePolicy2)
        self.lineEdit_ReadBy.setMinimumSize(QSize(220, 28))
        self.lineEdit_ReadBy.setMaximumSize(QSize(220, 28))
        self.lineEdit_ReadBy.setFont(font2)
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

        self.gridLayout_2.addWidget(self.lineEdit_ReadBy, 7, 0, 1, 5)

        self.lineEdit_Author = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_Author.setObjectName(u"lineEdit_Author")
        sizePolicy2.setHeightForWidth(self.lineEdit_Author.sizePolicy().hasHeightForWidth())
        self.lineEdit_Author.setSizePolicy(sizePolicy2)
        self.lineEdit_Author.setMinimumSize(QSize(220, 28))
        self.lineEdit_Author.setMaximumSize(QSize(220, 28))
        self.lineEdit_Author.setFont(font2)
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

        self.gridLayout_2.addWidget(self.lineEdit_Author, 4, 0, 1, 5)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMinimumSize(QSize(0, 16))
        self.label_7.setMaximumSize(QSize(16777215, 16))
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

        self.gridLayout_2.addWidget(self.label_7, 9, 0, 1, 3)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setMinimumSize(QSize(0, 16))
        self.label_13.setMaximumSize(QSize(16777215, 16))
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

        self.gridLayout_2.addWidget(self.label_13, 13, 4, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(MetadataWidget)

        QMetaObject.connectSlotsByName(MetadataWidget)
    # setupUi

    def retranslateUi(self, MetadataWidget):
        MetadataWidget.setWindowTitle(QCoreApplication.translate("MetadataWidget", u"Form", None))
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_10.setText("")
        self.label_6.setText(QCoreApplication.translate("MetadataWidget", u"Read By", None))
        self.label_4.setText(QCoreApplication.translate("MetadataWidget", u"Book Title", None))
        self.label_2.setText(QCoreApplication.translate("MetadataWidget", u"Sepatate the authers with a comma.", None))
        self.dateEdit_DateModified.setDisplayFormat(QCoreApplication.translate("MetadataWidget", u"yyyy-MM-dd", None))
        self.label.setText(QCoreApplication.translate("MetadataWidget", u"Sepatate the authers with a comma.", None))
        self.label_14.setText(QCoreApplication.translate("MetadataWidget", u"Date Published", None))
        self.label_16.setText(QCoreApplication.translate("MetadataWidget", u"Date Modified", None))
        self.label_5.setText(QCoreApplication.translate("MetadataWidget", u"Author", None))
        self.label_8.setText(QCoreApplication.translate("MetadataWidget", u"Website", None))
        self.label_9.setText(QCoreApplication.translate("MetadataWidget", u"Duration", None))
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
        self.label_13.setText(QCoreApplication.translate("MetadataWidget", u"Language", None))
    # retranslateUi

