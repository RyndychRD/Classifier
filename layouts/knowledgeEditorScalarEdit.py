# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knowledgeEditorScalarEdit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_scalarEdit(object):
    def setupUi(self, scalarEdit):
        scalarEdit.setObjectName("scalarEdit")
        scalarEdit.resize(400, 300)
        scalarEdit.setMinimumSize(QtCore.QSize(400, 300))
        scalarEdit.setMaximumSize(QtCore.QSize(400, 300))
        self.button_goBack_scalarEdit = QtWidgets.QPushButton(scalarEdit)
        self.button_goBack_scalarEdit.setGeometry(QtCore.QRect(20, 250, 102, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_goBack_scalarEdit.setFont(font)
        self.button_goBack_scalarEdit.setObjectName("button_goBack_scalarEdit")
        self.button_ok_scalarEdit = QtWidgets.QPushButton(scalarEdit)
        self.button_ok_scalarEdit.setGeometry(QtCore.QRect(280, 250, 102, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_ok_scalarEdit.setFont(font)
        self.button_ok_scalarEdit.setObjectName("button_ok_scalarEdit")
        self.layoutWidget = QtWidgets.QWidget(scalarEdit)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 361, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.button_addDefinition_scalarEdit = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_addDefinition_scalarEdit.setFont(font)
        self.button_addDefinition_scalarEdit.setObjectName("button_addDefinition_scalarEdit")
        self.gridLayout.addWidget(self.button_addDefinition_scalarEdit, 1, 1, 1, 1)
        self.line_featureAdd_scalarEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_featureAdd_scalarEdit.setObjectName("line_featureAdd_scalarEdit")
        self.gridLayout.addWidget(self.line_featureAdd_scalarEdit, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox_setDefinition_scalarEdit = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_setDefinition_scalarEdit.setObjectName("comboBox_setDefinition_scalarEdit")
        self.verticalLayout.addWidget(self.comboBox_setDefinition_scalarEdit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboBox_deleteDefiniton_scalarEdit = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_deleteDefiniton_scalarEdit.setObjectName("comboBox_deleteDefiniton_scalarEdit")
        self.verticalLayout.addWidget(self.comboBox_deleteDefiniton_scalarEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(scalarEdit)
        QtCore.QMetaObject.connectSlotsByName(scalarEdit)

    def retranslateUi(self, scalarEdit):
        _translate = QtCore.QCoreApplication.translate
        scalarEdit.setWindowTitle(_translate("scalarEdit", "Скалярное значение"))
        self.button_goBack_scalarEdit.setText(_translate("scalarEdit", "Вернуться"))
        self.button_ok_scalarEdit.setText(_translate("scalarEdit", "ОК"))
        self.label.setText(_translate("scalarEdit", "Введите значение для добавления"))
        self.button_addDefinition_scalarEdit.setText(_translate("scalarEdit", "Добавить"))
        self.label_2.setText(_translate("scalarEdit", "Выберите значение для назначения"))
        self.label_3.setText(_translate("scalarEdit", "Выберите значение для удаления"))

