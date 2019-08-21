#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 9:03
# @Author  : Andrew.chu
# @Site    : Schindler
# @File    : _package.py
# @Software: PyCharm
"""
Description:

"""


from PyInstaller.__main__ import run
# -F:打包成一个EXE文件
# -w:不带console输出控制台，window窗体格式
# --paths：依赖包路径
# --icon：图标
# --noupx：不用upx压缩
# --clean：清理掉临时文件

if __name__ == '__main__':
    opts = ['-F', '--paths=C:\\python3.6\\Lib\\site-packages\\PyQt5\\Qt\\plugins',
            '--paths=C:\\python3.6\\Lib\\site-packages\\PyQt5\\Qt\\bin',
            '--clean', 'main.py']

    run(opts)
