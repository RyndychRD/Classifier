# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knowledgeEditorFeaturePossibleDefinition.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_featurePossibleDefinition(object):
    def setupUi(self, featurePossibleDefinition):
        featurePossibleDefinition.setObjectName("featurePossibleDefinition")
        featurePossibleDefinition.resize(527, 452)
        featurePossibleDefinition.setMinimumSize(QtCore.QSize(527, 452))
        featurePossibleDefinition.setMaximumSize(QtCore.QSize(527, 452))
        self.centralwidget = QtWidgets.QWidget(featurePossibleDefinition)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_featureChoose_featurePossibleDefinition = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_featureChoose_featurePossibleDefinition.setGeometry(QtCore.QRect(30, 80, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_featureChoose_featurePossibleDefinition.setFont(font)
        self.comboBox_featureChoose_featurePossibleDefinition.setObjectName("comboBox_featureChoose_featurePossibleDefinition")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 150, 291, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.radioBut_scalar_featurePossibleDefinition = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioBut_scalar_featurePossibleDefinition.setFont(font)
        self.radioBut_scalar_featurePossibleDefinition.setObjectName("radioBut_scalar_featurePossibleDefinition")
        self.verticalLayout.addWidget(self.radioBut_scalar_featurePossibleDefinition)
        self.radioBut_logic_featurePossibleDefinition = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioBut_logic_featurePossibleDefinition.setFont(font)
        self.radioBut_logic_featurePossibleDefinition.setObjectName("radioBut_logic_featurePossibleDefinition")
        self.verticalLayout.addWidget(self.radioBut_logic_featurePossibleDefinition)
        self.radioBut_dimensional_featurePossibleDefinition = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioBut_dimensional_featurePossibleDefinition.setFont(font)
        self.radioBut_dimensional_featurePossibleDefinition.setObjectName("radioBut_dimensional_featurePossibleDefinition")
        self.verticalLayout.addWidget(self.radioBut_dimensional_featurePossibleDefinition)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(31, 360, 471, 32))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_goBack_featurePossibleDefinition = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_goBack_featurePossibleDefinition.setFont(font)
        self.button_goBack_featurePossibleDefinition.setObjectName("button_goBack_featurePossibleDefinition")
        self.horizontalLayout.addWidget(self.button_goBack_featurePossibleDefinition)
        self.button_Ok_featurePossibleDefinition = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_Ok_featurePossibleDefinition.setFont(font)
        self.button_Ok_featurePossibleDefinition.setObjectName("button_Ok_featurePossibleDefinition")
        self.horizontalLayout.addWidget(self.button_Ok_featurePossibleDefinition)
        featurePossibleDefinition.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(featurePossibleDefinition)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 22))
        self.menubar.setObjectName("menubar")
        featurePossibleDefinition.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(featurePossibleDefinition)
        self.statusbar.setObjectName("statusbar")
        featurePossibleDefinition.setStatusBar(self.statusbar)

        self.retranslateUi(featurePossibleDefinition)
        QtCore.QMetaObject.connectSlotsByName(featurePossibleDefinition)

    def retranslateUi(self, featurePossibleDefinition):
        _translate = QtCore.QCoreApplication.translate
        featurePossibleDefinition.setWindowTitle(_translate("featurePossibleDefinition", "Редактор знаний. Возможные значения признаков"))
        self.label.setText(_translate("featurePossibleDefinition", "Выберите признак"))
        self.label_2.setText(_translate("featurePossibleDefinition", "Тип признака"))
        self.radioBut_scalar_featurePossibleDefinition.setText(_translate("featurePossibleDefinition", "Скалярное значение"))
        self.radioBut_logic_featurePossibleDefinition.setText(_translate("featurePossibleDefinition", "Логический"))
        self.radioBut_dimensional_featurePossibleDefinition.setText(_translate("featurePossibleDefinition", "Размерное значение"))
        self.button_goBack_featurePossibleDefinition.setText(_translate("featurePossibleDefinition", "Вернуться"))
        self.button_Ok_featurePossibleDefinition.setText(_translate("featurePossibleDefinition", "Установить значение"))

