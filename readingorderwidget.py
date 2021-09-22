# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 03:49:55 2021
"""

import logging
# import os
# import shutil
import mimetypes
from multipledispatch import dispatch

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# from ui_readingorderitem import Ui_ReadingOrderItem
from ui_readingorderwidget import Ui_ReadingOrderWidget
from readingorderitem import ReadingOrderItem
# from attachfromwidget import AttachFromWidget
from attachfromwidgetwithouturl import AttachFromWidgetWithoutURL
from alert import Alert, AlertWithButtons
from translucent import MaskWidget
from book import Audiobook, Helper
from supplementallistwidgetitem import SupplementalListWidgetItem
# import resources_rc


class ReadingOrderWidget(QWidget):
    signal_Duration_Changed = Signal(float)
    signal_Add_Resource_to_TOC = Signal(str, str)

    str_LastOpenedDirectory = None

    @dispatch(QMainWindow)
    def __init__(self, mainWindow):
        logging.debug('@dispatch()')
        self.__init__(mainWindow, 420, 78)

    @dispatch(QMainWindow, int, int)
    def __init__(self, mainWindow=None, width=420, height=78):
        logging.debug('@dispatch(int, int)')
        super(ReadingOrderWidget, self).__init__()

        self.mainWindow = mainWindow
        self.ui = Ui_ReadingOrderWidget()
        self.ui.setupUi(self)
        self.ui.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.verticalLayout.setAlignment(self.ui.widget, Qt.AlignTop)

        self.ui.verticalLayout.removeWidget(self.ui.label_Book)
        self.ui.verticalLayout.removeWidget(self.ui.listWidget)
        self.ui.listWidget.setVisible(False)
        self.ui.verticalLayout.addSpacerItem(QSpacerItem(420, 10, QSizePolicy.Fixed, QSizePolicy.Expanding))
        self.ui.verticalLayout.addWidget(self.ui.label_Book)
        self.ui.verticalLayout.setAlignment(self.ui.label_Book, Qt.AlignBottom)

        self._listWidgetItemSerialNo = 0
        self._itemWidth = width
        self._itemHeight = height
        self.ui.listWidget.model().rowsMoved.connect(self.afterDrop)
        self.ui.listWidget.installEventFilter(self)

        self._isEmpty = True

        self._translate = QCoreApplication.translate

        self.ui.pushButton_Add.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
                                          "font-weight: 400;font-size: 14px;line-height: 20px;border: 0px;\">" +
                                          self._translate("ReadingOrderWidget", "Add voice to Reading Order") +
                                          "</p>")

        self._seconds_Duration = 0.0
        self.mask = None
        self.afw = None
        self.alert = None
        self.alertwithbuttons = None
        self._afterDrop = False
        self.roiList = []

    @dispatch(list, str, QMainWindow)
    def __init__(self, rList, bookDir, mainWindow=None, width=420, height=78):
        super(ReadingOrderWidget, self).__init__()

        self.mainWindow = mainWindow
        self.ui = Ui_ReadingOrderWidget()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate

        self.ui.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.listWidget.model().rowsMoved.connect(self.afterDrop)
        self.ui.pushButton_Add.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
                                          "font-weight: 400;font-size: 14px;line-height: 20px;border: 0px;\">" +
                                          self._translate("ReadingOrderWidget", "Add voice to Reading Order") +
                                          "</p>")

        # self.ui.listWidget.setAcceptDrops(True)
        self.ui.listWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.ui.listWidget.setDefaultDropAction(Qt.MoveAction)
        self.ui.listWidget.installEventFilter(self)

        if len(rList) > 0:

            for i in range(self.ui.verticalLayout.count()):
                item = self.ui.verticalLayout.itemAt(i)
                if isinstance(item, QSpacerItem):
                    logging.debug("QSpacerItem  is at pos " + str(i))
                    one = self.ui.verticalLayout.takeAt(i)
                    del one
                    break

            self.ui.verticalLayout.removeWidget(self.ui.widget_Board)
            self.ui.verticalLayout.removeWidget(self.ui.label_Book)
            self.ui.widget_Board.setVisible(False)
            self.ui.label_Book.setVisible(False)
            # self.ui.verticalLayout.removeItem(self.spacerItem)
            self.ui.verticalLayout.addWidget(self.ui.listWidget, 1)
            self.ui.listWidget.show()

            logging.debug(self.ui.verticalLayout.count())
            self._isEmpty = False

        else:
            self.ui.verticalLayout.removeWidget(self.ui.listWidget)
            self.ui.listWidget.hide()
            self.ui.verticalLayout.setAlignment(self.ui.widget, Qt.AlignTop)
            self.ui.verticalLayout.removeWidget(self.ui.label_Book)
            self.ui.verticalLayout.addSpacerItem(QSpacerItem(420, 10, QSizePolicy.Fixed, QSizePolicy.Expanding))
            self.ui.verticalLayout.addWidget(self.ui.label_Book)
            self.ui.verticalLayout.setAlignment(self.ui.label_Book, Qt.AlignBottom)
            self._isEmpty = True

        self._listWidgetItemSerialNo = 0
        self._itemWidth = width
        self._itemHeight = height
        self._seconds_Duration = 0.0
        self.roiList = []
        book = Audiobook.getInstance()

        if len(rList) > 0:
            self._isEmpty = False

            for r in rList:
                logging.debug(r)
                if isinstance(r, dict):
                    url = r.get("url", "")

                    item = QListWidgetItem()
                    # item.setText(str(self.ui.listWidget.count()))
                    item.setSizeHint(self.getItemSize())

                    roi = ReadingOrderItem((book.getBookDir() + '/' + url, url)[url.startswith("http")],
                                           item,
                                           self.getSerialNo())

                    roi.ui.lineEdit.setText(r.get("name", ""))

                    self.ui.listWidget.addItem(item)
                    self.ui.listWidget.setItemWidget(item, roi)
                    self._listWidgetItemSerialNo += 1
                    self.roiList.append(roi)
                elif isinstance(r, str):
                    logging.debug("isinstance(r, str)")
                    url = r
                    if url.startswith("http"):  # http(s) link
                        pass
                    else:
                        item = QListWidgetItem()
                        # item.setText(str(self.ui.listWidget.count()))
                        item.setSizeHint(self.getItemSize())

                        roi = ReadingOrderItem((book.getBookDir() + '/' + url, url)[url.startswith("http")],
                                               item,
                                               self.getSerialNo())
                        self.ui.listWidget.addItem(item)
                        self.ui.listWidget.setItemWidget(item, roi)
                        self._listWidgetItemSerialNo += 1
                        self.roiList.append(roi)
            logging.warning("ROL has initialized")
            logging.debug(self._seconds_Duration)
            self.resortItems()

        self.getDuration()

        self.mask = None
        self.afw = None
        self.alert = None
        self.alertwithbuttons = None
        self._afterDrop = False

    def getItemSize(self):
        return QSize(self._itemWidth, self._itemHeight)

    def getSerialNo(self):
        return self._listWidgetItemSerialNo

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
            book.checkAttachedFile(filenames, set_url, ReadingOrderWidget, self)

    @Slot()
    def on_pushButton_Add_clicked(self):
        logging.debug('on_pushButton_Add_clicked')
        book = Audiobook.getInstance()

        self.mask = MaskWidget(self.mainWindow)
        self.mask.show()

        self.afw = AttachFromWidgetWithoutURL(False,
                                              self._translate("ReadingOrderWidget", 'Open file'),
                                              (ReadingOrderWidget.str_LastOpenedDirectory, book.getBookDir() + '/')
                                              [ReadingOrderWidget.str_LastOpenedDirectory is None],
                                              "Audio files (*.mp3);; Wav files (*.wav)")

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

    def getDuration(self):
        duration = 0.0
        for i in range(self.ui.listWidget.count()):
            duration += self.ui.listWidget.itemWidget(self.ui.listWidget.item(i)).getDuration()
        self._seconds_Duration = duration
        logging.debug('latest total duration = ' + str(duration) + ' seconds.')
        self.signal_Duration_Changed.emit(duration)
        return duration

    @Slot(str, int)
    def addItems(self, fullFilename='', number=1):
        logging.debug("addItems()")
        logging.debug('fullFilename = ' + fullFilename)
        if self.ui.listWidget.count() == 0:
            for i in range(self.ui.verticalLayout.count()):
                item = self.ui.verticalLayout.itemAt(i)
                if isinstance(item, QSpacerItem):
                    logging.debug("QSpacerItem  is at pos " + str(i))
                    one = self.ui.verticalLayout.takeAt(i)
                    del one
                    break

            self.ui.verticalLayout.removeWidget(self.ui.widget_Board)
            self.ui.verticalLayout.removeWidget(self.ui.label_Book)
            self.ui.widget_Board.setVisible(False)
            self.ui.label_Book.setVisible(False)
            # self.ui.verticalLayout.removeItem(self.spacerItem)
            self.ui.verticalLayout.addWidget(self.ui.listWidget, 1)
            self.ui.listWidget.show()

            self._isEmpty = False

        for i in range(number):
            item = QListWidgetItem()
            # item.setText(str(self.ui.listWidget.count()))
            item.setSizeHint(self.getItemSize())

            if fullFilename == '':
                roi = ReadingOrderItem(item, self.getSerialNo())
            else:
                roi = ReadingOrderItem(fullFilename, item, self.getSerialNo())

            # roi = ReadingOrderItem(item, self.getSerialNo())
            roi.ui.label_Index.setText("{:d}".format(self.ui.listWidget.count()))
            # roi.signal_resize_item.connect(self.on_signal_resize_item)

            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, roi)
            self._listWidgetItemSerialNo += 1
            self.roiList.append(roi)

        # print(self.ui.listWidget.geometry())
        self.getDuration()

    @Slot()
    def removeSelectedItems(self):
        items = self.ui.listWidget.selectedItems()
        for item in items:
            oldItem = self.ui.listWidget.takeItem(self.ui.listWidget.row(item))
            del oldItem

        if self.ui.listWidget.count() == 0:
            # self.spacerItem = QSpacerItem(420, 10, QSizePolicy.Fixed, QSizePolicy.Expanding)

            self.ui.verticalLayout.removeWidget(self.ui.listWidget)
            self.ui.listWidget.hide()
            self.ui.verticalLayout.addWidget(self.ui.widget_Board)
            self.ui.widget_Board.show()
            self.ui.verticalLayout.addSpacerItem(QSpacerItem(420, 10, QSizePolicy.Fixed, QSizePolicy.Expanding))
            self.ui.verticalLayout.addWidget(self.ui.label_Book)
            self.ui.label_Book.show()
            self._isEmpty = True

        self.resortItems()
        self.getDuration()

    def removeItem(self, item):
        logging.debug("removeItem is called")
        itemWidget = self.ui.listWidget.itemWidget(item)
        if itemWidget is not None:
            self.roiList.remove(itemWidget)
            del itemWidget
        oldItem = self.ui.listWidget.takeItem(self.ui.listWidget.row(item))
        # itemWidget = self.ui.listWidget.itemWidget(oldItem)

        del oldItem

        if self.ui.listWidget.count() == 0:
            self.ui.verticalLayout.removeWidget(self.ui.listWidget)
            self.ui.listWidget.hide()
            self.ui.verticalLayout.addWidget(self.ui.widget_Board)
            self.ui.widget_Board.show()
            self.ui.verticalLayout.addSpacerItem(QSpacerItem(420, 10, QSizePolicy.Fixed, QSizePolicy.Expanding))
            self.ui.verticalLayout.addWidget(self.ui.label_Book)
            self.ui.label_Book.show()
            self._isEmpty = True

        self.resortItems()
        self.getDuration()

    def resortItems(self):
        for i in range(self.ui.listWidget.count()):
            # self.ui.listWidget.item(i).setText(str(i))
            itemWidget = self.ui.listWidget.itemWidget(self.ui.listWidget.item(i))
            itemWidget.ui.label_Index.setText("{:d}".format(i))

    def save(self):
        readingOrderList = []
        seconds_Duration = 0.0

        for i in range(self.ui.listWidget.count()):
            # item = self.listWidget.item(i)
            item = self.ui.listWidget.itemWidget(self.ui.listWidget.item(i))

            # url = item.ui.label_Href.text()
            url = item.getFullFilename()

            if url == "*.mp3":
                continue

            mime, encoding = mimetypes.guess_type(url, strict=False)
            extension = mimetypes.guess_extension(mime, strict=False)

            # kind = filetype.guess(url)
            book = Audiobook.getInstance()
            # kind = filetype.guess(bookDir + r'/' + url)
            if mime is None:
                logging.warning('Cannot guess file type!')
                readingOrderList.append({"url": (url.replace(book.getBookDir() + "/", "")
                                                 , url)[url.startswith('http')]})
            else:
                logging.debug('File extension: %s' % extension)
                logging.debug('File MIME type: %s' % mime)
                if extension == ".mp3" and mime.startswith("audio"):
                    seconds_Duration += item.getDuration()  # _seconds
                    logging.debug("url = " + url)

                    readingOrderList.append({"url": (url.replace(book.getBookDir() + "/",
                                                                 ""), url)[url.startswith('http')],
                                             "encodingFormat": mime,
                                             "name": item.ui.lineEdit.text(),
                                             "duration": "PT" + str(item.getDuration()) + "S"})

        return readingOrderList

    def add_Resource_to_TOC(self, fullFilename, title):
        logging.debug('add_Resource_to_TOC')
        self.signal_Add_Resource_to_TOC.emit(fullFilename, title)

    def afterDrop(self, parent, start, end, destination, row):
        # super(ReadingOrderWidget, self).dropEvent(event)
        logging.debug('afterDrop')
        self._afterDrop = True
        self.resortItems()

    def changeEvent(self, event):
        """Handle LanguageChange event"""
        if event.type() == QEvent.LanguageChange:
            logging.debug("Language changed")
            self.ui.retranslateUi(self)
            self.ui.pushButton_Add.setToolTip("<p style=\"color:#FFFFFF;font-family: Noto Sans;font-style: normal;"
                                              "font-weight: 400;font-size: 14px;line-height: 20px;border: 0px;\">" +
                                              self._translate("ReadingOrderWidget", "Add voice to Reading Order") +
                                              "</p>")
        super().changeEvent(event)

    def eventFilter(self, sender, event):
        if not (event.type() in [QEvent.Paint, QEvent.Leave, QEvent.Enter, QEvent.FocusAboutToChange, QEvent.Timer]):
            logging.debug(event.type())

        if event.type() == QEvent.DragEnter:
            logging.debug("QEvent.DragEnter")
            logging.debug(sender)
            logging.debug(event.source())
            logging.debug(event.mimeData().formats())

            # It's a ReadingOrderItem, not a SupplementalListWidgetItem
            # if sender is self.ui.listWidget:
            if isinstance(event.source(), ReadingOrderItem):
                # self.ui.listWidget.setDragDropMode(QAbstractItemView.InternalMove)
                event.setDropAction(Qt.MoveAction)
                event.acceptProposedAction()
                return True

            # if event.mimeData().hasText() and event.mimeData().hasUrls():
            #     logging.debug(event.mimeData().text())
            #     for url in event.mimeData().urls():
            #         logging.debug(url.toString())
            #     # event.acceptProposedAction()
            #     self.dragEnterEvent(event)
            #     return True

            #  It's a SupplementalListWidgetItem, not a ReadingOrderItem
            elif isinstance(event.source(), SupplementalListWidgetItem):  # not event.mimeData().hasText() and event.mimeData().hasUrls():
                # event.setDropAction(Qt.CopyAction)
                # event.acceptProposedAction()
                event.ignore()
                return True
            else:
                super().eventFilter(sender, event)
                return True

        elif event.type() == QEvent.Drop:
            logging.debug("QEvent.Drop")
            logging.debug(sender)
            logging.debug(event.source())
            logging.debug(event.mimeData().formats())

            # It's a ReadingOrderItem, not a SupplementalListWidgetItem
            if isinstance(event.source(), ReadingOrderItem):
                event.acceptProposedAction()

                # target = self.ui.listWidget.itemAt(event.pos())
                # sources = self.ui.listWidget.selectedItems()
                # logging.debug(event.pos())
                # logging.debug(target)
                # logging.debug(sources)

                selection = self.ui.listWidget.selectedIndexes()
                from_index = selection[0].row() if selection else -1
                to_index = self.ui.listWidget.indexAt(event.pos()).row()
                if (0 <= from_index < self.ui.listWidget.model().rowCount() and
                        0 <= to_index < self.ui.listWidget.model().rowCount() and
                        from_index != to_index):
                    if from_index < to_index:
                        for i in range(from_index, to_index):
                            result = self.ui.listWidget.model().moveRow(self.ui.listWidget.rootIndex(),
                                                                        i+1,
                                                                        self.ui.listWidget.rootIndex(),
                                                                        i)
                            logging.debug("from {} to {} : {}".format(from_index, to_index, ("Fail", "Succeed")[result]))
                    else:
                        result = self.ui.listWidget.model().moveRow(self.ui.listWidget.rootIndex(),
                                                                    from_index,
                                                                    self.ui.listWidget.rootIndex(),
                                                                    to_index)
                        logging.debug("from {} to {} : {}".format(from_index, to_index, ("Fail", "Succeed")[result]))
                    event.accept()
                return True

            #  It's a SupplementalListWidgetItem, not a ReadingOrderItem
            elif isinstance(event.source(), SupplementalListWidgetItem):
                event.ignore()
                return True
            else:
                super().eventFilter(sender, event)
                return True

        # elif event.type() == QEvent.ChildRemoved:  # sender == self.ui.listWidget and
        #     logging.debug("QEvent.ChildRemoved")
        #     # self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
        #     logging.debug("SN={}".format(self.getSerialNo()))
        #     logging.debug("listCount={}".format(self.ui.listWidget.count()))
        #     logging.debug("currentRow={}".format(self.ui.listWidget.currentRow()))
        #
        #     if not self._afterDrop:
        #         itemWidget = self.ui.listWidget.itemWidget(self.ui.listWidget.currentItem())
        #         if itemWidget is None:
        #             logging.debug("itemWidget is None")
        #             roiList = self.roiList.copy()
        #             itemWOWidget = -1
        #             for i in range(self.ui.listWidget.count()):
        #                 item = self.ui.listWidget.item(i)
        #                 itemWidget = self.ui.listWidget.itemWidget(item)
        #                 if itemWidget is not None:
        #                     roiList.remove(itemWidget)
        #                 else:
        #                     itemWOWidget = i
        #             if len(roiList) == 1:
        #                 super().eventFilter(sender, event)
        #                 oldROI = roiList[0]
        #                 roi = ReadingOrderItem(oldROI.getFullFilename(),
        #                                        self.ui.listWidget.item(itemWOWidget),
        #                                        self.getSerialNo())
        #                 roi.ui.lineEdit.setText(oldROI.ui.lineEdit.text())
        #                 self._listWidgetItemSerialNo += 1
        #                 self.ui.listWidget.setItemWidget(self.ui.listWidget.item(itemWOWidget), roi)
        #                 self.roiList.remove(oldROI)
        #                 self.roiList.append(roi)
        #                 self.resortItems()
        #                 return True
        #     else:
        #         self._afterDrop = False
        #         return False

        return super().eventFilter(sender, event)

    # def dragEnterEvent(self, event):
    #     logging.debug(event.source())
    #     logging.debug(event.mimeData().formats())
    #     # for mimeType in event.mimeData().formats():
    #     #     logging.debug(mimeType)
    #
    #     # It's a ReadingOrderItem, not a SupplementalListWidgetItem
    #     if event.mimeData().hasText() and event.mimeData().hasUrls():
    #         logging.debug(event.mimeData().text())
    #         for url in event.mimeData().urls():
    #             logging.debug(url.toString())
    #         event.acceptProposedAction()
    #     else:
    #         event.ignore()
    #
    # def dropEvent(self, event):
    #     logging.debug(event.source())
    #     logging.debug(event.mimeData().text())
    #     for url in event.mimeData().urls():
    #         logging.debug(url.toString())
    #
    #     event.setDropAction(Qt.MoveAction)
    #     self.ui.listWidget.setDragDropMode(QAbstractItemView.InternalMove)
    #     event.accept()



    # def eventFilter(self, sender, event):
    #     if sender == self.ui.listWidget and event.type() == QEvent.ChildRemoved:
    #         logging.debug("eventFilter")
    #         # self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
    #         logging.debug("SN={}".format(self.getSerialNo()))
    #         logging.debug("listCount={}".format(self.ui.listWidget.count()))
    #         logging.debug("currentRow={}".format(self.ui.listWidget.currentRow()))
    #
    #         if not self._afterDrop:
    #             itemWidget = self.ui.listWidget.itemWidget(self.ui.listWidget.currentItem())
    #             if itemWidget is None:
    #                 logging.debug("itemWidget is None")
    #                 roiList = self.roiList.copy()
    #                 itemWOWidget = -1
    #                 for i in range(self.ui.listWidget.count()):
    #                     item = self.ui.listWidget.item(i)
    #                     itemWidget = self.ui.listWidget.itemWidget(item)
    #                     if itemWidget is not None:
    #                         roiList.remove(itemWidget)
    #                     else:
    #                         itemWOWidget = i
    #                 if len(roiList) == 1:
    #                     super().eventFilter(sender, event)
    #                     oldROI = roiList[0]
    #                     roi = ReadingOrderItem(oldROI.getFullFilename(),
    #                                            self.ui.listWidget.item(itemWOWidget),
    #                                            self.getSerialNo())
    #                     roi.ui.lineEdit.setText(oldROI.ui.lineEdit.text())
    #                     self._listWidgetItemSerialNo += 1
    #                     self.ui.listWidget.setItemWidget(self.ui.listWidget.item(itemWOWidget), roi)
    #                     self.roiList.remove(oldROI)
    #                     self.roiList.append(roi)
    #                     self.resortItems()
    #                     return True
    #         else:
    #             self._afterDrop = False
    #
    #     return super().eventFilter(sender, event)
