#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 13:39
# @Author  : Andrew.chu
# @Site    : Schindler
# @File    : test_Server.py
# @Software: PyCharm
"""
Description:
"""

import socket
import time
import threading

SERVER_PORT = 80
IP = "127.0.0.1"


def tcplink(sock, addr):
    print('new connecting from:', addr)
    i = 1
    while True:
        data = b'\x00\x00\x00' + str(i).encode()
        i += 1
        print(data)
        sock.send(data)
        # print("TaTu send done!")
        time.sleep(1)
        if i > 99:
            i = 0


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((IP, SERVER_PORT))
    s.listen(10)
    print('waiting for connecting...')
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


if __name__ == "__main__":
    main()
