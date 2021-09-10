# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateNewWizard.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_CreateNewWizard(object):
    def setupUi(self, CreateNewWizard):
        if not CreateNewWizard.objectName():
            CreateNewWizard.setObjectName(u"CreateNewWizard")
        CreateNewWizard.resize(382, 453)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateNewWizard.sizePolicy().hasHeightForWidth())
        CreateNewWizard.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/audiobook-editor-logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        CreateNewWizard.setWindowIcon(icon)
        CreateNewWizard.setAutoFillBackground(False)
        CreateNewWizard.setStyleSheet(u"/* starting panel */\n"
"\n"
"\n"
"position: relative;\n"
"width: 380px;\n"
"height: 446px;\n"
"\n"
"background: #333333;")
        self.label = QLabel(CreateNewWizard)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 380, 48))
        self.label.setPixmap(QPixmap(u":/SVG/svg/icon/create-project-banner.svg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(CreateNewWizard)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(24, 67, 332, 22))
        font = QFont()
        font.setFamily(u"Noto Sans TC")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label_2.setFont(font)
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.label_2.setStyleSheet(u"/*\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 16px;\n"
"line-height: 22px;\n"
"*/\n"
"\n"
"\n"
"\n"
"color: #FFFFFF;")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_3 = QLabel(CreateNewWizard)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(38, 111, 49, 20))
        font1 = QFont()
        font1.setFamily(u"Noto Sans TC")
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"position: static;\n"
"width: 49px;\n"
"height: 16px;\n"
"left: 2px;\n"
"top: calc(50% - 16px/2);\n"
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
        self.label_4 = QLabel(CreateNewWizard)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(38, 165, 56, 20))
        self.label_4.setStyleSheet(u"position: static;\n"
"width: 56px;\n"
"height: 16px;\n"
"left: 2px;\n"
"top: calc(50% - 16px/2);\n"
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
        self.label_5 = QLabel(CreateNewWizard)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(38, 221, 40, 16))
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
        self.label_6 = QLabel(CreateNewWizard)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(38, 275, 46, 16))
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
        self.label_7 = QLabel(CreateNewWizard)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(38, 329, 54, 16))
        self.label_7.setStyleSheet(u"position: static;\n"
"width: 54px;\n"
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
        self.lineEdit_BookPath = QLineEdit(CreateNewWizard)
        self.lineEdit_BookPath.setObjectName(u"lineEdit_BookPath")
        self.lineEdit_BookPath.setGeometry(QRect(36, 131, 226, 28))
        font2 = QFont()
        font2.setFamily(u"Noto Sans")
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.lineEdit_BookPath.setFont(font2)
        self.lineEdit_BookPath.setStyleSheet(u"/* Rectangle 8 */\n"
"\n"
"\n"
"position: absolute;\n"
"left: 0px;\n"
"right: 0px;\n"
"top: 0px;\n"
"bottom: 0px;\n"
"\n"
"/* cell/text input background */\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border: 1px solid rgba(0, 0, 0, 0.05);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"\n"
"/* Browse */\n"
"\n"
"\n"
"position: static;\n"
"width: 45px;\n"
"height: 18px;\n"
"left: 12px;\n"
"top: 5px;\n"
"\n"
"font-family: Noto Sans;\n"
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
"")
        self.lineEdit_BookPath.setReadOnly(True)
        self.lineEdit_BookTitle = QLineEdit(CreateNewWizard)
        self.lineEdit_BookTitle.setObjectName(u"lineEdit_BookTitle")
        self.lineEdit_BookTitle.setGeometry(QRect(36, 185, 308, 28))
        self.lineEdit_BookTitle.setStyleSheet(u"/* Rectangle 8 */\n"
"\n"
"\n"
"position: absolute;\n"
"left: 0px;\n"
"right: 0px;\n"
"top: 0px;\n"
"bottom: 0px;\n"
"\n"
"/* cell/text input background */\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border: 1px solid rgba(0, 0, 0, 0.05);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"\n"
"/* Browse */\n"
"\n"
"\n"
"position: static;\n"
"width: 45px;\n"
"height: 18px;\n"
"left: 12px;\n"
"top: 5px;\n"
"\n"
"font-family: Noto Sans;\n"
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
"")
        self.lineEdit_Author = QLineEdit(CreateNewWizard)
        self.lineEdit_Author.setObjectName(u"lineEdit_Author")
        self.lineEdit_Author.setGeometry(QRect(36, 239, 308, 28))
        self.lineEdit_Author.setStyleSheet(u"/* Rectangle 8 */\n"
"\n"
"\n"
"position: absolute;\n"
"left: 0px;\n"
"right: 0px;\n"
"top: 0px;\n"
"bottom: 0px;\n"
"\n"
"/* cell/text input background */\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border: 1px solid rgba(0, 0, 0, 0.05);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"\n"
"/* Browse */\n"
"\n"
"\n"
"position: static;\n"
"width: 45px;\n"
"height: 18px;\n"
"left: 12px;\n"
"top: 5px;\n"
"\n"
"font-family: Noto Sans;\n"
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
"")
        self.lineEdit_ReadBy = QLineEdit(CreateNewWizard)
        self.lineEdit_ReadBy.setObjectName(u"lineEdit_ReadBy")
        self.lineEdit_ReadBy.setGeometry(QRect(36, 293, 308, 28))
        self.lineEdit_ReadBy.setStyleSheet(u"/* Rectangle 8 */\n"
"\n"
"\n"
"position: absolute;\n"
"left: 0px;\n"
"right: 0px;\n"
"top: 0px;\n"
"bottom: 0px;\n"
"\n"
"/* cell/text input background */\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border: 1px solid rgba(0, 0, 0, 0.05);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"\n"
"/* Browse */\n"
"\n"
"\n"
"position: static;\n"
"width: 45px;\n"
"height: 18px;\n"
"left: 12px;\n"
"top: 5px;\n"
"\n"
"font-family: Noto Sans;\n"
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
"")
        self.lineEdit_Publisher = QLineEdit(CreateNewWizard)
        self.lineEdit_Publisher.setObjectName(u"lineEdit_Publisher")
        self.lineEdit_Publisher.setGeometry(QRect(36, 347, 308, 28))
        self.lineEdit_Publisher.setStyleSheet(u"/* Rectangle 8 */\n"
"\n"
"\n"
"position: absolute;\n"
"left: 0px;\n"
"right: 0px;\n"
"top: 0px;\n"
"bottom: 0px;\n"
"\n"
"/* cell/text input background */\n"
"\n"
"background: rgba(0, 0, 0, 0.2);\n"
"border: 1px solid rgba(0, 0, 0, 0.05);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"\n"
"/* Browse */\n"
"\n"
"\n"
"position: static;\n"
"width: 45px;\n"
"height: 18px;\n"
"left: 12px;\n"
"top: 5px;\n"
"\n"
"font-family: Noto Sans;\n"
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
"")
        self.pushButton_Create = QPushButton(CreateNewWizard)
        self.pushButton_Create.setObjectName(u"pushButton_Create")
        self.pushButton_Create.setGeometry(QRect(280, 398, 64, 28))
        self.pushButton_Create.setFont(font1)
        self.pushButton_Create.setStyleSheet(u"position: absolute;\n"
"width: 69px;\n"
"height: 28px;\n"
"left: 274px;\n"
"top: 23px;\n"
"\n"
"border: 1px solid rgba(255, 255, 255, 0.4);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"\n"
"/* Create */\n"
"\n"
"\n"
"position: static;\n"
"width: 40px;\n"
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
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;\n"
"")
        self.pushButton_Cancel = QPushButton(CreateNewWizard)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")
        self.pushButton_Cancel.setGeometry(QRect(207, 398, 65, 28))
        self.pushButton_Cancel.setFont(font1)
        self.pushButton_Cancel.setStyleSheet(u"position: absolute;\n"
"height: 28px;\n"
"left: 207px;\n"
"right: 108px;\n"
"top: 20px;\n"
"\n"
"border: 1px solid rgba(255, 255, 255, 0.4);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"\n"
"\n"
"\n"
"/* Cancel */\n"
"\n"
"\n"
"position: static;\n"
"width: 41px;\n"
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
"margin: 0px 0px;")
        self.pushButton_Browse = QPushButton(CreateNewWizard)
        self.pushButton_Browse.setObjectName(u"pushButton_Browse")
        self.pushButton_Browse.setGeometry(QRect(274, 131, 69, 28))
        self.pushButton_Browse.setFont(font1)
        self.pushButton_Browse.setStyleSheet(u"position: absolute;\n"
"width: 69px;\n"
"height: 28px;\n"
"left: 274px;\n"
"top: 23px;\n"
"\n"
"border: 1px solid rgba(255, 255, 255, 0.4);\n"
"box-sizing: border-box;\n"
"border-radius: 6px;\n"
"\n"
"/* Browse */\n"
"\n"
"\n"
"position: static;\n"
"width: 45px;\n"
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
"margin: 0px 0px;")
        self.label_9 = QLabel(CreateNewWizard)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(91, 111, 7, 20))
        font3 = QFont()
        font3.setFamily(u"Noto Sans")
        font3.setPointSize(12)
        self.label_9.setFont(font3)
        self.label_9.setPixmap(QPixmap(u":/SVG/svg/icon/common-text-field-required.svg"))
        self.label_9.setScaledContents(True)
        self.label_10 = QLabel(CreateNewWizard)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(98, 165, 7, 20))
        self.label_10.setPixmap(QPixmap(u":/SVG/svg/icon/common-text-field-required.svg"))
        self.label_10.setScaledContents(True)

        self.retranslateUi(CreateNewWizard)

        QMetaObject.connectSlotsByName(CreateNewWizard)
    # setupUi

    def retranslateUi(self, CreateNewWizard):
        CreateNewWizard.setWindowTitle(QCoreApplication.translate("CreateNewWizard", u"Create Wizard", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("CreateNewWizard", u"Create a new audiobook", None))
        self.label_3.setText(QCoreApplication.translate("CreateNewWizard", u"File Path", None))
        self.label_4.setText(QCoreApplication.translate("CreateNewWizard", u"Book Title", None))
        self.label_5.setText(QCoreApplication.translate("CreateNewWizard", u"Author", None))
        self.label_6.setText(QCoreApplication.translate("CreateNewWizard", u"Read By", None))
        self.label_7.setText(QCoreApplication.translate("CreateNewWizard", u"Publisher", None))
        self.lineEdit_BookPath.setText("")
        self.lineEdit_BookTitle.setText("")
        self.pushButton_Create.setText(QCoreApplication.translate("CreateNewWizard", u"Create", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("CreateNewWizard", u"Cancel", None))
        self.pushButton_Browse.setText(QCoreApplication.translate("CreateNewWizard", u"Browse", None))
        self.label_9.setText("")
        self.label_10.setText("")
    # retranslateUi

