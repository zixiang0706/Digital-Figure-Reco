#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 13:13
# @Author  : Andrew.chu
# @Site    : Schindler
# @File    : _myTCP_Client.py
# @Software: PyCharm
"""
Description:

"""
import socket
import re
import time


class TCP(object):
    def __init__(self, **kwargs):
        self.ip = ''
        self.port = ''
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        for key, value in kwargs.items():
            if key == "q_gui2tcp_tatu":
                self.q_gui2tcp_tatu = value
            elif key == "q_tcp_tatu2gui":
                self.q_tcp_tatu2gui = value

    def update_q(self):
        if self.q_gui2tcp_tatu.qsize():
            data_dict = self.q_gui2tcp_tatu.get()
            for key, value in data_dict.items():
                if key == "ip":
                    self.ip, self.port = re.match(r"([\w\.]*)\:(\w*)", value).groups()
        time.sleep(0.01)

    def my_run(self):
        while True:
            if self.ip:
                print("Try to connect TaTu")
                try:
                    self.s.connect((self.ip, int(self.port)))
                    print("Success Connect to Tatu")
                    while True:
                        data = self.s.recv(1024)
                        if data:
                            data = data.strip(b'\x00').decode()
                            self.q_tcp_tatu2gui.put({"tatu": data})
                        else:
                            break
                except Exception as e:
                    print(e)
                    time.sleep(1)
            self.update_q()
            time.sleep(5)


def run_tcp(**kwargs):
    tcp = TCP(**kwargs)
    tcp.my_run()