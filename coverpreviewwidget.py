# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 13:03:44 2021
"""

import logging
import mimetypes
from multipledispatch import dispatch
import os
import shutil
# import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from book import Audiobook
from ui_coverpreviewwidget import Ui_CoverPreviewWidget
# from attachfromwidget import AttachFromWidget
from attachfromwidgetwithouturl import AttachFromWidgetWithoutURL
from alert import Alert, AlertWithButtons
from translucent import MaskWidget
import resources_rc


class CoverPreviewWidget(QWidget):
    switch_window = Signal()

    @dispatch(dict, str, QMainWindow)
    def __init__(self, dict_Cover, dir_Book, mainWindow=None):
        super(CoverPreviewWidget, self).__init__()

        self.mainWindow = mainWindow
        self.ui = Ui_CoverPreviewWidget()
        self.ui.setupUi(self)
        self.href = ""

        url = dict_Cover.get("url", "")
        if url == "" or url.endswith(".html"):  # For now, just "bypass" .html cover
            # self.href = dir_Book + "/" + url
            self.href = ""

            self.ui.pushButton_AddCover.setVisible(True)
            self.ui.pushButton_Remove.setVisible(False)
            self.ui.pushButton_Replace.setVisible(False)

        else:
            # try:
            self.href = dir_Book + "/" + url
            if not os.path.exists(self.href):
                self.ui.label_Cover.setPixmap(QPixmap(":/SVG/svg/icon/cover-preview-empty.svg"))
                self.href = ''
                self.ui.pushButton_Remove.setVisible(False)
                self.ui.pushButton_Replace.setVisible(False)
                self.ui.pushButton_AddCover.setVisible(True)
            else:
                pixmap = QPixmap(self.href)
                w, h = pixmap.size().width(), pixmap.size().height()
                img = pixmap.scaledToWidth(120, Qt.SmoothTransformation) \
                    if w > h else pixmap.scaledToHeight(120, Qt.SmoothTransformation)

                self.coverFilename = self.href

                self.ui.label_Cover.setFixedSize(img.size())
                self.ui.label_Cover.setPixmap(img)

                # pixmap = pixmap.scaled(self.ui.label_Cover.size(), Qt.KeepAspectRatio)
                # self.ui.label_Cover.setPixmap(pixmap)
                self.ui.pushButton_Remove.setVisible(True)
                self.ui.pushButton_Replace.setVisible(True)
                self.ui.pushButton_AddCover.setVisible(False)

            # except Exception as ex:
            #     logging.critical(ex)
            #     self.href = ''
            #     self.ui.pushButton_AddCover.setVisible(True)
            #     self.ui.pushButton_Remove.setVisible(False)
            #     self.ui.pushButton_Replace.setVisible(False)

        self.ui.pushButton_AddCover.clicked.connect(
            lambda: self.on_pushButton_clicked(self.ui.pushButton_AddCover))
        self.ui.pushButton_Replace.clicked.connect(
            lambda: self.on_pushButton_clicked(self.ui.pushButton_Replace))
        self.ui.pushButton_Remove.clicked.connect(
            lambda: self.on_pushButton_clicked(self.ui.pushButton_Remove))

        self._translate = QCoreApplication.translate

        # self.ui.pushButton_AddCover.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
        #                                        "font-weight: 400;font-size: 14px;line-height: 20px;"
        #                                        "border: 0px #404040;\">" +
        #                                        self._translate("CoverPreviewWidget", "Add a picture as cover") +
        #                                        "</p>")
        # self.ui.pushButton_Replace.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
        #                                       "font-weight: 400;font-size: 14px;line-height: 20px;"
        #                                       "border: 0px #404040;\">" +
        #                                       self._translate("CoverPreviewWidget", "Replace this cover") +
        #                                       "</p>")
        # self.ui.pushButton_Remove.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
        #                                      "font-weight: 400;font-size: 14px;line-height: 20px;"
        #                                      "border: 0px #404040;\">" +
        #                                      self._translate("CoverPreviewWidget", "Remove this cover") +
        #                                      "</p>")

        self.mask = None
        self.alert = None
        self.afw = None

    @dispatch(QMainWindow)
    def __init__(self, mainWindow=None):
        super(CoverPreviewWidget, self).__init__()

        self.mainWindow = mainWindow
        self.ui = Ui_CoverPreviewWidget()
        self.ui.setupUi(self)
        self.href = ""

        self.ui.pushButton_AddCover.setVisible(True)
        self.ui.pushButton_Remove.setVisible(False)
        self.ui.pushButton_Replace.setVisible(False)

        self.ui.pushButton_AddCover.clicked.connect(lambda: self.on_pushButton_clicked(self.ui.pushButton_AddCover))
        self.ui.pushButton_Replace.clicked.connect(lambda: self.on_pushButton_clicked(self.ui.pushButton_Replace))
        self.ui.pushButton_Remove.clicked.connect(lambda: self.on_pushButton_clicked(self.ui.pushButton_Remove))

        self._translate = QCoreApplication.translate

        # self.ui.pushButton_AddCover.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
        #                                        "font-weight: 400;font-size: 14px;line-height: 20px;"
        #                                        "border: 0px #404040;\">" +
        #                                        self._translate("CoverPreviewWidget", "Add a picture as cover") +
        #                                        "</p>")
        # self.ui.pushButton_Replace.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
        #                                       "font-weight: 400;font-size: 14px;line-height: 20px;"
        #                                       "border: 0px #404040;\">" +
        #                                       self._translate("CoverPreviewWidget", "Replace this cover") +
        #                                       "</p>")
        # self.ui.pushButton_Remove.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
        #                                      "font-weight: 400;font-size: 14px;line-height: 20px;"
        #                                      "border: 0px #404040;\">" +
        #                                      self._translate("CoverPreviewWidget", "Remove this cover") +
        #                                      "</p>")

        self.mask = None
        self.alert = None
        self.afw = None

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

    def getAttachFromWidgetResult(self, bool_Result, str_Result):
        logging.debug(str(bool_Result) + ' ' + str_Result)
        book = Audiobook.getInstance()
        option, list_compulsory = book.determineOption()

        url_compulsory = [book.getBookDir() + '/' + f
                          for f in list_compulsory
                          if not f.startswith('http')]
        url_orderingOrder = [book.getBookDir() + '/' + f["url"]
                             for f in self.mainWindow.readingOrderWidget.save()
                             if not f["url"].startswith('http')]
        url_toc = [book.getBookDir() + '/' + f["href"]
                   for f in self.mainWindow.tocWidget.save(True)
                   if not f["href"].startswith('http')]
        url_cover = [book.getBookDir() + '/' + f["url"]
                     for f in [self.save()]
                     if not f["url"].startswith('http')]
        url_supplemental = [book.getBookDir() + '/' + f["url"] for f in self.mainWindow.supplementalListWidget.save()
                            if not f["url"].startswith('http')]

        set_url = set(url_compulsory +
                      url_orderingOrder +
                      url_toc +
                      url_cover +
                      url_supplemental)

        filename = ""

        if not bool_Result:
            filename = str_Result
            file_folder, file_name = os.path.split(filename)

            if filename in set_url:
                logging.debug("You have chosen one file already in this audiobook")

                self._openAlertWindow(self._translate("CoverPreviewWidget",
                                                      'You have chosen one file already in this audiobook!'),
                                      self._translate("CoverPreviewWidget", "Warning"))

                filename = ""
                return

            elif book.getBookDir() + '/' + file_name in set_url:
                logging.debug("One file with the same name is already in this audiobook")

                result = self._openAlertWithButtonsWindow(self._translate("CoverPreviewWidget",
                                                                          'One file with the same name is already '
                                                                          'in this audiobook! '
                                                                          'Do you want to overwrite '
                                                                          'that original file?'),
                                                          self._translate("CoverPreviewWidget",
                                                                          "Warning"))

                if result:
                    try:
                        shutil.copyfile(filename, book.getBookDir() + '/' + file_name)
                        filename = book.getBookDir() + '/' + file_name
                    except Exception as ex:
                        logging.critical(ex)

                        self._openAlertWindow(self._translate("CoverPreviewWidget",
                                                              'Sorry, we couldn\'t overwrite the original file!'),
                                              self._translate("CoverPreviewWidget", "Warning"))

                        return
                else:
                    filename = ""
                    return

            elif file_folder == book.getBookDir():
                pass
            else:
                pass

            src = QFile(filename)
            # info = QFileInfo(filename)
            if file_folder != book.getBookDir():
                try:
                    shutil.copyfile(filename, book.getBookDir() + '/' + file_name)
                    filename = book.getBookDir() + '/' + file_name
                except Exception as ex:
                    logging.critical(ex)

                    self._openAlertWindow(self._translate("CoverPreviewWidget",
                                                          'Sorry, we couldn\'t copy this file '
                                                          'to the audiobook folder!'),
                                          self._translate("CoverPreviewWidget",
                                                          "Warning"))
                    return
            else:
                filename = book.getBookDir() + '/' + file_name

            img = QPixmap(filename)
            w, h = img.size().width(), img.size().height()
            img = img.scaledToWidth(120, Qt.SmoothTransformation) \
                if w > h else img.scaledToHeight(120, Qt.SmoothTransformation)
            # self.ui.label_Cover.setFixedSize(img.size())
            # self.ui.label_Cover.setPixmap(img)

            if self.href:
                bool_Removed = QFile.remove(self.href)
                if not bool_Removed:
                    self._openAlertWindow(self._translate("CoverPreviewWidget",
                                                          'We couldn\'t remove the old cover for you!'),
                                          self._translate("CoverPreviewWidget",
                                                          "Warning"))
                    # return

            self.ui.label_Cover.setFixedSize(img.size())
            self.ui.label_Cover.setPixmap(img)
            self.href = filename
            self.ui.pushButton_Remove.setVisible(True)
            self.ui.pushButton_Replace.setVisible(True)
            self.ui.pushButton_AddCover.setVisible(False)

    def _getOpenFilename(self, bool_Flag, str_Title, str_Path, str_FileTypes):
        logging.debug('_getOpenFilename')
        self.mask = MaskWidget(self.mainWindow)
        self.mask.show()

        self.afw = AttachFromWidgetWithoutURL(bool_Flag,
                                              str_Title,
                                              str_Path,
                                              str_FileTypes)

        self.afw.move(self.mainWindow.geometry().x() +
                      self.mainWindow.geometry().width() / 2 -
                      self.afw.geometry().width() / 2,
                      self.mainWindow.geometry().y() +
                      self.mainWindow.geometry().height() / 2 -
                      self.afw.geometry().height() / 2)

        result = self.afw.exec_()
        filename = self.afw.getURL()

        self.mask.close()
        return result, filename

    def on_pushButton_clicked(self, sender):
        book = Audiobook.getInstance()
        if sender.objectName() == "pushButton_AddCover":
            logging.debug('button_AddCover is clicked')

            filename, _ = QFileDialog.getOpenFileName(self,
                                                      self._translate("CoverPreviewWidget", 'Open file'),
                                                      book.getBookDir() + '/',
                                                      "JPG Files (*.jpg);;PNG Files (*.png)")

            # result, filename = self._getOpenFilename(False,
            #                                          'Open file',
            #                                          book.getBookDir() + '/',
            #                                          "JPG Files (*.jpg);;PNG Files (*.png)")

            if filename:
                self.getAttachFromWidgetResult(False, filename)
            else:
                return

        elif sender.objectName() == 'pushButton_Remove':
            logging.debug('button_Remove is clicked')
            bool_removed = QFile.remove(self.href)
            self.ui.label_Cover.setFixedSize(120, 120)
            self.ui.label_Cover.setPixmap(QPixmap(":/SVG/svg/icon/cover-preview-empty.svg"))
            self.href = ''

            self.ui.pushButton_Remove.setVisible(False)
            self.ui.pushButton_Replace.setVisible(False)
            self.ui.pushButton_AddCover.setVisible(True)

        elif sender.objectName() == 'pushButton_Replace':
            logging.debug('button_Replace is clicked')

            filename, _ = QFileDialog.getOpenFileName(self,
                                                      self._translate("CoverPreviewWidget", 'Open file'),
                                                      book.getBookDir() + '/',
                                                      "JPG Files (*.jpg);;PNG Files (*.png)")

            if filename:
                self.getAttachFromWidgetResult(False, filename)
            else:
                return

    def save(self):
        book = Audiobook.getInstance()
        # kind = filetype.guess(self.href)

        mime, _ = mimetypes.guess_type(self.href)
        extension = mimetypes.guess_extension(self.href)

        if mime is not None:
            dict_cover = {"url": self.href.replace(book.getBookDir() + "/", ""),
                          "encodingFormat": mime,
                          "name": "Cover",
                          "rel": "cover"}
        else:
            dict_cover = {"url": "",
                          "encodingFormat": "",
                          "name": "Cover",
                          "rel": "cover"}
        return dict_cover

    def changeEvent(self, event):
        """Handle LanguageChange event"""
        if event.type() == QEvent.LanguageChange:
            logging.debug("Language changed")
            self.ui.retranslateUi(self)

        super().changeEvent(event)
