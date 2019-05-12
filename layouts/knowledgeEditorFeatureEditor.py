# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knowledgeEditorFeautreEditor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_featureEditor(object):
    def setupUi(self, featureEditor):
        featureEditor.setObjectName("featureEditor")
        featureEditor.resize(798, 595)
        featureEditor.setMinimumSize(QtCore.QSize(798, 595))
        featureEditor.setMaximumSize(QtCore.QSize(798, 595))
        self.centralwidget = QtWidgets.QWidget(featureEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.button_featureAdd_featureEditor = QtWidgets.QPushButton(self.centralwidget)
        self.button_featureAdd_featureEditor.setGeometry(QtCore.QRect(540, 80, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_featureAdd_featureEditor.setFont(font)
        self.button_featureAdd_featureEditor.setObjectName("button_featureAdd_featureEditor")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 45, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.button_goBack_featureEditor = QtWidgets.QPushButton(self.centralwidget)
        self.button_goBack_featureEditor.setGeometry(QtCore.QRect(50, 510, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_goBack_featureEditor.setFont(font)
        self.button_goBack_featureEditor.setObjectName("button_goBack_featureEditor")
        self.text_featureExist_featureEditor = QtWidgets.QTextEdit(self.centralwidget)
        self.text_featureExist_featureEditor.setGeometry(QtCore.QRect(70, 190, 451, 151))
        self.text_featureExist_featureEditor.setObjectName("text_featureExist_featureEditor")
        self.comboBox_featureDelete_featureEditor = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_featureDelete_featureEditor.setGeometry(QtCore.QRect(70, 410, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_featureDelete_featureEditor.setFont(font)
        self.comboBox_featureDelete_featureEditor.setObjectName("comboBox_featureDelete_featureEditor")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 370, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.button_featureDelete_featureEditor = QtWidgets.QPushButton(self.centralwidget)
        self.button_featureDelete_featureEditor.setGeometry(QtCore.QRect(540, 400, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_featureDelete_featureEditor.setFont(font)
        self.button_featureDelete_featureEditor.setObjectName("button_featureDelete_featureEditor")
        self.line_featureAdd_classEditor = QtWidgets.QLineEdit(self.centralwidget)
        self.line_featureAdd_classEditor.setGeometry(QtCore.QRect(70, 90, 461, 31))
        self.line_featureAdd_classEditor.setObjectName("line_featureAdd_classEditor")
        featureEditor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(featureEditor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menubar.setObjectName("menubar")
        featureEditor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(featureEditor)
        self.statusbar.setObjectName("statusbar")
        featureEditor.setStatusBar(self.statusbar)

        self.retranslateUi(featureEditor)
        QtCore.QMetaObject.connectSlotsByName(featureEditor)

    def retranslateUi(self, featureEditor):
        _translate = QtCore.QCoreApplication.translate
        featureEditor.setWindowTitle(_translate("featureEditor", "Редактор знаний. Признаки"))
        self.button_featureAdd_featureEditor.setText(_translate("featureEditor", "Добавить новый признак"))
        self.label.setText(_translate("featureEditor", "Введите название признака электротехники"))
        self.label_2.setText(_translate("featureEditor", "Существующие признаки электротехники"))
        self.button_goBack_featureEditor.setText(_translate("featureEditor", "Вернуться"))
        self.label_3.setText(_translate("featureEditor", "Выберите признак для удаления"))
        self.button_featureDelete_featureEditor.setText(_translate("featureEditor", "Удалить признак"))

