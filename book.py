# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 07:00:16 2021
"""

import logging
from bs4 import BeautifulSoup
import datetime
import mimetypes
import glob
import json
import os
import re
# import backports.tempfile
from tinytag import TinyTag
from tempfile import NamedTemporaryFile
from multipledispatch import dispatch
import zipfile
import urllib.request
from urllib.request import urlopen
# import io
import shutil

from PySide2.QtCore import *
# from PySide2.QtGui import *
from PySide2.QtWidgets import *

from alert import Alert, AlertWithButtons
from translucent import MaskWidget


class Helper(QObject):

    def __init__(self):
        super().__init__(self)
        logging.debug("Helper.__init__ is called!")

    def __del__(self):
        pass

    @staticmethod
    def getMP3Duration(audioFile):  # audioFile should be a full path or URL
        if audioFile.startswith('http'):

            mp3Contents = urlopen(audioFile).read()
            if mp3Contents is not None:
                # mutagen is under GPL v2
                # inMemoryFile = io.BytesIO(mp3Contents)
                # audio = MP3(inMemoryFile)

                with NamedTemporaryFile(delete=False) as temp:
                    temp.write(mp3Contents)
                    temp.flush()
                    tempFilename = temp.name
                audio = TinyTag.get(tempFilename)
                logging.debug(tempFilename)
                return audio.duration

            else:
                return 0.0
        else:
            # mutagen is under GPL v2
            # audio = MP3(audioFile)
            audio = TinyTag.get(audioFile)
        return audio.duration  # audio.info.length

    @staticmethod
    def summarizeMP3Durations(audioFiles):
        totalDuration = 0.0
        for audioFile in audioFiles:
            totalDuration += Helper.getMP3Duration(audioFile)
        return totalDuration

    @staticmethod
    def checkURLAvailability(url):
        """
        Checks that a given URL is reachable.
        :param url: A URL
        :return type: bool
        """
        try:
            urlopen(url)
            return True
        except urllib.error.URLError:
            return False


class Audiobook(QObject):
    _PEP_OPTION_1 = """<!DOCTYPE html>    
<html>
    <head>
        <title>{}</title>
        <meta charset="utf-8">
{}
        <link rel=\"publication\" href=\"#{}\">
        <script type=\"application/ld+json\" id=\"{}\">
{}
        </script>
    </head>
    <body>
        <nav role=\"doc-toc\">
            <h1>{}</h1>
{}
        </nav>
    </body>
</html>"""

    _PEP_OPTION_2 = """<!DOCTYPE html>    
<html>
    <head>
        <title>{}</title>
        <meta charset="utf-8">
{}
        <link rel=\"publication\" href=\"{}\">
    </head>
    <body>
        <h1>{}</h1>
    </body>
</html>"""

    _TOC_OPTION_2 = """<!DOCTYPE html>    
<html>
    <head>
        <title>Table of Contents</title>
        <meta charset="utf-8">
    </head>
    <body>
        <nav role=\"doc-toc\">
            <h1>{}</h1>
{}
        </nav>
    </body>
</html>"""

    _PEP_OPTION_3 = """<!DOCTYPE html>    
<html>
    <head>
        <title>{}</title>
        <meta charset="utf-8">
{}
        <link rel=\"publication\" href=\"{}\">
    </head>
    <body>
        <nav role=\"doc-toc\">
            <h1>{}</h1>
{}
        </nav>
    </body>
</html>"""

    _TOC_OPTION_4 = """<!DOCTYPE html>    
<html>
    <head>
        <title>Table of Contents</title>
        <meta charset="utf-8">
    </head>
    <body>
        <nav role=\"doc-toc\">
            <h1>{}</h1>
{}
        </nav>
    </body>
