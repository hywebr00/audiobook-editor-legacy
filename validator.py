# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:08:11 2021
"""


import logging
import sys
import json
import jsonschema
import os


from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *

from alert import Alert
# from translucent import MaskWidget


class Validator(Alert):

    class WorkThread(QThread):
        setText = Signal(str)

        def __int__(self):
            super(Validator.WorkThread, self).__init__()
            self.schema = None
            self.jsonObj = None
            self.text = ''

        def setWork(self, schema, jsonObject):
            self.schema = schema
            self.jsonObj = jsonObject
            self.text = ''
            self._translate = QCoreApplication.translate

        def run(self):
            try:
                jsonschema.validate(instance=self.jsonObj, schema=self.schema)
                self.text += self._translate('Validator', 'Validation succeeded!')
                self.setText.emit(self.text)
                logging.debug('validation passed')
            except jsonschema.ValidationError:
                self.text += self._translate('Validator', 'Validation error')
                self.setText.emit(self.text)
                logging.debug('validation error')
            except jsonschema.SchemaError:
                self.text += self._translate('Validator', 'Schema error')
                self.setText.emit(self.text)
                logging.debug('Schema error')

    def __init__(self, msg, title, instance_schema, instance_json):
        super().__init__(msg, title)

        self.flag_Finish = False

        # self._validate('schema-example.json', {'name': 'Skyrookie', 'price': 100})
        self.timer = QTimer(self)
        self.text = msg
        self.times = -1
        self._translate = QCoreApplication.translate

        self.ui.pushButton_Ok.setVisible(False)  # .clicked.connect(self.accept)
        self.ui.toolButton_Close.setVisible(False)  # .clicked.connect(self.reject)

        self.work = self.WorkThread()
        self.work.setWork(instance_schema, instance_json)
        self.work.setText.connect(self.setText)
        self._validate()
        self.work.start()

    def _validate(self):
        logging.debug('start to validate')
        self.timer.timeout.connect(self.run)
        self.times = 0
        self.timer.start(300)

    def run(self):
        logging.debug('run')

        self.times += 1
        self.text = self.text + '.'
        self.ui.label_Msg.setText(self.text)

    def setText(self, text):
        logging.debug('setText')
        self.timer.stop()
        self.text = self.text + '\n' + text
        self.ui.label_Msg.setText(self.text)
        self.ui.pushButton_Ok.setVisible(True)
        self.ui.toolButton_Close.setVisible(True)




