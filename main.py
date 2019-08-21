#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 12:36
# @Author  : Andrew.chu
# @Site    : Schindler
# @File    : main.py
# @Software: PyCharm
"""
Description:
the main file
"""

import _myGUI
import _myCamera
import _myTCP_Client

from _myCNN import Net

import queue
from threading import Thread


if __name__ == '__main__':
    # the queue list, for data exchange between threading
    q_dict = {
        "q_gui2camera":             queue.Queue(),
        "q_gui2tcp_tatu":           queue.Queue(),
        "q_camera2gui":             queue.Queue(),
        "q_pre_processing2gui":     queue.Queue(),
        "q_cnn2gui":                queue.Queue(),
        "q_tcp_tatu2gui":           queue.Queue()
    }
    # gui thread, used for HMI, set daemon
    gui_thread = Thread(target=_myGUI.run_gui, args=(),
                        kwargs=q_dict, name="GUI", daemon=True)
    gui_thread.start()
    # camera thread, used for Video capture, set daemon,
    camera_thread = Thread(target=_myCamera.run_camera, args=(),
                           kwargs=q_dict, name="camera", daemon=True)
    camera_thread.start()
    # tcp thread, used for get tatu info, set daemon,
    tcp_thread = Thread(target=_myTCP_Client.run_tcp, args=(),
                        kwargs=q_dict, name="tcp", daemon=True)
    tcp_thread.start()
    # block the main thread, until the gui is finished
    gui_thread.join()






