# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knowledgeEditorClassEditor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_classEditor(object):
    def setupUi(self, classEditor):
        classEditor.setObjectName("classEditor")
        classEditor.resize(798, 595)
        classEditor.setMinimumSize(QtCore.QSize(798, 595))
        classEditor.setMaximumSize(QtCore.QSize(798, 595))
        self.centralwidget = QtWidgets.QWidget(classEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.button_classAdd_classEditor = QtWidgets.QPushButton(self.centralwidget)
        self.button_classAdd_classEditor.setGeometry(QtCore.QRect(540, 80, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_classAdd_classEditor.setFont(font)
        self.button_classAdd_classEditor.setObjectName("button_classAdd_classEditor")
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
        self.button_goBack_classEditor = QtWidgets.QPushButton(self.centralwidget)
        self.button_goBack_classEditor.setGeometry(QtCore.QRect(50, 510, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_goBack_classEditor.setFont(font)
        self.button_goBack_classEditor.setObjectName("button_goBack_classEditor")
        self.text_classExist_classEditor = QtWidgets.QTextEdit(self.centralwidget)
        self.text_classExist_classEditor.setGeometry(QtCore.QRect(70, 190, 451, 151))
        self.text_classExist_classEditor.setObjectName("text_classExist_classEditor")
        self.comboBox_classDelete_classEditor = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_classDelete_classEditor.setGeometry(QtCore.QRect(70, 410, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_classDelete_classEditor.setFont(font)
        self.comboBox_classDelete_classEditor.setObjectName("comboBox_classDelete_classEditor")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 370, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.button_classDelete_classEditor = QtWidgets.QPushButton(self.centralwidget)
        self.button_classDelete_classEditor.setGeometry(QtCore.QRect(540, 400, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_classDelete_classEditor.setFont(font)
        self.button_classDelete_classEditor.setObjectName("button_classDelete_classEditor")
        self.line_classAdd_classEditor = QtWidgets.QLineEdit(self.centralwidget)
        self.line_classAdd_classEditor.setGeometry(QtCore.QRect(70, 90, 451, 31))
        self.line_classAdd_classEditor.setObjectName("line_classAdd_classEditor")
        classEditor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(classEditor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menubar.setObjectName("menubar")
        classEditor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(classEditor)
        self.statusbar.setObjectName("statusbar")
        classEditor.setStatusBar(self.statusbar)

        self.retranslateUi(classEditor)
        QtCore.QMetaObject.connectSlotsByName(classEditor)

    def retranslateUi(self, classEditor):
        _translate = QtCore.QCoreApplication.translate
        classEditor.setWindowTitle(_translate("classEditor", "Редактор знаний. Классы"))
        self.button_classAdd_classEditor.setText(_translate("classEditor", "Добавить новый класс"))
        self.label.setText(_translate("classEditor", "Введите название класса электротехники"))
        self.label_2.setText(_translate("classEditor", "Существующие классы электротехники"))
        self.button_goBack_classEditor.setText(_translate("classEditor", "Вернуться"))
        self.label_3.setText(_translate("classEditor", "Выберите класс для удаления"))
        self.button_classDelete_classEditor.setText(_translate("classEditor", "Удалить класс"))

