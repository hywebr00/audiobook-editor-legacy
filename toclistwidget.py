# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 18:41:48 2021
"""

import json
import logging
from multipledispatch import dispatch

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from toclistwidgetitem import TOCListWidgetItem
from book import Audiobook, Helper 
from alert import Alert
from translucent import MaskWidget

from ui_toclistwidget import Ui_TOCListWidget


class TOCListWidget(QWidget):
    
    signal_duration_calculated = Signal(float)

    @dispatch(QMainWindow)
    def __init__(self, mainWindow):
        logging.debug('@dispatch()')
        super(TOCListWidget, self).__init__()
        self._initialize(mainWindow, 240, 82)

    @dispatch(QMainWindow, int, int)
    def __init__(self, mainWindow, width=240, height=82):
        super(TOCListWidget, self).__init__()
        self._initialize(mainWindow, width, height)

    @dispatch(QMainWindow, list)
    def __init__(self, mainWindow, tocList, width=240, height=82):
        super(TOCListWidget, self).__init__()
        self._initialize(mainWindow, width, height)
        self.on_generateListWidgetItemAction_triggered(tocList)

    def _initialize(self, mainWindow, width, height):
        self._itemWidth = width
        self._itemHeight = height
        self.mainWindow = mainWindow

        self.ui = Ui_TOCListWidget()
        self.ui.setupUi(self)
        self.ui.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.ui.listWidget.model().rowsMoved.connect(self.afterDrop)
        self.ui.listWidget.installEventFilter(self)

        self._isEmpty = True
        self._listWidgetItemSerialNo = 0
        self._translate = QCoreApplication.translate
        self._TOCList = []

        self.mask = None
        self.alert = None
        self._afterDrop = False
        self.roiList = []
        self.startTime = ""

    def getItemSize(self):
        return QSize(self._itemWidth, self._itemHeight)
    
    def getSerialNo(self):
        return self._listWidgetItemSerialNo
    
    @dispatch(int)
    def addItems(self, number=1):
        if self._isEmpty:
            self.ui.widget_NoItem.setVisible(False)
            self.ui.listWidget.setEnabled(True)
            self._isEmpty = False
            
        for i in range(number):
            item = QListWidgetItem()  
            # item.setText(str(self.ui.listWidget.count()))
            item.setSizeHint(self.getItemSize()) 
            
            roi = TOCListWidgetItem(item, self.getSerialNo())
              
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, roi)
            self._listWidgetItemSerialNo += 1
            self.roiList.append(roi)

    @dispatch(str)
    def addItems(self, fullFilename):  
        if self._isEmpty:
            self.ui.widget_NoItem.setVisible(False)
            self.ui.listWidget.setEnabled(True)
            self._isEmpty = False
            
        item = QListWidgetItem()  
        # item.setText(str(self.ui.listWidget.count()))
        item.setSizeHint(self.getItemSize()) 
        
        roi = TOCListWidgetItem(fullFilename, item, self.getSerialNo())
          
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.setItemWidget(item, roi)
        self._listWidgetItemSerialNo += 1
        self.roiList.append(roi)
         
    def getSerialNo(self):
        return self._listWidgetItemSerialNo
    
    def removeItem(self, item):
        logging.debug("removeItem is called")

        itemWidget = self.ui.listWidget.itemWidget(item)
        if itemWidget is not None:
            self.roiList.remove(itemWidget)
            del itemWidget
        oldItem = self.ui.listWidget.takeItem(self.ui.listWidget.row(item))
        del oldItem

        # oldItem = self.ui.listWidget.takeItem(self.ui.listWidget.row(item))
        # del oldItem

        if self.ui.listWidget.count() == 0:
            self.ui.widget_NoItem.setVisible(True)
            self.ui.listWidget.setEnabled(False)
            self._isEmpty = True  
            
    def resortItems(self):
        for i in range(self.listWidget.count()):
            self.listWidget.item(i).setText(str(i))

    def on_generateListWidgetItemAction_triggered(self, data, root=None):
        logging.debug('TOCListWidget : on_generateListWidgetItemAction_triggered')
        self.ui.listWidget.clear()
        book = Audiobook.getInstance()
        
        def addChildItem(data, level, parentItem):
            children = data['children']
            if children:
                return
            for i in range(len(children)): 
                child = children[i]
                lvl = child['level']
                if lvl == level:
                    item = QListWidgetItem(parentItem)
                    item.setSizeHint(self.getItemSize()) 
                    
                    roi = TOCListWidgetItem(item, self.getSerialNo())                    
                    roi.ui.lineEdit_Title.setText(dict_TOC['title'])            
                    
                    href = dict_TOC["href"]
                    indexOfSharpSign = href.find('#t=')
                    if indexOfSharpSign == -1:  # Not in
                        roi.ui.label_Href.setText(href)
                    else:
                        timeStamp = href[indexOfSharpSign + 3:]
                        [startTime, endTime] = timeStamp.split(',')
                        roi.ui.timeEdit_Start.setTime(QTime.fromString(startTime, "hh:mm:ss.zzz"))
                        # roi.ui.lineEdit_End.setText(endTime)
                        
                    self._listWidgetItemSerialNo += 1                                            
                    addChildItem(child, level + 1, item)
                    
        if isinstance(data, list):
            logging.debug('isinstance(data, list)')
            if len(data) > 0:
                if self._isEmpty:
                    logging.debug('self.ui.widget_NoItem.setVisible(False)')
                    self.ui.widget_NoItem.setVisible(False)
                    self.ui.listWidget.setEnabled(True)
                    self._isEmpty = False
            
            for i in range(len(data)):
                dict_TOC = data[i]
                level = dict_TOC["level"]
                if level == 0:
                       
                    item = QListWidgetItem()  
                    # item.setText(str(self.ui.listWidget.count()))
                    item.setSizeHint(self.getItemSize()) 
                    
                    href = dict_TOC["href"]
                    indexOfSharpSign = href.find('#t=')
                    timeStamp = ''
                    if indexOfSharpSign == -1:
                        fullFilename = (book.getBookDir() + '/' + href, href)[href.startswith('http')]
                        roi = TOCListWidgetItem(fullFilename, item, self.getSerialNo(), dict_TOC['title'])
                        # roi.ui.lineEdit_Title.setText(dict_TOC['title'])
                    else:
                        timeStamp = href[indexOfSharpSign + 3:]
                        fullFilename = (book.getBookDir() + '/' + href[0: indexOfSharpSign],
                                        href[0: indexOfSharpSign])[href.startswith('http')]
                        roi = TOCListWidgetItem(fullFilename, item, self.getSerialNo(), dict_TOC['title'])
                        # roi.ui.lineEdit_Title.setText(dict_TOC['title'])

                        if timeStamp.find(',') == -1:
                            startTime = timeStamp
                            startTimeFloat = float(startTime)
                            hh = int(startTimeFloat // 3600)
                            startTimeFloat -= hh * 3600
                            mm = int(startTimeFloat // 60)
                            startTimeFloat -= mm * 60
                            ss = int(startTimeFloat)
                            startTimeFloat -= ss
                            zzz = startTimeFloat
                            startTimeString = "{:02d}".format(hh) + \
                                              ":{:02d}".format(mm) + \
                                              ":{:02d}".format(ss) + \
                                              str("{:.3f}".format(zzz))[1: 5]
                            roi.ui.timeEdit_Start.setTime(QTime.fromString(startTimeString, "hh:mm:ss.zzz"))
                        else:
                            # To-Do: start- & end-time both exist
                            [startTime, endTime] = timeStamp.split(',')
                            startTimeFloat = float(startTime)
                            endTimeFloat = float(endTime)

                            hh = int(startTimeFloat // 3600)
                            startTimeFloat -= hh * 3600
                            mm = int(startTimeFloat // 60)
                            startTimeFloat -= mm * 60
                            ss = int(startTimeFloat)
                            startTimeFloat -= ss
                            zzz = startTimeFloat
                            startTimeString = "{:02d}".format(hh) + \
                                              ":{:02d}".format(mm) + \
                                              ":{:02d}".format(ss) + \
                                              str("{:.3f}".format(zzz))[1: 5]

                            hh = int(endTimeFloat // 3600)
                            endTimeFloat -= hh * 3600
                            mm = int(endTimeFloat // 60)
                            endTimeFloat -= mm * 60
                            ss = int(endTimeFloat)
                            endTimeFloat -= ss
                            zzz = endTimeFloat
                            endTimeString = "{:02d}".format(hh) + \
                                              ":{:02d}".format(mm) + \
                                              ":{:02d}".format(ss) + \
                                              str("{:.3f}".format(zzz))[1: 5]

                            roi.ui.timeEdit_Start.setTime(QTime.fromString(startTimeString, "hh:mm:ss.zzz"))

                            pass                    
                    
                    self.ui.listWidget.addItem(item) 
                    self.ui.listWidget.setItemWidget(item, roi)
                    self._listWidgetItemSerialNo += 1                        
                    # if dict_TOC['children'] != []:
                    addChildItem(dict_TOC, level + 1, item)
                    self.roiList.append(roi)
                    
            self.ui.listWidget.setEnabled(True)    

    @Slot()  # FORCE: No checking title and No adding timestamps
    def on_traverseTreeAction_triggered(self, FORCE=False):
        logging.debug("on_traverseAction_triggered")
        self._TOCList = []

        # Warning: This searchChildItem function may need to be FIXED immediately!
        # def serchChildItem(item=None, level=0):
        #     TOCList = []
        #     if not item:
        #         return
        #     for m in range(item.childCount()):
        #         child = item.child(m)
        #         if child.timeEdit_Start.time().toString("hh:mm:ss.zzz") != "00:00:00.000" and \
        #                 child.timeEdit_End.time().toString("hh:mm:ss.zzz") != "00:00:00.000":
        #             startSeconds = child.timeEdit_Start.time().hour() * 3600 + \
        #                            child.timeEdit_Start.time().minute() * 60 + \
        #                            child.timeEdit_Start.time().second() + \
        #                            float(child.timeEdit_Start.time().msec()) / 1000
        #
        #             endSeconds = child.timeEdit_End.time().hour() * 3600 + \
        #                            child.timeEdit_End.time().minute() * 60 + \
        #                            child.timeEdit_End.time().second() + \
        #                            float(child.timeEdit_End.time().msec()) / 1000
        #
        #             TOCList.append({"level": level,
        #                             "href": child.comboBox.currentText() +
        #                                     "#t=" +
        #                                     str(startSeconds) +
        #                                     "," +
        #                                     str(endSeconds),
        #                             "title": child.lineEdit.text(),
        #                             "children": serchChildItem(child, level + 1)})
        #         else:
        #             TOCList.append({"level": level,
        #                             "href": child.comboBox.currentText(),
        #                             "title": child.lineEdit.text(),
        #                             "children": serchChildItem(child, level + 1)})
        #     return TOCList

        lastHref = ""
        lastStartTime = QTime(0, 0)
        lastElementIndex = -1
        for i in range(self.ui.listWidget.count()):
            widget = self.ui.listWidget.itemWidget(self.ui.listWidget.item(i))
            level = 0
            if not FORCE and widget.ui.lineEdit_Title.text() == "":
                widget.ui.lineEdit_Title.setEnabled(False)
                self.mask = MaskWidget(self.mainWindow)
                self.mask.show()

                self.alert = Alert(self._translate("TOCListWidget", "Some required fields are empty!"))
                self.alert.close_alert.connect(self.closeAlert)
                self.alert.move(
                    self.mainWindow.geometry().x() +
                    self.mainWindow.geometry().width() / 2 -
                    self.alert.geometry().width() / 2,
                    self.mainWindow.geometry().y() +
                    self.mainWindow.geometry().height() / 2 -
                    self.alert.geometry().height() / 2)

                # self.alert.show()
                self.alert.exec_()
                self.closeAlert()
                return {}

            if not FORCE and widget.ui.timeEdit_Start.time().toString("hh:mm:ss.zzz") != "00:00:00.000":
                startSeconds = widget.ui.timeEdit_Start.time().hour() * 3600 + \
                          widget.ui.timeEdit_Start.time().minute() * 60 + \
                          widget.ui.timeEdit_Start.time().second() + \
                          float(widget.ui.timeEdit_Start.time().msec()) / 1000

                if lastHref != widget.ui.label_Href.text():
                    lastHref = widget.ui.label_Href.text()
                    lastStartTime = widget.ui.timeEdit_Start.time()
                    lastElementIndex = i
                    self._TOCList.append({"level": level,
                                          "href": widget.ui.label_Href.text() +
                                                  "#t=" +
                                                  str(startSeconds),
                                          "title": widget.ui.lineEdit_Title.text(),
                                          "children": []})
                    # widget.setTitle(widget.ui.lineEdit_Title.text())

                else:
                    pos = self._TOCList[lastElementIndex]['href'].find('#t=')
                    if pos == -1:
                        self._TOCList[lastElementIndex] = {"level": self._TOCList[lastElementIndex]['level'],
                                                           "href": self._TOCList[lastElementIndex]['href'] +
                                                                   "#t=0," +
                                                                   str(startSeconds),
                                                           "title": self._TOCList[lastElementIndex]['title'],
                                                           "children": []}
                        lastElementIndex = i
                        lastStartTime = widget.ui.timeEdit_Start.time()
                        self._TOCList.append({"level": level,
                                              "href": widget.ui.label_Href.text() +
                                                      "#t=" +
                                                      str(startSeconds),
                                              "title": widget.ui.lineEdit_Title.text(),
                                              "children": []})

                    else:
                        str_Time = self._TOCList[lastElementIndex].get('href')[pos + 3:]
                        if str_Time.find(',') == -1:  # Not found, only #t=
                            float_Time = float(str_Time)
                            if float_Time < startSeconds:  # Check lastElement
                                self._TOCList[lastElementIndex] = {"level": self._TOCList[lastElementIndex]['level'],
                                                                   "href": self._TOCList[lastElementIndex]['href'] +
                                                                           "," +
                                                                           str(startSeconds),
                                                                   "title": self._TOCList[lastElementIndex]['title'],
                                                                   "children": []}
                                lastElementIndex = i
                                lastStartTime = widget.ui.timeEdit_Start.time()
                                self._TOCList.append({"level": level,
                                                      "href": widget.ui.label_Href.text() +
                                                              "#t=" +
                                                              str(startSeconds),
                                                      "title": widget.ui.lineEdit_Title.text(),
                                                      "children": []})
                            else:  # Don't care, just pass
                                lastElementIndex = i
                                lastStartTime = widget.ui.timeEdit_Start.time()
                                self._TOCList.append({"level": level,
                                                      "href": widget.ui.label_Href.text() +
                                                              "#t=" +
                                                              str(startSeconds),
                                                      "title": widget.ui.lineEdit_Title.text(),
                                                      "children": []})
                                continue
                        else:
                            lastElementIndex = i
                            lastStartTime = widget.ui.timeEdit_Start.time()
                            self._TOCList.append({"level": level,
                                                  "href": widget.ui.label_Href.text() +
                                                          "#t=" +
                                                          str(startSeconds),
                                                  "title": widget.ui.lineEdit_Title.text(),
                                                  "children": []})
                            continue

            else:
                self._TOCList.append({"level": level,
                                      "href": widget.ui.label_Href.text(),
                                      "title": widget.ui.lineEdit_Title.text(),
                                      "children": []})
                lastHref = widget.ui.label_Href.text()
                lastStartTime = QTime(0, 0)
                lastElementIndex = i

        logging.debug(json.dumps(self._TOCList, indent=4, ensure_ascii=False))
        return self._TOCList
            
    def save(self, FORCE=False):
        logging.debug("save in TOCWidget")
        return self.on_traverseTreeAction_triggered(FORCE)

    @Slot(str, str)
    def add_Resource_to_TOC_triggered(self, fullFilename, title):
        logging.debug('TOCListWidget : add_Resource_to_TOC_triggered')
        if self._isEmpty:
            self.ui.widget_NoItem.setVisible(False)
            self.ui.listWidget.setEnabled(True)
            self._isEmpty = False
            
        # self.ui.listWidget.setEnabled(True)   
        
        item = QListWidgetItem()  
        # item.setText(str(self.ui.listWidget.count()))
        item.setSizeHint(self.getItemSize()) 
        
        roi = TOCListWidgetItem(fullFilename, item, self.getSerialNo(), title)
        roi.ui.lineEdit_Title.setText(title)
        
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.setItemWidget(item, roi)
        self._listWidgetItemSerialNo += 1
        self.roiList.append(roi)

    def closeAlert(self):
        self.mask.close()
        for i in range(self.ui.listWidget.count()):
            widget = self.ui.listWidget.itemWidget(self.ui.listWidget.item(i))
            widget.ui.lineEdit_Title.setEnabled(True)

    def changeEvent(self, event):
        """Handle LanguageChange event"""
        if event.type() == QEvent.LanguageChange:
            logging.debug("Language changed")
            for i in range(self.ui.listWidget.count()):
                widget = self.ui.listWidget.itemWidget(self.ui.listWidget.item(i))
                widget.setTitle(widget.getTitle())

            self.ui.retranslateUi(self)

        super().changeEvent(event)

    def afterDrop(self, parent, start, end, destination, row):
        # super(ReadingOrderWidget, self).dropEvent(event)
        logging.debug('afterDrop')
        self._afterDrop = True

    def eventFilter(self, sender, event):
        if sender == self.ui.listWidget and event.type() == QEvent.ChildRemoved:
            logging.debug("eventFilter")

            if not self._afterDrop:
                itemWidget = self.ui.listWidget.itemWidget(self.ui.listWidget.currentItem())
                if itemWidget is None:
                    logging.debug("itemWidget is None")
                    roiList = self.roiList.copy()
                    itemWOWidget = -1
                    for i in range(self.ui.listWidget.count()):
                        item = self.ui.listWidget.item(i)
                        itemWidget = self.ui.listWidget.itemWidget(item)
                        if itemWidget is not None:
                            roiList.remove(itemWidget)
                        else:
                            itemWOWidget = i
                    if len(roiList) == 1:
                        super().eventFilter(sender, event)
                        oldROI = roiList[0]
                        roi = TOCListWidgetItem(oldROI.getFullFilename(),
                                                self.ui.listWidget.item(itemWOWidget),
                                                self.getSerialNo(),
                                                oldROI.getTitle())
                        isEnabled, startTime = oldROI.getTimeStamps()
                        roi.ui.timeEdit_Start.setEnabled(isEnabled)
                        if isEnabled:
                            roi.ui.timeEdit_Start.setTime(startTime)
                        self._listWidgetItemSerialNo += 1
                        self.ui.listWidget.setItemWidget(self.ui.listWidget.item(itemWOWidget), roi)
                        self.roiList.remove(oldROI)
                        self.roiList.append(roi)
                        return True
            else:
                self._afterDrop = False

        return super().eventFilter(sender, event)