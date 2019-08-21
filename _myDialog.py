#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 10:27
# @Author  : Andrew.chu
# @Site    : Schindler
# @File    : _myTrainGUI.py
# @Software: PyCharm
"""
Description:

"""

import re
from UI.trainingUI import Ui_Train

from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.QtCore import QTimer


class DialogTrainingNN(QDialog, Ui_Train):
    """
    show the train window
    """
    def __init__(self, **kwargs):
        super().__init__()
        self.setupUi(self)

        for key, value in kwargs.items():
            if key == "q_gui2camera":
                self.q_gui2camera = value
            elif key == "q_cnn2gui":
                self.q_cnn2gui = value
        self.x = 0
        self.epoches = int(self.lineEdit.text())
        timer = QTimer(self)
        timer.timeout.connect(self.progress_update)
        timer.start(500)
        self.pushButton.clicked.connect(self.start_train)

    def start_train(self):
        self.epoches = int(self.lineEdit.text())
        hyper_data = {"epoches": self.epoches,
                      "learning_rate": float(self.lineEdit_2.text()),
                      "batch_size": int(self.lineEdit_3.text())}
        self.q_gui2camera.put({"re_training": hyper_data})

    def progress_update(self):
        if self.q_cnn2gui.qsize():
            train_dic = self.q_cnn2gui.get()
            for key, value in train_dic.items():
                if key == "train_progress":
                    self.textBrowser.append(value)
                    self.x = int(re.match(r"\w*:\s(\d*)", value).groups()[0])
        self.progressBar.setValue(self.x/(self.epoches-1)*100)
        if self.x >= self.epoches-1:
            QMessageBox.information(self, 'Message', "Train Success, please reboot!!!")
            self.close()

    def closeEvent(self, event):
        if self.x < self.epoches-1:
            print(self.x)
            reply = QMessageBox.question(self, 'Message', "Are you sure to abandon Train???",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

