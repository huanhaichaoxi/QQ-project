#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 10:22
# @Author  : zhang shuai
# @Email   : 310966164@qq.com
# @File    : loginUI.py
# @Software: PyCharm
import sys
import time

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication


class loginWindow(QtWidgets.QWidget):
    def setupUi(self):
        self.setObjectName("登录QQ")
        # self.resize(390, 300)
        self.setFixedSize(390, 300)

        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 140, 331, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(50, 30))
        self.label.setMaximumSize(QtCore.QSize(50, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.idEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.idEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.idEdit.setMaximumSize(QtCore.QSize(180, 30))
        self.idEdit.setObjectName("idEdit")
        self.gridLayout.addWidget(self.idEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(50, 30))
        self.label_2.setMaximumSize(QtCore.QSize(50, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.passwordEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.passwordEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.passwordEdit.setMaximumSize(QtCore.QSize(180, 30))
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout.addWidget(self.passwordEdit, 1, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 250, 271, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.loginBtn.setMaximumSize(QtCore.QSize(80, 35))
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout.addWidget(self.loginBtn)
        self.signupBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.signupBtn.setMaximumSize(QtCore.QSize(80, 35))
        self.signupBtn.setObjectName("signupBtn")
        self.horizontalLayout.addWidget(self.signupBtn)

        self.setBackground()
        self.retranslateUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        QtCore.QMetaObject.connectSlotsByName(self)

        # 绑定按钮事件
        self.loginBtn.clicked.connect(self.loginQQ)
        self.signupBtn.clicked.connect(self.signup)

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
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap('F:/QQ-project/source/login.png')))
        self.setPalette(palette)

    # 登录按钮功能
    def loginQQ(self):
        username = self.idEdit.text()
        password = self.passwordEdit.text()
        print(username, password)
        # 查询数据库是否存在用户及用户密码是否正确
        pass

    # 注册按钮功能
    def signup(self):
        print('请注册QQ...')
        pass

