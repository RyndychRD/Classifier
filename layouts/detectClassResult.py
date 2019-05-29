# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detectClassResult.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_result(object):
    def setupUi(self, result):
        result.setObjectName("result")
        result.resize(800, 600)
        result.setMinimumSize(QtCore.QSize(800, 600))
        result.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(result)
        self.centralwidget.setObjectName("centralwidget")
        self.button_goBack_result = QtWidgets.QPushButton(self.centralwidget)
        self.button_goBack_result.setGeometry(QtCore.QRect(20, 510, 102, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_goBack_result.setFont(font)
        self.button_goBack_result.setObjectName("button_goBack_result")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 20, 681, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.line_possibleClass_result = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_possibleClass_result.setReadOnly(True)
        self.line_possibleClass_result.setObjectName("line_possibleClass_result")
        self.horizontalLayout.addWidget(self.line_possibleClass_result)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.text_impossibleClasses_result = QtWidgets.QTextEdit(self.layoutWidget)
        self.text_impossibleClasses_result.setReadOnly(True)
        self.text_impossibleClasses_result.setObjectName("text_impossibleClasses_result")
        self.verticalLayout.addWidget(self.text_impossibleClasses_result)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        result.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(result)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        result.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(result)
        self.statusbar.setObjectName("statusbar")
        result.setStatusBar(self.statusbar)

        self.retranslateUi(result)
        QtCore.QMetaObject.connectSlotsByName(result)

    def retranslateUi(self, result):
        _translate = QtCore.QCoreApplication.translate
        result.setWindowTitle(_translate("result", "Определение класса электротехники. Результат"))
        self.button_goBack_result.setText(_translate("result", "Вернуться"))
        self.label.setText(_translate("result", "Результат"))
        self.label_2.setText(_translate("result", "Возможный класс"))
        self.label_3.setText(_translate("result", "Список неподходящих классов"))

