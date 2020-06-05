#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 10:22
# @Author  : zhang shuai
# @Email   : 310966164@qq.com
# @File    : loginUI.py
# @Software: PyCharm
import sys
import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication


class loginWindow(QtWidgets.QWidget):
    def setupUi(self):
        self.setObjectName("登录QQ")
        self.resize(420, 330)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(50, 150, 331, 101))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(50, 30))
        self.label.setMaximumSize(QtCore.QSize(50, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.idEdit = QtWidgets.QLineEdit(self.widget)
        self.idEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.idEdit.setMaximumSize(QtCore.QSize(180, 30))
        self.idEdit.setObjectName("idEdit")
        self.gridLayout.addWidget(self.idEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(50, 30))
        self.label_2.setMaximumSize(QtCore.QSize(50, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.passwordEdit = QtWidgets.QLineEdit(self.widget)
        self.passwordEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.passwordEdit.setMaximumSize(QtCore.QSize(180, 30))
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout.addWidget(self.passwordEdit, 1, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self)
        self.widget1.setGeometry(QtCore.QRect(70, 260, 271, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginBtn = QtWidgets.QPushButton(self.widget1)
        self.loginBtn.setMaximumSize(QtCore.QSize(80, 35))
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout.addWidget(self.loginBtn)
        self.signupBtn = QtWidgets.QPushButton(self.widget1)
        self.signupBtn.setMaximumSize(QtCore.QSize(80, 35))
        self.signupBtn.setObjectName("signupBtn")
        self.horizontalLayout.addWidget(self.signupBtn)

        self.setBackground()
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录QQ"))
        self.label.setText(_translate("Form", "QQ号："))
        self.label_2.setText(_translate("Form", "密码："))
        self.loginBtn.setText(_translate("Form", "登录"))
        self.signupBtn.setText(_translate("Form", "注册"))

    # 设置登录界面背景
    def setBackground(self):
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap('../../source/login.jpg')))
        self.setPalette(palette)
