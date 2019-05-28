# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkOfFullness.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_checkOfFullness(object):
    def setupUi(self, checkOfFullness):
        checkOfFullness.setObjectName("checkOfFullness")
        checkOfFullness.resize(387, 300)
        self.text_checkFullness = QtWidgets.QTextBrowser(checkOfFullness)
        self.text_checkFullness.setGeometry(QtCore.QRect(30, 20, 321, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_checkFullness.setFont(font)
        self.text_checkFullness.setObjectName("text_checkFullness")
        self.button_ok_checkFullness = QtWidgets.QPushButton(checkOfFullness)
        self.button_ok_checkFullness.setGeometry(QtCore.QRect(260, 240, 102, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_ok_checkFullness.setFont(font)
        self.button_ok_checkFullness.setObjectName("button_ok_checkFullness")
        self.button_goBack_checkFullness = QtWidgets.QPushButton(checkOfFullness)
        self.button_goBack_checkFullness.setGeometry(QtCore.QRect(20, 240, 102, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_goBack_checkFullness.setFont(font)
        self.button_goBack_checkFullness.setObjectName("button_goBack_checkFullness")

        self.retranslateUi(checkOfFullness)
        QtCore.QMetaObject.connectSlotsByName(checkOfFullness)

    def retranslateUi(self, checkOfFullness):
        _translate = QtCore.QCoreApplication.translate
        checkOfFullness.setWindowTitle(_translate("checkOfFullness", "Dialog"))
        self.button_ok_checkFullness.setText(_translate("checkOfFullness", "ОК"))
        self.button_goBack_checkFullness.setText(_translate("checkOfFullness", "Вернуться"))

