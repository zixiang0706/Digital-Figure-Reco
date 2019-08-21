#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 12:36
# @Author  : Andrew.chu
# @Site    : Schindler
# @File    : _myQLabel.py
# @Software: PyCharm
'''
Description:

'''

from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen
import pickle


class MyQLabel(QLabel):
    def __init__(self, q_gui2camera):
        super(MyQLabel, self).__init__()
        self._q_gui2camera = q_gui2camera
        self._x0 = 0
        self._y0 = 0
        self._w = 0
        self._h = 0
        self._flag = False
        self.load_config()

    def load_config(self):
        try:
            with open("./asset/coordinate.pickle", "rb") as f:
                coor_temp = pickle.load(f)
                print(coor_temp)
                self._q_gui2camera.put(coor_temp)
                self._x0, self._y0, self._w, self._h = coor_temp["coordinate"][:4]
                self.update()
        except Exception as e:
            print(e)
        finally:
            pass

    def mousePressEvent(self, event):
        self._flag = True
        self._x0 = event.x()
        self._y0 = event.y()
        self._w = 1
        self._h = 1

    def mouseReleaseEvent(self, event):
        self._flag = False
        self._q_gui2camera.put({"coordinate": [self._x0, self._y0, self._w, self._h,
                                               self.size().width(), self.size().height()]})

        with open("./asset/coordinate.pickle", "wb") as f:
            pickle.dump({"coordinate": [self._x0, self._y0, self._w, self._h,
                                        self.size().width(), self.size().height()]},
                        f, pickle.HIGHEST_PROTOCOL)

    def mouseMoveEvent(self, event):
        if self._flag:
            self._w = abs(event.x() - self._x0)
            self._h = abs(event.y() - self._y0)
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        rect = QRect(self._x0, self._y0, self._w, self._h)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
        painter.drawRect(rect)