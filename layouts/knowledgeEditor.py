# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knowledgeEditor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_knowledgeEditor(object):
    def setupUi(self, knowledgeEditor):
        knowledgeEditor.setObjectName("knowledgeEditor")
        knowledgeEditor.resize(798, 595)
        knowledgeEditor.setMinimumSize(QtCore.QSize(798, 595))
        knowledgeEditor.setMaximumSize(QtCore.QSize(798, 595))
        self.centralwidget = QtWidgets.QWidget(knowledgeEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.button_goBack_knowledgeEditor = QtWidgets.QPushButton(self.centralwidget)
        self.button_goBack_knowledgeEditor.setGeometry(QtCore.QRect(50, 510, 102, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_goBack_knowledgeEditor.setFont(font)
        self.button_goBack_knowledgeEditor.setObjectName("button_goBack_knowledgeEditor")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 70, 481, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_classEditor_knowledgeEditor = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_classEditor_knowledgeEditor.setFont(font)
        self.button_classEditor_knowledgeEditor.setObjectName("button_classEditor_knowledgeEditor")
        self.verticalLayout.addWidget(self.button_classEditor_knowledgeEditor)
        self.button_featureEditor_knowledgeEditor = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_featureEditor_knowledgeEditor.setFont(font)
        self.button_featureEditor_knowledgeEditor.setObjectName("button_featureEditor_knowledgeEditor")
        self.verticalLayout.addWidget(self.button_featureEditor_knowledgeEditor)
        self.button_featurePossibleDefinition_knowledgeEditor = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_featurePossibleDefinition_knowledgeEditor.setFont(font)
        self.button_featurePossibleDefinition_knowledgeEditor.setObjectName("button_featurePossibleDefinition_knowledgeEditor")
        self.verticalLayout.addWidget(self.button_featurePossibleDefinition_knowledgeEditor)
        self.button_classExplanation_knowledgeEditor = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_classExplanation_knowledgeEditor.setFont(font)
        self.button_classExplanation_knowledgeEditor.setObjectName("button_classExplanation_knowledgeEditor")
        self.verticalLayout.addWidget(self.button_classExplanation_knowledgeEditor)
        self.button_classFeatureDefinition_knowledgeEditor = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_classFeatureDefinition_knowledgeEditor.setFont(font)
        self.button_classFeatureDefinition_knowledgeEditor.setObjectName("button_classFeatureDefinition_knowledgeEditor")
        self.verticalLayout.addWidget(self.button_classFeatureDefinition_knowledgeEditor)
        knowledgeEditor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(knowledgeEditor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menubar.setObjectName("menubar")
        knowledgeEditor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(knowledgeEditor)
        self.statusbar.setObjectName("statusbar")
        knowledgeEditor.setStatusBar(self.statusbar)

        self.retranslateUi(knowledgeEditor)
        QtCore.QMetaObject.connectSlotsByName(knowledgeEditor)

    def retranslateUi(self, knowledgeEditor):
        _translate = QtCore.QCoreApplication.translate
        knowledgeEditor.setWindowTitle(_translate("knowledgeEditor", "Редактор знаний"))
        self.button_goBack_knowledgeEditor.setText(_translate("knowledgeEditor", "Вернуться"))
        self.label.setText(_translate("knowledgeEditor", "Выберите раздел"))
        self.button_classEditor_knowledgeEditor.setText(_translate("knowledgeEditor", "Редактировать классы"))
        self.button_featureEditor_knowledgeEditor.setText(_translate("knowledgeEditor", "Редактировать признаки"))
        self.button_featurePossibleDefinition_knowledgeEditor.setText(_translate("knowledgeEditor", "Установка возможных значений признаков"))
        self.button_classExplanation_knowledgeEditor.setText(_translate("knowledgeEditor", "Признаковое описание классов"))
        self.button_classFeatureDefinition_knowledgeEditor.setText(_translate("knowledgeEditor", "Значение признаков для классов"))
