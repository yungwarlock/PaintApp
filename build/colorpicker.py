# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/new_colorpicker.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_colorpicker(object):
    def setupUi(self, colorpicker):
        colorpicker.setObjectName("colorpicker")
        colorpicker.resize(322, 43)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(colorpicker)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.red = QtWidgets.QWidget(colorpicker)
        self.red.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.red.setObjectName("red")
        self.horizontalLayout.addWidget(self.red)
        self.blue = QtWidgets.QWidget(colorpicker)
        self.blue.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.blue.setObjectName("blue")
        self.horizontalLayout.addWidget(self.blue)
        self.yellow = QtWidgets.QLabel(colorpicker)
        self.yellow.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.yellow.setText("")
        self.yellow.setObjectName("yellow")
        self.horizontalLayout.addWidget(self.yellow)
        self.green = QtWidgets.QWidget(colorpicker)
        self.green.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.green.setObjectName("green")
        self.horizontalLayout.addWidget(self.green)
        self.black = QtWidgets.QLabel(colorpicker)
        self.black.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.black.setObjectName("black")
        self.horizontalLayout.addWidget(self.black)
        self.more_color = QtWidgets.QToolButton(colorpicker)
        self.more_color.setObjectName("more_color")
        self.horizontalLayout.addWidget(self.more_color)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(colorpicker)
        QtCore.QMetaObject.connectSlotsByName(colorpicker)

    def retranslateUi(self, colorpicker):
        _translate = QtCore.QCoreApplication.translate
        colorpicker.setWindowTitle(_translate("colorpicker", "Form"))
        self.black.setText(_translate("colorpicker", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.more_color.setText(_translate("colorpicker", "..."))
