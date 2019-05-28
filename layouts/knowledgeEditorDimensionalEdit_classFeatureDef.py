# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knowledgeEditorDimensionalEdit_classFeatureDef.ui'
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
        self.button_goBack_dimensionalEdit.setGeometry(QtCore.QRect(20, 250, 121, 31))
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
        self.widget = QtWidgets.QWidget(dimensionalEdit)
        self.widget.setGeometry(QtCore.QRect(50, 40, 321, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.spinbox_min = QtWidgets.QDoubleSpinBox(self.widget)
        self.spinbox_min.setDecimals(3)
        self.spinbox_min.setSingleStep(0.001)
        self.spinbox_min.setObjectName("spinbox_min")
        self.verticalLayout.addWidget(self.spinbox_min)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.spinbox_max = QtWidgets.QDoubleSpinBox(self.widget)
        self.spinbox_max.setDecimals(3)
        self.spinbox_max.setSingleStep(0.001)
        self.spinbox_max.setObjectName("spinbox_max")
        self.verticalLayout_2.addWidget(self.spinbox_max)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(dimensionalEdit)
        QtCore.QMetaObject.connectSlotsByName(dimensionalEdit)

    def retranslateUi(self, dimensionalEdit):
        _translate = QtCore.QCoreApplication.translate
        dimensionalEdit.setWindowTitle(_translate("dimensionalEdit", "Размерное значение"))
        self.button_goBack_dimensionalEdit.setText(_translate("dimensionalEdit", "Вернуться"))
        self.button_ok_dimensionalEdit.setText(_translate("dimensionalEdit", "ОК"))
        self.label.setText(_translate("dimensionalEdit", "Введите нижнее значение"))
        self.label_2.setText(_translate("dimensionalEdit", "Введите верхнее значение"))

