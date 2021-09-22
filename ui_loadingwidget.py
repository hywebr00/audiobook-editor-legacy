# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoadingWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_LoadingWidget(object):
    def setupUi(self, LoadingWidget):
        if not LoadingWidget.objectName():
            LoadingWidget.setObjectName(u"LoadingWidget")
        LoadingWidget.resize(640, 480)
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/AudiobookEditorLogo@16.svg", QSize(), QIcon.Normal, QIcon.Off)
        LoadingWidget.setWindowIcon(icon)
        LoadingWidget.setStyleSheet(u"/* loading */\n"
"\n"
"\n"
"position: relative;\n"
"width: 640px;\n"
"height: 480px;\n"
"\n"
"background: #333333;")
        self.label = QLabel(LoadingWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 640, 80))
        self.label.setPixmap(QPixmap(u":/SVG/svg/icon/loading-banner.svg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(LoadingWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(48, 193, 544, 38))
        font = QFont()
        font.setFamily(u"Noto Sans TC")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"position: static;\n"
"width: 544px;\n"
"height: 38px;\n"
"left: 48px;\n"
"top: 13px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal; \n"
"font-weight: bold;\n"
"font-size: 28px;\n"
"line-height: 38px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 1;\n"
"margin: 0px 0px;")
        self.label_3 = QLabel(LoadingWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(48, 252, 472, 16))
        font1 = QFont()
        font1.setFamily(u"Noto Sans TC")
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(37)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"/* https://github.com/dpublishing/audiobooks-samples/blob/main/case1/publication.json */\n"
"\n"
"\n"
"position: static;\n"
"width: 472px;\n"
"height: 16px;\n"
"left: 48px;\n"
"top: 8px;\n"
"\n"
"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: 300;\n"
"font-size: 12px;\n"
"line-height: 16px;\n"
"\n"
"color: #69ADFD;\n"
"\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.label_4 = QLabel(LoadingWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(259, 445, 122, 18))
        font2 = QFont()
        font2.setFamily(u"Noto Sans TC")
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"position: static;\n"
"width: 122px;\n"
"height: 18px;\n"
"left: 259px;\n"
"top: 17px;\n"
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
"color: rgba(255, 255, 255, 0.4);\n"
"\n"
"\n"
"/* Inside Auto Layout */\n"
"\n"
"flex: none;\n"
"order: 0;\n"
"flex-grow: 0;\n"
"margin: 0px 0px;")
        self.progressBar = QProgressBar(LoadingWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 290, 485, 8))
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)
        self.label_Progress = QLabel(LoadingWidget)
        self.label_Progress.setObjectName(u"label_Progress")
        self.label_Progress.setGeometry(QRect(547, 287, 24, 14))
        font3 = QFont()
        font3.setFamily(u"Helvetica")
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(37)
        self.label_Progress.setFont(font3)
        self.label_Progress.setStyleSheet(u"position: absolute;\n"
"width: 24px;\n"
"height: 14px;\n"
"left: 0px;\n"
"top: calc(50% - 14px/2);\n"
"\n"
"font-family: Helvetica;\n"
"font-style: normal;\n"
"font-weight: 300;\n"
"font-size: 12px;\n"
"line-height: 14px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;")

        self.retranslateUi(LoadingWidget)

        QMetaObject.connectSlotsByName(LoadingWidget)
    # setupUi

    def retranslateUi(self, LoadingWidget):
        LoadingWidget.setWindowTitle(QCoreApplication.translate("LoadingWidget", u"Audiobook Editor", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("LoadingWidget", u"Audiobook Editor", None))
        self.label_3.setText(QCoreApplication.translate("LoadingWidget", u"Loading......", None))
        self.label_4.setText(QCoreApplication.translate("LoadingWidget", u"Powered by HyRead", None))
        self.label_Progress.setText(QCoreApplication.translate("LoadingWidget", u"24%", None))
    # retranslateUi

