# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knowledgeEditorDimensionalEdit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dimensionalEdit(object):
    def setupUi(self, dimensionalEdit):
        dimensionalEdit.setObjectName("dimensionalEdit")
        dimensionalEdit.resize(400, 300)
        dimensionalEdit.setMinimumSize(QtCore.QSize(400, 300))
        dimensionalEdit.setMaximumSize(QtCore.QSize(400, 300))
        self.button_goBack_dimensionalEdit = QtWidgets.QPushButton(dimensionalEdit)
        self.button_goBack_dimensionalEdit.setGeometry(QtCore.QRect(20, 250, 102, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_goBack_dimensionalEdit.setFont(font)
        self.button_goBack_dimensionalEdit.setObjectName("button_goBack_dimensionalEdit")
        self.button_ok_dimensionalEdit = QtWidgets.QPushButton(dimensionalEdit)
        self.button_ok_dimensionalEdit.setGeometry(QtCore.QRect(280, 250, 102, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_ok_dimensionalEdit.setFont(font)
        self.button_ok_dimensionalEdit.setObjectName("button_ok_dimensionalEdit")
        self.layoutWidget = QtWidgets.QWidget(dimensionalEdit)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 371, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.spinBox_start_dimensionalEdit = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spinBox_start_dimensionalEdit.setMaximum(999999999.0)
        self.spinBox_start_dimensionalEdit.setSingleStep(0.1)
        self.spinBox_start_dimensionalEdit.setObjectName("spinBox_start_dimensionalEdit")
        self.gridLayout.addWidget(self.spinBox_start_dimensionalEdit, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)
        self.spinBox_end_dimensionalEdit = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spinBox_end_dimensionalEdit.setMaximum(999999999.0)
        self.spinBox_end_dimensionalEdit.setSingleStep(0.1)
        self.spinBox_end_dimensionalEdit.setObjectName("spinBox_end_dimensionalEdit")
        self.gridLayout_2.addWidget(self.spinBox_end_dimensionalEdit, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(dimensionalEdit)
        QtCore.QMetaObject.connectSlotsByName(dimensionalEdit)

    def retranslateUi(self, dimensionalEdit):
        _translate = QtCore.QCoreApplication.translate
        dimensionalEdit.setWindowTitle(_translate("dimensionalEdit", "Размерное значение"))
        self.button_goBack_dimensionalEdit.setText(_translate("dimensionalEdit", "Вернуться"))
        self.button_ok_dimensionalEdit.setText(_translate("dimensionalEdit", "ОК"))
        self.label.setText(_translate("dimensionalEdit", "Введите начальное значение"))
        self.label_2.setText(_translate("dimensionalEdit", "Введите конечное значение"))

