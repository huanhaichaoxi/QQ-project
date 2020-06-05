#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 16:47
# @Author  : zhang shuai
# @Email   : 310966164@qq.com
# @File    : main.py
# @Software: PyCharm
import sys
from PyQt5 import QtWidgets
from src.UI import loginUI


class Controller:

    __logUI = None

    def __init__(self):
        self.__initWindow()

    def __initWindow(self):
        app = QtWidgets.QApplication(sys.argv)
        self.__logUI = loginUI.loginWindow()
        self.__logUI.setupUi()
        self.__logUI.show()
        sys.exit(app.exec_())


Controller()