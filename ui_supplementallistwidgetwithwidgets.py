# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SupplementalListWidgetWithWidgets.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_SupplementalListWidgetWithWidgets(object):
    def setupUi(self, SupplementalListWidgetWithWidgets):
        if not SupplementalListWidgetWithWidgets.objectName():
            SupplementalListWidgetWithWidgets.setObjectName(u"SupplementalListWidgetWithWidgets")
        SupplementalListWidgetWithWidgets.resize(256, 325)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SupplementalListWidgetWithWidgets.sizePolicy().hasHeightForWidth())
        SupplementalListWidgetWithWidgets.setSizePolicy(sizePolicy)
        SupplementalListWidgetWithWidgets.setMinimumSize(QSize(256, 136))
        SupplementalListWidgetWithWidgets.setMaximumSize(QSize(256, 16777215))
        SupplementalListWidgetWithWidgets.setStyleSheet(u"/* panel/background */\n"
"\n"
"background: #404040;\n"
"box-shadow: inset 1px 0px 0px rgba(0, 0, 0, 0.25);\n"
"\n"
"")
        self.gridLayout = QGridLayout(SupplementalListWidgetWithWidgets)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(SupplementalListWidgetWithWidgets)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(256, 36))
        self.widget.setMaximumSize(QSize(256, 36))
        self.widget.setStyleSheet(u"background: rgba(255, 255, 255, 0.0001);\n"
"box-shadow: inset 0px 1px 0px rgba(0, 0, 0, 0.2);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(7, 9, 18, 18))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(18, 18))
        self.label_3.setBaseSize(QSize(18, 18))
        self.label_3.setStyleSheet(u"/* icon/resource-image */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 24px;\n"
"height: 24px;\n"
"left: calc(50% - 24px/2);\n"
"top: calc(50% - 24px/2);\n"
"\n"
"color: rgba(255, 255, 255, 0.5);\n"
"background: rgba(255, 255, 255, 0.0001);")
        self.label_3.setText(u"")
        self.label_3.setPixmap(QPixmap(u":/SVG/svg/icon/toc-resource.svg"))
        self.label_3.setScaledContents(True)
        self.label_3.setTextInteractionFlags(Qt.NoTextInteraction)
        self.pushButton_Add = QPushButton(self.widget)
        self.pushButton_Add.setObjectName(u"pushButton_Add")
        self.pushButton_Add.setGeometry(QRect(225, 6, 24, 24))
        sizePolicy2.setHeightForWidth(self.pushButton_Add.sizePolicy().hasHeightForWidth())
        self.pushButton_Add.setSizePolicy(sizePolicy2)
        self.pushButton_Add.setMinimumSize(QSize(24, 24))
        self.pushButton_Add.setMaximumSize(QSize(0, 0))
        self.pushButton_Add.setBaseSize(QSize(24, 24))
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(13)
        self.pushButton_Add.setFont(font)
        self.pushButton_Add.setStyleSheet(u"/* icon/reading-order-add-to-list */\n"
"\n"
"/*\n"
"color: rgba(255, 255, 255, 0.5);\n"
"background: rgba(255, 255, 255, 0.0001);\n"
"*/\n"
"\n"
"background: #404040;\n"
"border: 0px;\n"
"color: #FFFFFF;\n"
"")
        self.pushButton_Add.setText(u"")
        icon = QIcon()
        icon.addFile(u":/SVG/svg/icon/common-add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Add.setIcon(icon)
        self.pushButton_Add.setIconSize(QSize(24, 24))
        self.label_2 = QLabel(self.widget)
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
"color: rgba(255, 255, 255, 0.5);\n"
"background: rgba(255, 255, 255, 0.0001);\n"
"\n"
"")

        self.verticalLayout.addWidget(self.widget)

        self.label_NoItem = QLabel(SupplementalListWidgetWithWidgets)
        self.label_NoItem.setObjectName(u"label_NoItem")
        self.label_NoItem.setMinimumSize(QSize(208, 15))
        self.label_NoItem.setMaximumSize(QSize(208, 15))
        self.label_NoItem.setStyleSheet(u"font-family: Noto Sans TC;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 11px;\n"
"line-height: 15px;\n"
"/* identical to box height */\n"
"\n"
"color: rgba(255, 255, 255, 0.45);\n"
"background: rgba(255, 255, 255, 0.0001);")
        self.label_NoItem.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.label_NoItem)

        self.listWidget = QListWidget(SupplementalListWidgetWithWidgets)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QSize(256, 0))
        self.listWidget.setMaximumSize(QSize(256, 16777215))
        font1 = QFont()
        font1.setFamily(u"Noto Sans")
        self.listWidget.setFont(font1)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setStyleSheet(u"\n"
"border:0px;\n"
"\n"
"color: rgba(255, 255, 255, 0.5);\n"
"background: rgba(255, 255, 255, 0.0001);\n"
"\n"
"margin: 0px;\n"
"spacing: 0px;\n"
"\n"
"")
        self.listWidget.setFrameShape(QFrame.StyledPanel)
        self.listWidget.setLineWidth(0)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setAutoScrollMargin(0)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.listWidget.setDefaultDropAction(Qt.MoveAction)
        self.listWidget.setResizeMode(QListView.Fixed)
        self.listWidget.setSpacing(0)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setItemAlignment(Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.listWidget, 0, Qt.AlignHCenter)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(SupplementalListWidgetWithWidgets)

        QMetaObject.connectSlotsByName(SupplementalListWidgetWithWidgets)
    # setupUi

    def retranslateUi(self, SupplementalListWidgetWithWidgets):
        SupplementalListWidgetWithWidgets.setWindowTitle(QCoreApplication.translate("SupplementalListWidgetWithWidgets", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("SupplementalListWidgetWithWidgets", u"Supplemental List", None))
        self.label_NoItem.setText(QCoreApplication.translate("SupplementalListWidgetWithWidgets", u"     There is no supplemental item.", None))
    # retranslateUi

