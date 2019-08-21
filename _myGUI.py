#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 12:37
# @Author  : Andrew.chu
# @Site    : Schindler
# @File    : _myGUI.py
# @Software: PyCharm
"""
Description:
the HMI file.
"""

from _myQLabel import MyQLabel
from _myDialog import DialogTrainingNN
from UI.mainUI import Ui_MainWindow

import sys
import time
import cv2
import os
import pickle
from datetime import datetime

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QInputDialog, QLineEdit
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap, QGuiApplication


class MyWindow(QMainWindow, Ui_MainWindow):
    """
    the class of the GUI
    """

    def __init__(self, **kwargs):
        """
        init the object
        :param kwargs: the queuelist
        """
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.q_list = kwargs
        for key, value in kwargs.items():
            if key == "q_gui2camera":
                self.q_gui2camera = value
            elif key == "q_gui2tcp_tatu":
                self.q_gui2tcp_tatu = value
            elif key == "q_camera2gui":
                self.q_camera2gui = value
            elif key == "q_pre_processing2gui":
                self.q_pre_processing2gui = value
            elif key == "q_cnn2gui":
                self.q_cnn2gui = value
            elif key == "q_tcp_tatu2gui":
                self.q_tcp_tatu2gui = value
        # final_img is the last pic feed to NN, this img can be used to store in file.
        self.final_img = None
        self.test_passed = 0
        self.test_failed = 0

        self.__init_original_img()
        self.__init_slot()

    def __init_slot(self):
        """
        all the slot definition is in here
        :return: None
        """
        # timer used to update the video
        q_timer = QTimer(self)
        q_timer.timeout.connect(self.my_q_update)
        q_timer.start(5)
        # this timer used to set the compare time gap between reco and Tatu
        self.compare_timer = QTimer(self)
        self.compare_timer.timeout.connect(self.delay_compare)
        # Menu action
        self.actionOpen_Log.triggered.connect(self.diaglog_open_log)
        self.actionExit.triggered.connect(self.close)
        self.actionExit.setShortcut("Ctrl+Q")
        self.actionSave_Image.triggered.connect(self.snapshot)
        self.actionSave_Image.setShortcut("Ctrl+S")
        self.actionSave_Log.triggered.connect(self.diaglog_save_log)
        self.actionConfigure.triggered.connect(
            lambda _: QMessageBox.information(self, 'Message', "Done!")
        )
        self.actionre_Training_NN.triggered.connect(self.dialog_training_nn)
        self.actioncollect_images.triggered.connect(
            lambda _: QMessageBox.information(self, 'Message', "Enter Label, then click \"Save Image\" Button")
        )
        self.actionConnect_TaTu.triggered.connect(self.dialog_tatu)
        self.actionMerge_images.triggered.connect(self.merge_final_img)
        # pushButton
        self.pushButton.clicked.connect(self.save_final_img)
        self.pushButton_3.clicked.connect(self.merge_final_img)
        self.pushButton_5.clicked.connect(self.dialog_training_nn)
        # slider
        self.horizontalSlider.valueChanged[int].connect(
            lambda x: self.label_19.setText(str(x))
        )
        self.horizontalSlider.valueChanged[int].connect(
            lambda x: self.q_gui2camera.put({"sample_time": x})
        )

    def __init_original_img(self):
        """
        over-write the original_img to add new feature, like drag rectangle
        :return: None
        """
        self.original_img = MyQLabel(self.q_gui2camera)
        # the rest is same as definition in mainUI.py
        self.original_img.setMinimumSize(QtCore.QSize(456, 353))
        self.original_img.setMaximumSize(QtCore.QSize(456, 353))
        self.original_img.setScaledContents(True)
        self.gridLayout_3.addWidget(self.original_img, 1, 0, 1, 4)
        self.original_img.setCursor(Qt.CrossCursor)

    @staticmethod
    def my_cv2label(cls, img, label):
        """
        set img to the label
        :param cls:
        :param img: img with RGB format
        :param label: set the img to which label
        :return:
        """
        height, width, bytesPerComponent = img.shape
        pixmap = QPixmap.fromImage(QImage(img.data, width, height, 3 * width, QImage.Format_RGB888))
        label.setPixmap(pixmap)

    def dialog_training_nn(self):
        """
        show the dialog window of train NN
        :return:
        """
        training_window = DialogTrainingNN(**self.q_list)
        training_window.exec_()

    def dialog_tatu(self):
        """
        set the TaTu IP and let it TCP threading really run
        :return:
        """
        ip = ''
        try:
            with open("./asset/ip.pickle", "rb") as f:
                ip = pickle.load(f)
        except Exception as e:
            print(e)
        finally:
            ip, okPressed = QInputDialog.getText(self, "Get IP", "IP of Tatu:", QLineEdit.Normal, ip)
            if okPressed and ip != '':
                self.q_gui2tcp_tatu.put({"ip": ip})
                with open("./asset/ip.pickle", "wb") as f:
                    pickle.dump(ip, f)

    def diaglog_open_log(self):
        """
        open log interface
        :return:
        """
        fname = QFileDialog.getOpenFileName(self, 'Any name', './output/log')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textBrowser.append(data)

    def diaglog_save_log(self):
        """
        save log interface
        :return:
        """
        fname = QFileDialog.getSaveFileName(self, "Input Name:", './output/log/', '.txt')
        if fname[0]:
            with open(fname[0] + fname[1], 'w') as f:
                f.write(self.textBrowser.toPlainText())

    def snapshot(self):
        """
        save the snapshot
        :return:
        """
        pqscreen = QGuiApplication.primaryScreen()
        pixmap2 = pqscreen.grabWindow(self.frame.winId())
        name = "./output/snapshot/" + time.ctime().replace(":", ".") + '.png'
        pixmap2.save(name)
        QMessageBox.information(self, 'Message', "Image saved in path: " + name)

    def save_final_img(self):
        try:
            fname = int(self.lineEdit.text())
            if (fname >= 0) and (fname < 100):
                cv2.imwrite('./output/image/{}-{}.png'.format(fname, time.time()), self.final_img)
        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Message', "Enter the Label")
        finally:
            pass

    def merge_final_img(self):
        fname = QFileDialog.getOpenFileName(self, "Delete unwanted Images", './output/image/')
        if fname[0]:
            reply = QMessageBox.question(self, 'Message', "Are you sure to MERGE Images to Database?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                os.system("cp ./output/image/* ./input/dataSet/")
                os.system("rm ./output/image/* ")
                QMessageBox.information(self, 'Message', "Merge Success!!!")
            else:
                QMessageBox.information(self, 'Message', "Abandon Merge.")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def delay_compare(self):
        try:
            if self.original_figure.text() == self.label_7.text():
                self.test_passed += 1
                self.label_12.setNum(self.test_passed)
            else:
                self.test_failed += 1
                self.label_13.setNum(self.test_failed)
        except Exception as e:
            print(e)
        self.compare_timer.stop()

    def my_q_update(self):
        if self.q_camera2gui.qsize():
            img_dic = self.q_camera2gui.get()
            for key, value in img_dic.items():
                if key == "img":
                    self.my_cv2label(MyWindow, value, self.original_img)
                elif key == "crop_img":
                    self.my_cv2label(MyWindow, value, self.label_2)

        if self.q_pre_processing2gui.qsize():
            img_dic = self.q_pre_processing2gui.get()
            for key, value in img_dic.items():
                if key == "thresh_img":
                    self.my_cv2label(MyWindow, value, self.label_3)
                elif key == "erode_img":
                    self.my_cv2label(MyWindow, value, self.label_5)
                elif key == "contour_img":
                    self.my_cv2label(MyWindow, value, self.label_9)
                elif key == "find_string":
                    self.label_7.setText(value)
                    self.reco.setText(value)
                    self.textBrowser.append("{} -->> {}".format(value, datetime.now().strftime("%m-%d %Hh-%Mm-%Ss")))
                    # when the reco number bounce, the failed cnt will increase
                    try:
                        if self.original_figure.text() == self.label_7.text():
                            pass
                        else:
                            if self.original_figure.text() == "N.A.":
                                pass
                            else:
                                self.test_failed += 1
                                self.label_13.setNum(self.test_failed)
                    except Exception as e:
                        print(e)
                elif key == "final_img":
                    self.final_img = value

        if self.q_tcp_tatu2gui.qsize():
            num_dic = self.q_tcp_tatu2gui.get()
            for key, value in num_dic.items():
                if key == "tatu":
                    self.original_figure.setText(value)
                    self.compare_timer.start(100)


def run_gui(**kwargs):
    """
    call this func to run the GUI
    :param kwargs: queue list
    :return: None
    """
    app = QApplication(sys.argv)
    myWin = MyWindow(**kwargs)
    myWin.show()
    sys.exit(app.exec_())
