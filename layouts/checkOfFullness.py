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
        checkOfFullness.setMinimumSize(QtCore.QSize(387, 300))
        checkOfFullness.setMaximumSize(QtCore.QSize(387, 300))
        self.text_checkFullness = QtWidgets.QTextBrowser(checkOfFullness)
        self.text_checkFullness.setGeometry(QtCore.QRect(30, 20, 321, 181))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.text_checkFullness.setFont(font)
        self.text_checkFullness.setObjectName("text_checkFullness")
        self.widget = QtWidgets.QWidget(checkOfFullness)
        self.widget.setGeometry(QtCore.QRect(20, 241, 341, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_goBack_checkFullness = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_goBack_checkFullness.setFont(font)
        self.button_goBack_checkFullness.setObjectName("button_goBack_checkFullness")
        self.horizontalLayout.addWidget(self.button_goBack_checkFullness)
        self.button_ok_checkFullness = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_ok_checkFullness.setFont(font)
        self.button_ok_checkFullness.setObjectName("button_ok_checkFullness")
        self.horizontalLayout.addWidget(self.button_ok_checkFullness)

        self.retranslateUi(checkOfFullness)
        QtCore.QMetaObject.connectSlotsByName(checkOfFullness)

    def retranslateUi(self, checkOfFullness):
        _translate = QtCore.QCoreApplication.translate
        checkOfFullness.setWindowTitle(_translate("checkOfFullness", "Dialog"))
        self.button_goBack_checkFullness.setText(_translate("checkOfFullness", "Вернуться"))
        self.button_ok_checkFullness.setText(_translate("checkOfFullness", "Решить задачу"))

