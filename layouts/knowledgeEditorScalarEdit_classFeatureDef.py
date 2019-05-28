# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knowledgeEditorScalarEdit_classFeatureDef.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_scalarEdit(object):
    def setupUi(self, scalarEdit):
        scalarEdit.setObjectName("scalarEdit")
        scalarEdit.resize(400, 327)
        scalarEdit.setMinimumSize(QtCore.QSize(400, 300))
        scalarEdit.setMaximumSize(QtCore.QSize(400, 327))
        self.button_goBack_scalarEdit = QtWidgets.QPushButton(scalarEdit)
        self.button_goBack_scalarEdit.setGeometry(QtCore.QRect(20, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_goBack_scalarEdit.setFont(font)
        self.button_goBack_scalarEdit.setObjectName("button_goBack_scalarEdit")
        self.button_ok_scalarEdit = QtWidgets.QPushButton(scalarEdit)
        self.button_ok_scalarEdit.setGeometry(QtCore.QRect(280, 290, 102, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_ok_scalarEdit.setFont(font)
        self.button_ok_scalarEdit.setObjectName("button_ok_scalarEdit")
        self.widget = QtWidgets.QWidget(scalarEdit)
        self.widget.setGeometry(QtCore.QRect(40, 20, 316, 244))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget_ScalarEdit = QtWidgets.QListWidget(self.widget)
        self.listWidget_ScalarEdit.setObjectName("listWidget_ScalarEdit")
        self.verticalLayout.addWidget(self.listWidget_ScalarEdit)

        self.retranslateUi(scalarEdit)
        QtCore.QMetaObject.connectSlotsByName(scalarEdit)

    def retranslateUi(self, scalarEdit):
        _translate = QtCore.QCoreApplication.translate
        scalarEdit.setWindowTitle(_translate("scalarEdit", "Скалярное значение"))
        self.button_goBack_scalarEdit.setText(_translate("scalarEdit", "Вернуться"))
        self.button_ok_scalarEdit.setText(_translate("scalarEdit", "ОК"))
        self.label.setText(_translate("scalarEdit", "Выберите допустимые значения"))

