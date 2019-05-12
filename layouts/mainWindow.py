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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 50, 441, 141))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buton_knowledgeEditor_MainWindow = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buton_knowledgeEditor_MainWindow.setFont(font)
        self.buton_knowledgeEditor_MainWindow.setObjectName("buton_knowledgeEditor_MainWindow")
        self.verticalLayout.addWidget(self.buton_knowledgeEditor_MainWindow)
        self.button_detectClass_MainWindow = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_detectClass_MainWindow.setFont(font)
        self.button_detectClass_MainWindow.setObjectName("button_detectClass_MainWindow")
        self.verticalLayout.addWidget(self.button_detectClass_MainWindow)
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
        self.buton_knowledgeEditor_MainWindow.setText(_translate("MainWindow", "Редактор знаний"))
        self.button_detectClass_MainWindow.setText(_translate("MainWindow", "Определить класс электротехники"))

