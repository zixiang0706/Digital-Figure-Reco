#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 12:36
# @Author  : Andrew.chu
# @Site    : Schindler
# @File    : _myPreProcessing.py
# @Software: PyCharm
'''
Description:

'''

import cv2
import numpy as np
import torch
from PIL import Image
from _myCNN import predict
import time

MODEL_PATH = './asset/model1.pkl'


class MyPreProcess(object):
    def __init__(self, q_pre_processing2gui):
        self._q_pre_processing2gui = q_pre_processing2gui
        self.erode_img = None
        self.model_loaded = torch.load(MODEL_PATH)
        self.text = None
        self.text_double_confirm = None

    def blur_img(self, crop_img):
        # median blur to remove the noise point
        img_transformed = cv2.medianBlur(crop_img, 1)
        gray = cv2.cvtColor(img_transformed, cv2.COLOR_BGR2GRAY)
        # use OTSU binary the image
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # !!!!!!
        if thresh[0, 0] != 0:
            thresh = cv2.bitwise_not(thresh, thresh)

        # # use erode to make a detailed img
        # kernel = np.ones((3, 3), np.uint8)
        # self.erode_img = cv2.erode(thresh, kernel, iterations=1)
        self.erode_img = thresh

    def find_contours(self):
        minWidth = 10  # 最小宽度
        minHeight = 10  # 最小高度
        find_char = ''

        # 寻找轮廓
        bimg, contours, hier = cv2.findContours(self.erode_img,
                                                cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_SIMPLE)
        contourList = []

        # contors是按照y的大小来排序的，要按照x排序
        for cnt, contour in enumerate(contours):
            contourList.append(cv2.boundingRect(contour))  # (x, y, w, h)

        contourList.sort(reverse=True)
        digit_cv = None
        for item in contourList:
            (x, y, w, h) = item
            if w < minWidth and h < minHeight:
                # 如果不满足条件就过滤掉
                continue
            # 获取ROI图片
            digit = self.erode_img[y:y + h, x:x + w]
            digit_cv = self.get_standard_digit(digit)

            # 从cv2格式变为image格式
            digit = Image.fromarray(digit_cv)
            # 预测******************
            find_char = str(predict(self.model_loaded, digit)) + find_char

            # 原图绘制方形
            cv2.rectangle(self.erode_img, pt1=(x, y), pt2=(x + w, y + h), color=(200,), thickness=1)

        self._q_pre_processing2gui.put({"contour_img": cv2.cvtColor(self.erode_img, cv2.COLOR_GRAY2RGB)})
        self._q_pre_processing2gui.put({"final_img": digit_cv})

        # only if text is changed, and keep same twice, then send it
        if (self.text != find_char) and (self.text_double_confirm == find_char):
            self._q_pre_processing2gui.put({"find_string": find_char})
            self.text = find_char
        elif self.text != find_char:
            self.text_double_confirm = find_char


    def get_standard_digit(self, img):
        STD_WIDTH = 32  # 标准宽度
        STD_HEIGHT = 64

        height, width = img.shape

        # 判断是否存在长条的1
        new_width = int(width * STD_HEIGHT / height)
        if new_width > STD_WIDTH:
            new_width = STD_WIDTH
        # 以高度为准进行缩放
        resized_num = cv2.resize(img, (new_width, STD_HEIGHT), interpolation=cv2.INTER_NEAREST)
        # 新建画布
        canvas = np.zeros((STD_HEIGHT, STD_WIDTH))
        x = int((STD_WIDTH - new_width) / 2)
        canvas[:, x:x + new_width] = resized_num

        return canvas
