#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 12:37
# @Author  : Andrew.chu
# @Site    : Schindler
# @File    : _myCamera.py
# @Software: PyCharm
'''
Description:

'''
import cv2
from _myPreProcessing import MyPreProcess
import _myCNN

import time


class Camera(object):
    def __init__(self, **kwargs):
        self.video = cv2.VideoCapture(0)
        self.video.set(3, 640)
        self.video.set(4, 480)
        self.x, self.y, self.w, self.h = 0, 0, 640, 480
        self.re_training_mark = False
        self.SAMPLE_TIME = 25
        self.predict_cnt = self.SAMPLE_TIME

        for key, value in kwargs.items():
            if key == "q_gui2camera":
                self.q_gui2camera = value
            elif key == "q_camera2gui":
                self.q_camera2gui = value
            elif key == "q_pre_processing2gui":
                self.q_pre_processing2gui = value
            elif key == "q_cnn2gui":
                self.q_cnn2gui = value

    def update_q(self):
        if self.q_gui2camera.qsize():
            data_dict = self.q_gui2camera.get()
            for key, value in data_dict.items():
                if key == "coordinate":
                    self.x, self.y, self.w, self.h, gui_x, gui_y = value
                    self.x, self.w = int(self.x * 640 / gui_x), int(self.w * 640 / gui_x)
                    self.y, self.h = int(self.y * 480 / gui_y), int(self.h * 480 / gui_y)
                elif key == "re_training":
                    self.re_training_mark = True
                    _myCNN.main(q_cnn2gui=self.q_cnn2gui, **value)
                elif key == "sample_time":
                    self.SAMPLE_TIME = value
        time.sleep(0.001)

    def my_run(self):
        preProcessing = MyPreProcess(self.q_pre_processing2gui)
        while True:
            ret, img = self.video.read()
            if (not self.re_training_mark) and (self.predict_cnt == 0):
                self.predict_cnt = self.SAMPLE_TIME
                crop_img = img[self.y:(self.y + self.h), self.x:(self.x + self.w), :]
                preProcessing.blur_img(crop_img)
                preProcessing.find_contours()

                crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
                self.q_camera2gui.put({"crop_img": crop_img})

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.q_camera2gui.put({"img": img})
            self.update_q()
            cv2.waitKey(30)
            self.predict_cnt -= 1


def run_camera(**kwargs):
    camera = Camera(**kwargs)
    camera.my_run()
