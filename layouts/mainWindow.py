# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 270)
        MainWindow.setMinimumSize(QtCore.QSize(551, 270))
        MainWindow.setMaximumSize(QtCore.QSize(551, 270))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_detectClass_MainWindow = QtWidgets.QPushButton(self.centralwidget)
        self.button_detectClass_MainWindow.setGeometry(QtCore.QRect(120, 130, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_detectClass_MainWindow.setFont(font)
        self.button_detectClass_MainWindow.setObjectName("button_detectClass_MainWindow")
        self.buton_knowledgeEditor_MainWindow = QtWidgets.QPushButton(self.centralwidget)
        self.buton_knowledgeEditor_MainWindow.setGeometry(QtCore.QRect(120, 50, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buton_knowledgeEditor_MainWindow.setFont(font)
        self.buton_knowledgeEditor_MainWindow.setObjectName("buton_knowledgeEditor_MainWindow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Классификатор элетротехники"))
        self.button_detectClass_MainWindow.setText(_translate("MainWindow", "Определить класс электротехники"))
        self.buton_knowledgeEditor_MainWindow.setText(_translate("MainWindow", "Редактор знаний"))

