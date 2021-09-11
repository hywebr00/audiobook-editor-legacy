# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:42:41 2021
"""

import logging
# import os
# import shutil
import mimetypes
from multipledispatch import dispatch

from PySide2.QtCore import *
# from PySide2.QtGui import *
from PySide2.QtWidgets import *

from book import Audiobook
from ui_supplementallistwidgetwithwidgets import Ui_SupplementalListWidgetWithWidgets
from supplementallistwidgetitem import SupplementalListWidgetItem
# from attachfromwidget import AttachFromWidget
from attachfromwidgetwithouturl import AttachFromWidgetWithoutURL
from alert import Alert, AlertWithButtons
from translucent import MaskWidget
# import resources_rc


class SupplementalListWidgetWithWidgets(QWidget):
    signal_Add_Resource_to_TOC = Signal(str, str)
    signal_Duration_Changed = Signal(float)

    str_LastOpenedDirectory = None

    @dispatch(QMainWindow)
    def __init__(self, mainWindow=None, width=240, height=46):
        super(SupplementalListWidgetWithWidgets, self).__init__()

        self.mainWindow = mainWindow
        self._itemWidth = width
        self._itemHeight = height
        self.ui = Ui_SupplementalListWidgetWithWidgets()
        self.ui.setupUi(self)
        self.ui.listWidget.setEnabled(False)

        self.ui.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self._isEmpty = True
        self._listWidgetItemSerialNo = 0
        self._translate = QCoreApplication.translate

        self.ui.pushButton_Add.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
                                          "font-weight: 400;font-size: 14px;line-height: 20px;border: 0px;\">" +
                                          self._translate("SupplementalListWidgetWithWidgets", "Add more files") +
                                          "</p>")

        self.mask = None
        # self.maskCount = 0
        self.afw = None
        self.alert = None
        self.alertwithbuttons = None

    @dispatch(list, QMainWindow)
    def __init__(self, sList, mainWindow=None, width=240, height=46):
        super(SupplementalListWidgetWithWidgets, self).__init__()

        self.mainWindow = mainWindow
        self.ui = Ui_SupplementalListWidgetWithWidgets()
        self.ui.setupUi(self)

        self.ui.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.verticalLayout.setContentsMargins(0, 0, 0, 0)

        if len(sList) > 0:
            self.ui.label_NoItem.setVisible(False)
            self.ui.listWidget.setEnabled(True)
            self._isEmpty = False
        else:
            self.ui.label_NoItem.setVisible(True)
            self.ui.listWidget.setEnabled(False)
            self._isEmpty = True

        self._listWidgetItemSerialNo = 0  # Unique index for

        # self.ui.listWidget.setDragDropMode(QAbstractItemView.InternalMove)
        # self.ui.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.ui.listWidget.customContextMenuRequested[QPoint].connect(self.on_SupplementalListWidgetContextMenu_triggered)

        self._itemWidth = width
        self._itemHeight = height

        self._translate = QCoreApplication.translate
        self.ui.pushButton_Add.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
                                          "font-weight: 400;font-size: 14px;line-height: 20px;border: 0px;\">" +
                                          self._translate("SupplementalListWidgetWithWidgets", "Add more files") +
                                          "</p>")

        self.mask = None
        self.afw = None
        self.alert = None
        self.alertwithbuttons = None

        book = Audiobook.getInstance()
        for s in sList:
            url = s.get("url", "")
            if url != "":
                item = QListWidgetItem()
                # item.setText(str(self.ui.listWidget.count()))
                item.setSizeHint(self.getItemSize())
                roi = SupplementalListWidgetItem((book.getBookDir() + '/' + url, url)[url.startswith('http')],
                                                 item,
                                                 self.getSerialNo())

                self.ui.listWidget.addItem(item)
                self.ui.listWidget.setItemWidget(item, roi)
                self._listWidgetItemSerialNo += 1

    def _openAlertWithButtonsWindow(self, str_Msg, str_Title):
        self.mask = MaskWidget(self.mainWindow)
        self.mask.show()

        self.alertwithbuttons = AlertWithButtons(str_Msg, str_Title)
        self.alertwithbuttons.move(
            self.mainWindow.geometry().x() +
            self.mainWindow.geometry().width() / 2 -
            self.alertwithbuttons.geometry().width() / 2,
            self.mainWindow.geometry().y() +
            self.mainWindow.geometry().height() / 2 -
            self.alertwithbuttons.geometry().height() / 2)

        result = self.alertwithbuttons.exec_()
        self.mask.close()
        return result

    def _openAlertWindow(self, str_Msg, str_Title):
        self.mask = MaskWidget(self.mainWindow)
        self.mask.show()

        self.alert = Alert(str_Msg,
                           str_Title)
        self.alert.move(
            self.mainWindow.geometry().x() +
            self.mainWindow.geometry().width() / 2 -
            self.alert.geometry().width() / 2,
            self.mainWindow.geometry().y() +
            self.mainWindow.geometry().height() / 2 -
            self.alert.geometry().height() / 2)

        result = self.alert.exec_()
        self.mask.close()
        return result

    def getAttachFromWidgetResult(self, bool_Result, list_Result):
        logging.debug(str(bool_Result) + ' ' + ";".join(list_Result))
        book = Audiobook.getInstance()
        set_url = book.getCheckSet(self.mainWindow)
        filenames = []

        if not bool_Result:
            filenames = list_Result
            book.checkAttachedFile(filenames, set_url, SupplementalListWidgetWithWidgets, self)

    @Slot()
    def on_pushButton_Add_clicked(self):
        logging.debug('on_pushButton_Add_clicked')
        if self._isEmpty:
            self.ui.label_NoItem.setVisible(False)
            self.ui.listWidget.setEnabled(True)
            self._isEmpty = False

        book = Audiobook.getInstance()

        self.mask = MaskWidget(self.mainWindow)
        self.mask.show()

        self.afw = AttachFromWidgetWithoutURL(False,
                                              'Open files',
                                              (SupplementalListWidgetWithWidgets.str_LastOpenedDirectory,
                                               book.getBookDir() + '/')
                                              [SupplementalListWidgetWithWidgets.str_LastOpenedDirectory is None],
                                              "Any file(*.*)")

        self.afw.move(self.mainWindow.geometry().x() +
                      self.mainWindow.geometry().width() / 2 -
                      self.afw.geometry().width() / 2,
                      self.mainWindow.geometry().y() +
                      self.mainWindow.geometry().height() / 2 -
                      self.afw.geometry().height() / 2)

        result = self.afw.exec_()
        filenames = self.afw.getURLs()

        self.mask.close()

        if result == QDialog.Accepted and filenames:
            self.getAttachFromWidgetResult(False, filenames)
        else:
            return

    @Slot(bool)
    def on_removeItemAction_triggered(self, checked):
        logging.debug("removeItem is clicked")
        self.removeSelectedItems()
        self.resortItems()

    def removeItem(self, item):
        logging.debug("removeItem is called")
        oldItem = self.ui.listWidget.takeItem(self.ui.listWidget.row(item))
        del oldItem
        if self.ui.listWidget.count() == 0:
            self.ui.label_NoItem.setVisible(True)
            self.ui.listWidget.setEnabled(False)
            self._isEmpty = True

    def getItemSize(self):
        return QSize(self._itemWidth, self._itemHeight)

    def getSerialNo(self):
        return self._listWidgetItemSerialNo

    def addItems(self, fullFilename='', number=1):
        logging.debug('addItems() is called')
        for i in range(number):
            item = QListWidgetItem()
            # item.setText(str(self.ui.listWidget.count()))
            item.setSizeHint(self.getItemSize())

            if fullFilename == '':
                roi = SupplementalListWidgetItem(item, self.getSerialNo())
            else:
                roi = SupplementalListWidgetItem(fullFilename, item, self.getSerialNo())

            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, roi)
            self._listWidgetItemSerialNo += 1

    def removeSelectedItems(self):
        items = self.listWidget.selectedItems()
        for item in items:
            oldItem = self.listWidget.takeItem(self.listWidget.row(item))
            QFile.remove(item.getFullFilename())
            del oldItem

    def resortItems(self):
        for i in range(self.listWidget.count()):
            self.listWidget.item(i).setText(str(i))

    def save(self):
        supplementalList = []

        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.itemWidget(self.ui.listWidget.item(i))
            url = item.getFullFilename()  # item.ui.lineEdit.text()
            if url == "":
                continue
            book = Audiobook.getInstance()
            # kind = filetype.guess(book.getBookDir() + '/' + url)

            mime, encoding = mimetypes.guess_type(url, strict=False)

            if mime is None:
                logging.warning('Cannot guess file type!')
                supplementalList.append(
                    {"url": (url.replace(book.getBookDir() + "/", ""), url)[url.startswith('http')]})
            else:
                extension = mimetypes.guess_extension(mime)
                logging.debug('File extension: %s' % extension)
                logging.debug('File MIME type: %s' % mime)
                supplementalList.append({"url": url.replace(book.getBookDir() + "/", ""),
                                         "encodingFormat": mime})

        return supplementalList

    def add_Resource_to_TOC(self, fullFilename, _):
        logging.debug('add_Resource_to_TOC')
        self.signal_Add_Resource_to_TOC.emit(fullFilename, "")

    def mouseDoubleClickEvent(self, event):
        logging.debug(event.localPos())

    def changeEvent(self, event):
        """Handle LanguageChange event"""
        if event.type() == QEvent.LanguageChange:
            logging.debug("Language changed")
            self.ui.retranslateUi(self)
            self.ui.pushButton_Add.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
                                              "font-weight: 400;font-size: 14px;line-height: 20px;border: 0px;\">" +
                                              self._translate("SupplementalListWidgetWithWidgets", "Add more files") +
                                              "</p>")

        super().changeEvent(event)
