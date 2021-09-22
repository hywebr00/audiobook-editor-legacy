# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:36:14 2021
"""


import logging
from multipledispatch import dispatch

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# from ui_metadatawidget import Ui_MetadataWidget
from ui_metadatawidgetwithscrollarea import Ui_MetadataWidget
from alert import Alert, AlertWithButtons
from translucent import MaskWidget
# import resources_rc


class MetadataWidget(QWidget):
    
    switch_window = Signal()
    # signal_exit = pyqtSignal()
    
    @dispatch(QMainWindow)
    def __init__(self, mainWindow):
        super(MetadataWidget, self).__init__()

        self.mainWindow = mainWindow
        self.ui = Ui_MetadataWidget()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate
        _translate = self._translate

        self._duration = 0.0
        
        currentDate = QDate.currentDate()
        self.ui.dateEdit_DatePublished.setDate(currentDate)
        self.ui.dateEdit_DateModified.setDate(currentDate)

        self.mask = None
        self.alert = None

    @dispatch(QMainWindow, dict)
    def __init__(self, mainWindow, manifestDict):
        super(MetadataWidget, self).__init__()

        self.mainWindow = mainWindow
        self.ui = Ui_MetadataWidget()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate
        
        self._duration = 0.0
        
        currentDate = QDate.currentDate()       
        if manifestDict.get('saveDir') is not None:  # from CreateNewWizard
            self.ui.lineEdit_BookTitle.setText(manifestDict.get("bookTitle"))
        else:
            self.ui.lineEdit_BookTitle.setText(manifestDict.get("name"))

        # self.ui.lineEdit_BookTitle.setReadOnly(True)

        authorDict = manifestDict.get("author", {"type": "Person", "name": ""})
        if isinstance(authorDict, dict):  # New-styled
            author = authorDict.get("name", "")
        else:  # Old-fashioned: str
            author = authorDict
        self.ui.lineEdit_Author.setText(author)

        readByDict = manifestDict.get("readBy", {"type": "Person", "name": ""})
        if isinstance(readByDict, dict):  # New-styled
            readBy = readByDict.get("name", "")
        else:  # Old-fashioned
            readBy = readByDict
        self.ui.lineEdit_ReadBy.setText(readBy)

        self.ui.lineEdit_Publisher.setText(manifestDict.get("publisher", ""))
      
        self.ui.lineEdit_Website.setText(manifestDict.get("url", ""))
        self.ui.lineEdit_Website.setToolTip("<p style=\"color:#FFFFFF\">" + manifestDict.get("url", "") + "</p>")

        self.ui.comboBox_inLanguage.setCurrentText(manifestDict.get("inLanguage", ""))
                
        # print("datePublished =" + manifestDict.get("datePublished", currentDate.toString(Qt.ISODate)))
        try:
            self.ui.dateEdit_DatePublished.setDate(QDate.fromString(manifestDict.get("datePublished",
                                                                                     currentDate.toString(Qt.ISODate)),
                                                                    Qt.ISODate))
        except Exception as ex:
            self.ui.dateEdit_DatePublished.setDate(QDate.fromString(currentDate.toString(Qt.ISODate)))           

        try:
            self.ui.dateEdit_DateModified.setDate(QDate.fromString(manifestDict.get("dateModified",
                                                                                    currentDate.toString(Qt.ISODate)),
                                                                   Qt.ISODate))
        except Exception as ex:
            self.ui.dateEdit_DateModified.setDate(QDate.fromString(currentDate.toString(Qt.ISODate)))          

        self.mask = None
        self.alert = None

        '''
        # Required 
        
        self.ui.lineEdit_name.setText(manifestDict.get("name", ""))
        self.ui.lineEdit_conformsTo.setText(manifestDict.get("conformsTo", ""))
        self.ui.lineEdit_context.setText(str(manifestDict.get("@context", [])))
        
        self.ui.comboBox_abridged.setCurrentText(str(manifestDict.get("abridged", True)))
        self.ui.lineEdit_accessibilityFeature.setText(str(manifestDict.get("accessibilityFeature", [])))
        self.ui.lineEdit_accessibilityHazard.setText(manifestDict.get("accessibilityHazard", ""))
        self.ui.lineEdit_accessibilitySummary.setText(manifestDict.get("accessibilitySummary", ""))
        
        self.ui.comboBox_accessMode.setCurrentData(manifestDict.get("accessMode", []))
        self.ui.lineEdit_accessModeSufficient.setText(str(manifestDict.get("accessModeSufficient", [])))
        self.ui.lineEdit_author.setText(manifestDict.get("author", ""))
        self.ui.lineEdit_cover.setText(manifestDict.get("cover", ""))
        self.ui.lineEdit_duration.setText(manifestDict.get("duration", ""))
        
        print( "dateModified = " + manifestDict.get("dateModified", ""))
        dt = QDateTime.fromString("2020-12-15 22:00:30")
        print( "dateModified = " + dt.toString("yyyy-MM-dd hh:mm:ss"))
        
        self.ui.dateTimeEdit_dateModified.setDateTime(QDateTime.fromString(manifestDict.get("dateModified", "")))
        
        #date = QDate.fromString(manifestDict.get("datePublished", "1900-1-1"), "yyyy-MM-dd")
        
        self.ui.dateEdit_datePublished.setDate(QDate.fromString(manifestDict.get("datePublished", "1900-1-1"), "yyyy-MM-dd"))
        self.ui.lineEdit_id.setText(manifestDict.get("id", ""))
        self.ui.comboBox_inLanguage.setCurrentText(manifestDict.get("inLanguage", "ZH-TW"))
        self.ui.lineEdit_readBy.setText(manifestDict.get("readBy", ""))
        self.ui.comboBox_readingProgression.setCurrentText(manifestDict.get("readingProgression", ""))
        self.ui.lineEdit_type.setText(manifestDict.get("type", "CreativeWork"))
        self.ui.lineEdit_url.setText(manifestDict.get("url", ""))
        '''
        
    def save(self):
        dict_pm = dict()
        
        # Required 
        dict_pm["name"] = self.ui.lineEdit_BookTitle.text()
        dict_pm["conformsTo"] = "https://www.w3.org/TR/audiobooks/"
        dict_pm["@context"] = ["https://schema.org", "https://www.w3.org/ns/pub-context"] 

        # Optional
        '''
        dict_pm["abridged"] = self.ui.comboBox_abridged.currentText()
        
        dict_pm["accessibilityFeature"] = self.ui.lineEdit_accessibilityFeature.text() 
        dict_pm["accessibilityHazard"] = self.ui.lineEdit_accessibilityHazard.text()
        dict_pm["accessibilitySummary"] = self.ui.lineEdit_accessibilitySummary.text()
        dict_pm["accessModeSufficient"] = self.ui.lineEdit_accessModeSufficient.text()
        dict_pm["accessMode"] = self.ui.comboBox_accessMode.currentText()
        '''

        dict_pm["author"] = {"type": "Person", "name": self.ui.lineEdit_Author.text()}

        dict_pm["duration"] = "PT" + "{:.2f}".format(self._duration) + "S"
        
        dict_pm["dateModified"] = self.ui.dateEdit_DateModified.date().toString(Qt.ISODate)
        dict_pm["datePublished"] = self.ui.dateEdit_DatePublished.date().toString(Qt.ISODate)

        dict_pm["inLanguage"] = self.ui.comboBox_inLanguage.currentText()
        dict_pm["readBy"] = {"type": "Person", "name": self.ui.lineEdit_ReadBy.text()}
        dict_pm["publisher"] = self.ui.lineEdit_Publisher.text()
        # dict_pm["readingProgression"] = self.ui.comboBox_readingProgression.currentText()
        dict_pm["type"] = 'Audiobook'
        dict_pm["url"] = self.ui.lineEdit_Website.text()        
        
        """
        if dict_pm["name"] == "" or dict_pm["author"] == "" or dict_pm["readBy"] == "":
            self.alert = Alert(self._translate("MetadataWidget", "Some required fields are empty!"))
            self.alert.show()
            # QMessageBox.information(self, self._translate("MetadataWidget", "Hint!"), self._translate("MetadataWidget", "Some required fields are empty!"), QMessageBox.Ok)
            return {}
        """

        bool_Alert_BookTitle = False
        bool_Alert_Author = False
        bool_Alert_ReadBy = False
        
        if dict_pm["name"] == "":
            self.ui.lineEdit_BookTitle.setEnabled(False)
            bool_Alert_BookTitle = True
        if dict_pm["author"]["name"] == "":
            self.ui.lineEdit_Author.setEnabled(False)
            bool_Alert_Author = True
        if dict_pm["readBy"]["name"] == "":
            self.ui.lineEdit_ReadBy.setEnabled(False)
            bool_Alert_ReadBy = True
        
        if bool_Alert_BookTitle or bool_Alert_Author or bool_Alert_ReadBy:   
            self.mask = MaskWidget(self.mainWindow)
            self.mask.show()            
            
            self.alert = Alert(self._translate("MetadataWidget",
                                               "Some required fields are empty!"))
            # self.alert.close_alert.connect(self.closeAlert)
            self.alert.move(self.mainWindow.geometry().x() +
                            self.mainWindow.geometry().width()/2 -
                            self.alert.geometry().width()/2,
                            self.mainWindow.geometry().y() +
                            self.mainWindow.geometry().height()/2 -
                            self.alert.geometry().height()/2)
            
            # self.alert.show()
            result = self.alert.exec_()
            self.closeAlert()
            return {}
        
        return dict_pm
    
    def onDurationChanged(self, duration):
        logging.debug("onDurationChanged : duration = " +
                      "{:02d}".format(int(duration//3600)) +
                      ":{:02d}".format(int(duration//60)) +
                      ":{:02d}".format(int(duration%60)))
        self._duration = duration
        hr = int(duration//3600)
        mn = int(duration//60) - hr * 60
        self.ui.label_Duration.setText("{:02d}".format(hr) +
                                       ":{:02d}".format(mn) +
                                       ":{:02d}".format(int(duration%60)))
       
    def closeAlert(self):
        self.mask.close()
        self.ui.lineEdit_BookTitle.setEnabled(True)
        self.ui.lineEdit_Author.setEnabled(True)
        self.ui.lineEdit_ReadBy.setEnabled(True)

    def changeEvent(self, event):
        """Handle LanguageChange event"""
        if event.type() == QEvent.LanguageChange:
            logging.debug("Language changed")
            self.ui.retranslateUi(self)

        super().changeEvent(event)

        
        