</html>"""

    # Singleton Pattern
    _instance = None

    signal_not_W3C_compatible = Signal()

    @staticmethod
    @dispatch(dict)
    def getInstance(dict_New):
        if Audiobook._instance is None:
            Audiobook(dict_New)
        return Audiobook._instance

    @staticmethod
    @dispatch(str)
    def getInstance(item_Open):
        if Audiobook._instance is None:
            Audiobook(item_Open)
        return Audiobook._instance

    @staticmethod
    @dispatch()
    def getInstance():
        if Audiobook._instance is None:
            Audiobook({})
        return Audiobook._instance

    '''
    {"saveDir": saveDir, "bookTitle": bookTitle, "author": author, "publisher": publisher, "readBy": readBy}
    '''

    @dispatch(dict)
    def __init__(self, dict_New):
        super().__init__(None)
        # logging.basicConfig(level=logging.critical, format=LOGGING_FORMAT, datefmt=LOGGING_DATE_FORMAT)
        if Audiobook._instance is not None:
            raise Exception('Only one instance of Book should exist!')
            return

        Audiobook._instance = self
        self._translate = QCoreApplication.translate

        self._id = id(self)
        self._optionNo = 1
        self._loaded = False
        self._dirty = False

        self._PEP_File = ''

        self._CSS_File_List = []

        self._TOC = ''
        self._TOC_File = ''
        self._TOC_List = []

        self._MANIFEST = {}
        self._MANIFEST_File = ''
        # self._MANIFEST_List = []

        self._Reading_Order_List = []

        self._MANIFEST_ID = 'manifest'

        self.is_LPF = False
        # 21 keys
        self.CONST_MANIFEST_KEY_LIST = ['@context',
                                        'conformsTo',
                                        'type',
                                        'id',
                                        'url',
                                        'name',
                                        'author',
                                        'readBy',
                                        'abridged',
                                        'accessMode',
                                        'accessModeSufficient',
                                        'accessibilityFeature',
                                        'accessibilityHazard',
                                        'accessibilitySummary',
                                        'dateModified',
                                        'datePublished',
                                        'inLanguage',
                                        'readingProgression',
                                        'duration',
                                        'readingOrder',
                                        'resources']

        self._BOOK_DIR = dict_New.get("saveDir", "")
        self._Booktitle = dict_New.get("bookTitle", "")

        self._MANIFEST["name"] = dict_New.get("bookTitle", "")
        self._MANIFEST["author"] = dict_New.get("author", "")
        self._MANIFEST["publisher"] = dict_New.get("publisher", "")
        self._MANIFEST["readBy"] = dict_New.get("readBy", "")

        self.settings = QSettings()
        self.recentPackToLPFDirectoryInSettings = self.settings.value('RecentPackToLPFDirectory',
                                                                      QStandardPaths.DocumentsLocation,
                                                                      type=str)

    @dispatch(str)
    def __init__(self, item_Open):
        super().__init__(None)
        logging.debug('@dispatch(str)')
        if Audiobook._instance is not None:
            raise Exception('Only one instance of Book should exist!')
            return

        Audiobook._instance = self
        self._translate = QCoreApplication.translate

        self._id = id(self)

        self._optionNo = 1

        self._loaded = False
        self._dirty = False

        self._PEP_File = ''

        self._CSS_File_List = []

        self._TOC = ''
        self._TOC_File = ''
        self._TOC_List = []

        self._MANIFEST = {}
        self._MANIFEST_File = ''

        # self._Reading_Order_List = []

        self._Booktitle = ''

        self._MANIFEST_ID = 'manifest'

        # 21 keys
        self.CONST_MANIFEST_KEY_LIST = ['@context',
                                        'conformsTo',
                                        'type',
                                        'id',
                                        'url',
                                        'name',
                                        'author',
                                        'readBy',
                                        'abridged',
                                        'accessMode',
                                        'accessModeSufficient',
                                        'accessibilityFeature',
                                        'accessibilityHazard',
                                        'accessibilitySummary',
                                        'dateModified',
                                        'datePublished',
                                        'inLanguage',
                                        'readingProgression',
                                        'duration',
                                        'readingOrder',
                                        'resources']

        self.signal_not_W3C_compatible.connect(self.notW3CCompatible)
        if os.path.isdir(item_Open):
            logging.debug(item_Open + " is a directory")
            self._is_LPF = False
            self._LPF_File = ''
            self._BOOK_DIR = item_Open
            self.openFromDirectory(item_Open)

        elif os.path.isfile(item_Open):
            logging.debug(item_Open + " is a normal file")
            filename, file_extension = os.path.splitext(item_Open)
            if file_extension == '.lpf':
                self._is_LPF = True
                self._LPF_File = item_Open
                self.openFromLPF(item_Open,
                                 QStandardPaths.writableLocation(QStandardPaths.CacheLocation) +
                                 '/' +
                                 QUuid.createUuid().toString())
                self.openFromDirectory(self.BookDir)

        self.settings = QSettings()
        self.recentPackToLPFDirectoryInSettings = self.settings.value('RecentPackToLPFDirectory',
                                                                      QStandardPaths.DocumentsLocation,
                                                                      type=str)

    @property
    def dirty(self):
        return self._dirty

    @dirty.setter
    def dirty(self, value):
        self._dirty = value

    @dirty.deleter
    def dirty(self):
        del self._dirty

    @property
    def loaded(self):
        return self._loaded

    @loaded.setter
    def loaded(self, value):
        self._loaded = value

    @loaded.deleter
    def loaded(self):
        del self._loaded

    @property
    def is_LPF(self):
        return self._is_LPF

    @is_LPF.setter
    def is_LPF(self, value):
        self._is_LPF = value

    @is_LPF.deleter
    def is_LPF(self):
        del self._is_LPF

    def __del__(self):
        if Audiobook._instance is not None:
            logging.debug("Audiobook: del is called!")
            Audiobook._instance = None
        else:
            pass

    def resetToOption_1(self):
        self._optionNo = 1

        self._loaded = False
        self._dirty = False

        self._PEP_File = ''

        self._CSS_File_List = []

        self._TOC = ''
        self._TOC_File = ''
        self._TOC_List = []

        self._MANIFEST = {}
        self._MANIFEST_File = ''

        # self._Reading_Order_List = []

        self._Booktitle = ''

        self._MANIFEST_ID = 'manifest'

        # 21 keys
        self.CONST_MANIFEST_KEY_LIST = ['@context',
                                        'conformsTo',
                                        'type',
                                        'id',
                                        'url',
                                        'name',
                                        'author',
                                        'readBy',
                                        'abridged',
                                        'accessMode',
                                        'accessModeSufficient',
                                        'accessibilityFeature',
                                        'accessibilityHazard',
                                        'accessibilitySummary',
                                        'dateModified',
                                        'datePublished',
                                        'inLanguage',
                                        'readingProgression',
                                        'duration',
                                        'readingOrder',
                                        'resources']

    @Slot()
    def notW3CCompatible(self):
        logging.critical("This is not a W3C Compatible Audiobook!")
        logging.debug("We're going to NEW a book!")
        self.resetToOption_1()

    @property
    def LPFFilename(self):
        return self._LPF_File

    @property
    def BookDir(self):
        return self._BOOK_DIR

    @property
    def ID(self):
        return self._id

    @property
    def ManifestDict(self):
        return self._MANIFEST

    @ManifestDict.setter
    def ManifestDict(self, m):
        self._MANIFEST = m

    @property
    def TOCFile(self):
        return self._TOC_File

    @property
    def TOCList(self):
        return self._TOC_List

    @TOCList.setter
    def TOCList(self, t):
        self._TOC_List = t

    @property
    def CoverDict(self):
        if 'resources' in self.ManifestDict:
            for item in self.ManifestDict["resources"]:
                if item.get("rel") is not None and item.get("rel") == "cover":
                    return item
        return {}

    @CoverDict.setter
    def CoverDict(self, dict_Cover):
        if self._MANIFEST.get("resources", None) is None:
            self._MANIFEST["resources"] = [dict_Cover]
            return

        for i in len(self._MANIFEST["resources"]):
            if self._MANIFEST["resources"][i].get("rel", None) is not None and \
                    self._MANIFEST["resources"][i].get("rel") == "cover":
                self._MANIFEST["resources"].remove(i)
                break
        self._MANIFEST["resources"].append(dict_Cover)

    @property
    def SupplementalList(self):
        slist = []
        if 'resources' in self.ManifestDict:
            for item in self.ManifestDict["resources"]:
                if item.get("rel") is not None and item.get("rel") == "cover":
                    continue
                elif item.get("name") is not None and item.get("name") == "Primary Entry Page":
                    continue
                elif item.get("rel") is not None and item.get("rel") == "contents" and \
                        item.get("url") is not None and item.get("url") == "index.html":
                    continue
                elif item.get("name") is not None and item.get("name") == "Table of Contents":
                    continue
                else:
                    slist.append(item)

        return slist

    @SupplementalList.setter
    def SupplementalList(self, sList):
        if self._MANIFEST.get("resources", None) is None:
            self._MANIFEST["resources"] = sList
            return

        for s in sList:
            self._MANIFEST["resources"].append(s)

    @property
    def ReadingOrderList(self):
        if 'readingOrder' in self.ManifestDict:
            return self.ManifestDict['readingOrder']

        return []

    @ReadingOrderList.setter
    def ReadingOrderList(self, rList):
        self._MANIFEST["readingOrder"] = rList

    def on_action_Pack_triggered(self, mainWindow):
        logging.debug("Save as a LPF file!")
        fdlg = QFileDialog()
        fdlg.setFileMode(QFileDialog.AnyFile)
        self.recentPackToLPFDirectoryInSettings = self.settings.value('RecentPackToLPFDirectory',
                                                                      QStandardPaths.writableLocation(
                                                                          QStandardPaths.DocumentsLocation),
                                                                      type=str)
        saveLPFName, _ = fdlg.getSaveFileName(None,
                                              self._translate('Book', 'Save As Audiobook(lpf)'),
                                              self.recentPackToLPFDirectoryInSettings,
                                              self._translate('Book', 'Audiobooks (*.lpf)'))
        if saveLPFName:
            logging.debug(saveLPFName)
            if os.path.split(saveLPFName)[0] != self.recentPackToLPFDirectoryInSettings:
                self.settings.setValue('RecentPackToLPFDirectory',
                                       os.path.split(saveLPFName)[0])
            self.saveAsLPF(saveLPFName, mainWindow)
            return

    def _openAlertWindow(self, str_Msg, str_Title, bgWindow):
        self.mask = MaskWidget(bgWindow)
        self.mask.show()

        self.alert = Alert(str_Msg,
                           str_Title)
        self.alert.move(
            bgWindow.geometry().x() +
            bgWindow.geometry().width() / 2 -
            self.alert.geometry().width() / 2,
            bgWindow.geometry().y() +
            bgWindow.geometry().height() / 2 -
            self.alert.geometry().height() / 2)

        result = self.alert.exec_()
        self.mask.close()
        return result

    def saveAsLPF(self, lpf_file, bgWindow=None):
        filesToBePacked = set()

        def addFilesToBePacked(data):
            # data = self.TOCList
            for i in range(len(data)):
                tocDict = data[i]
                level = tocDict["level"]
                href = tocDict["href"]
                if not href.startswith('http'):
                    pos = href.find('#t=')
                    if pos == -1:
                        filesToBePacked.add(href)
                    else:
                        filesToBePacked.add(href[0:pos])
                addFilesToBePacked(data[i]['children'])

        data = self.TOCList
        addFilesToBePacked(data)

        for i in range(len(self._MANIFEST["readingOrder"])):
            if self._MANIFEST["readingOrder"][i].get("url", None) is not None and \
                    not self._MANIFEST["readingOrder"][i].get("url", None).startswith('http'):
                file = self._MANIFEST["readingOrder"][i].get("url", None)
                filesToBePacked.add(file)

        for i in range(len(self._MANIFEST["resources"])):
            if self._MANIFEST["resources"][i].get("url", None) is not None and \
                    not self._MANIFEST["resources"][i].get("url", None).startswith('http'):
                file = self._MANIFEST["resources"][i].get("url", None)
                filesToBePacked.add(file)

        for css in self._CSS_File_List:
            if not css.startswith('http'):
                file = css
                filesToBePacked.add(file)

        if not self._MANIFEST_File == '':
            filesToBePacked.add(self._MANIFEST_File)

        filesToBePacked = set(filesToBePacked)
        save_zip_file = zipfile.ZipFile(lpf_file, mode='w')
        for f in filesToBePacked:
            logging.debug(os.path.join(self.BookDir, f).replace('\\', '/'))
            if os.path.join(self.BookDir, f).replace('\\', '/') == lpf_file:
                continue

            mime, _ = mimetypes.guess_type(os.path.join(self.BookDir, f).replace('\\', '/'))

            if mime is None or (not mime.startswith("audio") and not mime.startswith("video")):
                save_zip_file.write(os.path.join(self.BookDir, f).replace('\\', '/'), f,
                                    compress_type=zipfile.ZIP_DEFLATED)
            else:
                save_zip_file.write(os.path.join(self.BookDir, f).replace('\\', '/'), f,
                                    compress_type=zipfile.ZIP_STORED)

        save_zip_file.close()
        if bgWindow is not None:
            self._openAlertWindow(self._translate("Book", "Packing is finished!"),
                                  self._translate("Book", "Information"),
                                  bgWindow)

    def getLPFInfo(self, lpf_file):
        zf = zipfile.ZipFile(lpf_file)
        for info in zf.infolist():
            logging.debug(info.filename)
            logging.debug('\tComment:\t', info.comment)
            logging.debug('\tModified:\t', datetime.datetime(*info.date_time))
            logging.debug('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
            logging.debug('\tZIP version:\t', info.create_version)
            logging.debug('\tCompressed:\t', info.compress_size, 'bytes')
            logging.debug('\tUncompressed:\t', info.file_size, 'bytes')

    @Slot()
    def on_action_Save_Audiobook_triggered(self):
        logging.debug("on_action_Save_Audiobook_triggered")
        self.saveIntoDirectory(self.BookDir)
        if self.is_LPF:
            logging.debug("Save as a LPF file!")
            self.saveAsLPF(self._LPF_File)

    def checkResources(self):
        errorList = []
        for resource in self._MANIFEST['resources']:
            if 'url' in resource.keys():
                logging.debug(resource['url'])
                url = resource['url']
                m = re.search(r'^https?://', url)
                if m:  # http(s)://
                    res = Helper.checkURLAvailability(url)
                    logging.debug(res)
                    if not res:
                        errorList.append(url)
                else:  # local
                    logging.debug('not a URL')
                    directory = self._BOOK_DIR
                    if os.path.exists(os.path.join(directory, url)):
                        logging.debug('{} exists'.format(os.path.join(directory, url)))
                    else:
                        logging.debug('{} doesn\'t exist'.format(os.path.join(directory, url)))
                        errorList.append(os.path.join(directory, url))

        return errorList

    def saveIntoDirectory(self, directory=None):
        def getTOCBlock(data, level=0):
            fullTOCString = '\t' * (3 + level * 2) + "<ol>\n"
            for i in range(len(data)):
                dict_TOC = data[i]
                lvl = dict_TOC["level"]
                href = dict_TOC["href"]
                title = dict_TOC["title"]
                fullTOCString += '\t' * (3 + level * 2 + 1) + \
                                 '<li><a href=\"' + \
                                 href + '\">' + \
                                 title + \
                                 '</a></li>\n'
                if len(dict_TOC["children"]) > 0:
                    fullTOCString += getTOCBlock(dict_TOC["children"], level + 1)
                else:
                    pass

            fullTOCString += '\t' * (3 + level * 2) + "</ol>"
            return fullTOCString

        logging.debug('saveIntoDirectory')
        errorList = self.checkResources()
        if not errorList:
            logging.debug('Resources check passed')
        else:
            logging.debug('Not-found list : {}'.format(errorList))
        if directory is None:
            directory = self._BOOK_DIR

        if self._optionNo == 1:  # self._PEP_File and not self._TOC_File and not self._MANIFEST_File
            logging.debug("self._optionNo = 1")
            fullManifestContent = ""
            data = self.TOCList
            tocString = getTOCBlock(data, 0)

            metadata = self.ManifestDict

            """
            <meta name=\"stylesheet\" src=\"{}\">
            """
            fullCSSContent = ""
            for css in self._CSS_File_List:
                fullCSSContent += '<meta name=\"stylesheet\" src=\"{}\">'.format(css)

            if self._MANIFEST.get("resources", "") == "":
                raise Exception("Packing Error: It seems not saved!")

            self._MANIFEST["resources"].append({"url": "index.html",
                                                "encodingFormat": "text/html",
                                                "name": "Primary Entry Page",
                                                "rel": "contents"})

            fullHTMLContent = self._PEP_OPTION_1.format(self._Booktitle if self._Booktitle else self._MANIFEST['name'],
                                                        fullCSSContent,
                                                        self._MANIFEST_ID,
                                                        self._MANIFEST_ID,
                                                        json.dumps(self._MANIFEST, indent=4, ensure_ascii=False),
                                                        self._Booktitle if self._Booktitle else self._MANIFEST['name'],
                                                        tocString)
            logging.debug(fullHTMLContent)
            with open(directory + "/" + "index.html", "w", encoding="utf-8") as f:
                # contents to be grabbed
                f.write(fullHTMLContent)

        elif self._optionNo == 2:
            logging.debug("self._optionNo = 2")

            # fullManifestContent = ""
            fullCSSContent = ""
            for css in self._CSS_File_List:
                fullCSSContent += '<meta name=\"stylesheet\" src=\"{}\">'.format(css)
            fullPEPContent = self._PEP_OPTION_2.format(self._Booktitle,
                                                       fullCSSContent,
                                                       self._MANIFEST_File,
                                                       self._Booktitle)

            with open(directory + "/" + "index.html", "w", encoding="utf-8") as f:
                f.write(fullPEPContent)

            data = self.TOCList
            tocString = getTOCBlock(data, 0)

            fullTOCContent = self._TOC_OPTION_2.format(self._Booktitle,
                                                       tocString)

            with open(directory + "/" + self._TOC_File, "w", encoding="utf-8") as f:
                f.write(fullTOCContent)

            self._MANIFEST["resources"].append({"type": "LinkedResource",
                                                "encodingFormat": "text/html",
                                                "name": "Table of Contents",
                                                "rel": "contents",
                                                "url": self.TOCFile or "toc.html"})
            self._MANIFEST["resources"].append({"url": "index.html",
                                                "encodingFormat": "text/html",
                                                "name": "Primary Entry Page",
                                                "rel": "contents"})
            with open(directory + "/" + self._MANIFEST_File, "w", encoding="utf-8") as f:
                json.dump(self._MANIFEST, f, indent=4, ensure_ascii=False)

        elif self._optionNo == 3:
            logging.debug("self._optionNo = 3")
            data = self.TOCList
            tocString = getTOCBlock(data, 0)

            # fullPEPContent = ""
            fullCSSContent = ""
            for css in self._CSS_File_List:
                fullCSSContent += '<meta name=\"stylesheet\" src=\"{}\">'.format(css)
            fullPEPContent = self._PEP_OPTION_3.format(self._Booktitle,
                                                       fullCSSContent,
                                                       self._MANIFEST_File,
                                                       self._Booktitle,
                                                       tocString)

            with open(directory + "/" + "index.html", "w", encoding="utf-8") as f:
                f.write(fullPEPContent)

            self._MANIFEST["resources"].append({"url": "index.html",
                                                "encodingFormat": "text/html",
                                                "name": "Primary Entry Page",
                                                "rel": "contents"})
            with open(directory + "/" + self._MANIFEST_File, "w", encoding="utf-8") as f:
                json.dump(self._MANIFEST, f, indent=4, ensure_ascii=False)

        elif self._optionNo == 4:
            logging.debug("self._optionNo = 4")

            data = self.TOCList
            tocString = getTOCBlock(data, 0)

            fullTOCContent = self._TOC_OPTION_4.format(self._Booktitle,
                                                       tocString)

            with open(directory + "/" + self._TOC_File, "w", encoding="utf-8") as f:
                f.write(fullTOCContent)

            self._MANIFEST["resources"].append({"type": "LinkedResource",
                                                "encodingFormat": "text/html",
                                                "name": "Table of Contents",
                                                "rel": "contents",
                                                "url": self.TOCFile or "toc.html"})
            with open(directory + "/" + self._MANIFEST_File, "w", encoding="utf-8") as f:
                json.dump(self._MANIFEST, f, indent=4, ensure_ascii=False)

        elif self._optionNo == 5:
            logging.debug("self._optionNo = 5")

            with open(directory + "/" + self._MANIFEST_File, "w", encoding="utf-8") as f:
                json.dump(self._MANIFEST, f, indent=4, ensure_ascii=False)

        else:
            logging.debug("self._optionNo = ???")

        if self.dirty:
            self.dirty = False

    def checkResources(self):
        errorList = []
        for resource in self._MANIFEST.get('resources', []):
            if 'url' in resource.keys():
                logging.debug(resource['url'])
                url = resource['url']
                m = re.search(r'^https?://', url)
                if m:  # http(s)://
                    res = self.helper.checkURLAvailability(url)
                    logging.debug(res)
                    if not res:
                        errorList.append(url)
                else:  # local
                    logging.debug('not a URL')
                    directory = self._BOOK_DIR
                    if os.path.exists(directory + "/" + url):
                        logging.debug('{} exists'.format(directory + "/" + url))
                    else:
                        logging.debug('{} doesn\'t exist'.format(directory + "/" + url))
                        errorList.append(directory + "/" + url)
        return errorList

    def determineOption(self):
        s = set()
        if self._PEP_File and not self._TOC_File and not self._MANIFEST_File:
            self._optionNo = 1
            s.add(self._PEP_File)
        elif self._PEP_File and self._TOC_File and self._MANIFEST_File:
            self._optionNo = 2
            s.add(self._PEP_File)
            s.add(self._TOC_File)
            s.add(self._MANIFEST_File)
        elif self._PEP_File and not self._TOC_File and self._MANIFEST_File:
            self._optionNo = 3
            s.add(self._PEP_File)
            s.add(self._MANIFEST_File)
        elif not self._PEP_File and self._TOC_File and self._MANIFEST_File:
            self._optionNo = 4
            s.add(self._TOC_File)
            s.add(self._MANIFEST_File)
        elif not self._PEP_File and not self._TOC_File and self._MANIFEST_File:
            self._optionNo = 5
        return self._optionNo, s

    def setOptionAndFilenames(self, opt_No, pep_file, toc_file, manifest_file):
        logging.debug("New an audiobook")
        self._optionNo = opt_No
        self._PEP_File = pep_file
        self._TOC_File = toc_file
        self._MANIFEST_File = manifest_file

    def openFromLPF(self, lpf_file, unzip_destination):
        """
        self.__is_LPF = False
        self.__LPF_File = ""
        self.__BOOK_DIR = ""
        """
        logging.debug('openFromLPF with destination = ' + unzip_destination)

        try:
            unzip_files = zipfile.ZipFile(lpf_file, mode='r', compression=zipfile.ZIP_DEFLATED)
            logging.debug(unzip_files)
            for f in unzip_files.namelist():
                logging.debug(f)

            unzip_files.extractall(unzip_destination)
            unzip_files.close()
        except Exception as ex:
            logging.error('Sorry, we failed to unzip this lpf file!')
            return False

        self._is_LPF = True
        self._LPF_File = lpf_file
        lpf_directory, lpf_filename = os.path.split(lpf_file)
        logging.debug(lpf_filename[:-4])
        self._BOOK_DIR = unzip_destination  # + '/' + lpf_filename[:-4]
        logging.debug("self._BOOK_DIR = " + self._BOOK_DIR)
        return True

    def openFromDirectory(self, directory):

        def parseTOC():
            tocFlag = False
            resources = self._MANIFEST.get("resources", None)
            for resource in resources:
                logging.debug(resource.keys())

                if "rel" in resource.keys() and resource["rel"] == "contents":
                    logging.debug(resource['url'])
                    tocSoup = BeautifulSoup(open(os.path.join(directory, resource["url"]), encoding="utf-8"),
                                            features='html5lib')
                    toc = tocSoup.select_one('[role="doc-toc"]')  # eg. <nav role="doc-toc">
                    if toc:
                        logging.debug("TOC ===\n" + "*" * 70 + "\n" + toc.get_text())
                        self._TOC = toc
                        self._TOC_File = resource["url"]
                        logging.debug(self._TOC_File)

                        ol = toc.find('ol', recursive=False)
                        ul = toc.find('ul', recursive=False)
                        if ol:
                            self._TOC_List = dictify(ol, 0)
                        elif ul:
                            self._TOC_List = dictify(ul, 0, tagName="ul")
                        logging.debug("dictify ===\n" + "*" * 70 + "\n" + json.dumps(self._TOC_List,
                                                                                     indent=4,
                                                                                     ensure_ascii=False))

                        tocFlag = True
                        break
            return tocFlag

        def dictify(ol, level, tagName="ol"):
            childrenList = []
            lvl = level

            for li in ol.find_all("li", recursive=False):
                result = {}
                a_tag = li.find('a', recursive=False)

                result['level'] = lvl
                result['href'] = a_tag['href']
                result['title'] = a_tag.get_text()

                next_ol = li.find(tagName, recursive=False)
                if next_ol:
                    result['children'] = dictify(next_ol, lvl + 1)
                else:
                    result['children'] = []
                childrenList.append(result)
            return childrenList

        logging.debug('openFromDirectory')
        if os.path.exists(directory + "/index.html"):
            logging.debug("\"index.html\" exists: PEP is available!\n" + "*" * 70)
            self._PEP_File = "index.html"

            soup = BeautifulSoup(open(directory + r"/index.html", encoding="utf-8"),
                                 features='html5lib')  # html5lib html.parser
            link = soup.select_one('link[rel=\"publication\"]')
            if link:
                href = link.attrs["href"]
                matchInternalID = re.match('^#(\w+)', href)
                if matchInternalID:
                    logging.debug(matchInternalID.group(1))
                    manifest = soup.select_one('script[id=\"' + matchInternalID.group(1) + '\"]')
                    if manifest:  # <script type="application/ld+json" id="XXX">
                        if manifest.attrs["type"] == "application/ld+json":
                            self._MANIFEST = json.loads(manifest.string)
                            # self.__MANIFEST_File = "index.html"
                            logging.debug('MANIFEST ===\n ' + '*' * 70 + '\n' + json.dumps(self._MANIFEST, indent=4,
                                                                                           ensure_ascii=False))

                else:
                    matchExternalJson = re.match('(\w+\.json$)', href)
                    if matchExternalJson:
                        logging.debug(matchExternalJson.group(1))
                        if not os.path.exists(os.path.join(directory, href)):
                            json_files = glob.glob(os.path.join(directory, '*.json'))
                            href = json_files[0].replace(directory + "/", "")
                        self._MANIFEST_File = href
                        fo = open(os.path.join(directory, href),
                                  mode='r',
                                  encoding="utf-8")
                        logging.debug("fo.name = " + fo.name)
                        manifestStr = fo.read()
                        # print("manifestStr = ", "*" * 70, "\n", manifestStr)
                        fo.close()
                        self._MANIFEST = json.loads(manifestStr)
                        logging.debug("MANIFEST ===\n" + "*" * 70 + "\n" + json.dumps(self._MANIFEST, indent=4))

            csses = soup.select('head > link[rel=\"stylesheet\"]')
            if csses:
                for css in csses:
                    href = css.attrs["href"]
                    # css.attrs["href"] = "css/mycss.css"
                    self._CSS_File_List.append(href)
                logging.debug(self._CSS_File_List)

            csses = soup.select('head > [name=\"stylesheet\"]')
            if csses:
                for css in csses:
                    src = css.attrs["src"]
                    self._CSS_File_List.append(src)
                logging.debug(self._CSS_File_List)

            booktitle = soup.select_one('head > title')
            if booktitle and booktitle.text:
                logging.debug(booktitle.text)
                self._Booktitle = booktitle.text
                # self._MANIFEST['name'] = booktitle.text
            else:
                self._Booktitle = self._MANIFEST['name']

            toc = soup.select_one('[role="doc-toc"]')  # <XXX role="doc-toc"> XXX is usually 'nav'
            if toc:
                logging.debug('toc.name =' + toc.name)
                self._TOC = toc

                ol = toc.find('ol', recursive=False)
                ul = toc.find('ul', recursive=False)
                if ol:
                    self._TOC_List = dictify(ol, 0)
                elif ul:
                    self._TOC_List = dictify(ul, 0, tagName='ul')
                logging.debug(
                    'dictify ===\n' + '*' * 70 + '\n' + json.dumps(self._TOC_List, indent=4, ensure_ascii=False))

            else:
                logging.debug("Try to find 'nav' in other .html files.")
                tocFlag = False
                """
                The algorithm here needs to be fixed.
                Old style: parse other html files directly
                Correct(New) style: 
                """
                tocFlag = parseTOC()
                # resources = self._MANIFEST.get("resources", None)
                # if resources:
                #     for resource in resources:
                #         logging.debug(resource.keys())
                #
                #         if "rel" in resource.keys() and resource["rel"] == "contents":
                #             tocFlag = False
                #             logging.debug(resource['url'])
                #             tocSoup = BeautifulSoup(open(directory + "/" + resource["url"], encoding="utf-8"),
                #                                     features='html5lib')
                #             toc = tocSoup.select_one('[role="doc-toc"]')  # eg. <nav role="doc-toc">
                #             if toc:
                #                 logging.debug("TOC ===\n" + "*" * 70 + "\n" + toc.get_text())
                #                 self._TOC = toc
                #                 self._TOC_File = resource["url"]
                #                 logging.debug(self._TOC_File)
                #
                #                 ol = toc.find('ol', recursive=False)
                #                 ul = toc.find('ul', recursive=False)
                #                 if ol:
                #                     self._TOC_List = dictify(ol, 0)
                #                 elif ul:
                #                     self._TOC_List = dictify(ul, 0, tagName="ul")
                #                 logging.debug("dictify ===\n" + "*" * 70 + "\n" + json.dumps(self._TOC_List,
                #                                                                              indent=4,
                #                                                                              ensure_ascii=False))
                #
                #                 tocFlag = True
                #                 break

        elif os.path.exists(directory + "/publication.json"):
            """
            The algorithm here needs to be fixed.
            Old style: parse other html files to find toc first
            Correct(New) style: no index.html, then publication.json must appear
            """
            logging.debug("\"publication.json\" exists: PEP isn't available!\n" + "*" * 70)
            with open(directory + "/publication.json", encoding="utf-8") as manifest_file:
                self._MANIFEST = json.load(manifest_file)
                self._MANIFEST_File = "publication.json"
                logging.debug("MANIFEST ===\n" +
                              "*" * 70 +
                              "\n" +
                              json.dumps(self._MANIFEST, indent=4, ensure_ascii=False))

            tocFlag = parseTOC()
            # resources = self._MANIFEST.get("resources", None)
            # if resources:
            #     for resource in resources:
            #         logging.debug(resource.keys())
            #
            #         if "rel" in resource.keys() and resource["rel"] == "contents":
            #             logging.debug(resource['url'])
            #             tocSoup = BeautifulSoup(open(directory + "/" + resource["url"], encoding="utf-8"),
            #                                     features='html5lib')
            #             toc = tocSoup.select_one('[role="doc-toc"]')  # eg. <nav role="doc-toc">
            #             if toc:
            #                 logging.debug("TOC ===\n" + "*" * 70 + "\n" + toc.get_text())
            #                 self._TOC = toc
            #                 self._TOC_File = resource["url"]
            #                 logging.debug(self._TOC_File)
            #
            #                 ol = toc.find('ol', recursive=False)
            #                 ul = toc.find('ul', recursive=False)
            #                 if ol:
            #                     self._TOC_List = dictify(ol, 0)
            #                 elif ul:
            #                     self._TOC_List = dictify(ul, 0, tagName="ul")
            #                 logging.debug("dictify ===\n" + "*" * 70 + "\n" + json.dumps(self._TOC_List,
            #                                                                              indent=4,
            #                                                                              ensure_ascii=False))
            #
            #                 tocFlag = True
            #                 break

        else:  # Not following the W3C rules
            # Search any .html file in Book directory seems like a good try
            # htmls = glob.glob(directory + "/*.html")
            logging.critical("Fatal error!")
            self.signal_not_W3C_compatible.emit()
            return

        if self._TOC or self._MANIFEST:
            self.loaded = True
            self.determineOption()
            logging.debug(self._optionNo)

            # For Test
            self.dirty = True

    def getCheckSet(self, mainWindow):
        option, list_compulsory = self.determineOption()
        url_compulsory = [self.BookDir + '/' + f
                          for f in list_compulsory
                          if not f.startswith('http')]
        url_orderingOrder = [self.BookDir + '/' + f["url"]
                             for f in mainWindow.readingOrderWidget.save()
                             if not f["url"].startswith('http')]
        url_toc = [self.BookDir + '/' + f["href"]
                   for f in mainWindow.tocWidget.save(True)
                   if not f["href"].startswith('http')]
        url_cover = [self.BookDir + '/' + f["url"]
                     for f in [mainWindow.coverPreviewWidget.save()]
                     if not f["url"].startswith('http')]
        url_supplemental = [self.BookDir + '/' + f["url"]
                            for f in mainWindow.supplementalListWidget.save()
                            if not f["url"].startswith('http')]
        set_url = set(url_compulsory +
                      url_orderingOrder +
                      url_toc +
                      url_cover +
                      url_supplemental)

        return set_url

    def checkAttachedFile(self, filenames, checkSet, cls, instance):
        for filename in filenames:
            file_folder, file_name = os.path.split(filename)

            if filename in checkSet:
                logging.debug("You have chosen one file already in this audiobook")
                continue

            elif self.BookDir + '/' + file_name in checkSet:
                logging.debug("One file with the same name is already in this audiobook")
                try:
                    shutil.copyfile(filename, self.BookDir + '/' + file_name)
                    filename = self.BookDir + '/' + file_name
                except Exception as ex:
                    logging.critical(ex)
                    continue
            elif file_folder == self.BookDir:
                pass
            else:
                pass

            cls.str_LastOpenedDirectory = file_folder

            src = QFile(filename)
            # info = QFileInfo(filename)
            if file_folder != self.BookDir:
                try:
                    shutil.copyfile(filename, self.BookDir + '/' + file_name)
                    filename = self.BookDir + '/' + file_name
                except Exception as ex:
                    logging.critical(ex)
                    continue
            else:
                filename = self.BookDir + '/' + file_name

            mime, _ = mimetypes.guess_type(filename, strict=False)

            if mime is None:
                logging.warning('Cannot guess file type!')
            else:
                logging.debug('File MIME type: %s' % mime)

            instance.addItems(filename, 1)

