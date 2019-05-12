# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knowledgeEditorLogicallEdit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_logicalEdit(object):
    def setupUi(self, logicalEdit):
        logicalEdit.setObjectName("logicalEdit")
        logicalEdit.resize(414, 300)
        logicalEdit.setMinimumSize(QtCore.QSize(414, 300))
        logicalEdit.setMaximumSize(QtCore.QSize(414, 300))
        self.button_goBack_logicalEdit = QtWidgets.QPushButton(logicalEdit)
        self.button_goBack_logicalEdit.setGeometry(QtCore.QRect(20, 250, 102, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_goBack_logicalEdit.setFont(font)
        self.button_goBack_logicalEdit.setObjectName("button_goBack_logicalEdit")
        self.button_ok_logicalEdit = QtWidgets.QPushButton(logicalEdit)
        self.button_ok_logicalEdit.setGeometry(QtCore.QRect(280, 250, 102, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_ok_logicalEdit.setFont(font)
        self.button_ok_logicalEdit.setObjectName("button_ok_logicalEdit")
        self.layoutWidget = QtWidgets.QWidget(logicalEdit)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 371, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_true_logicalEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_true_logicalEdit.setObjectName("line_true_logicalEdit")
        self.verticalLayout.addWidget(self.line_true_logicalEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line_false_logicalEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_false_logicalEdit.setObjectName("line_false_logicalEdit")
        self.verticalLayout.addWidget(self.line_false_logicalEdit)

        self.retranslateUi(logicalEdit)
        QtCore.QMetaObject.connectSlotsByName(logicalEdit)

    def retranslateUi(self, logicalEdit):
        _translate = QtCore.QCoreApplication.translate
        logicalEdit.setWindowTitle(_translate("logicalEdit", "Логическое значение"))
        self.button_goBack_logicalEdit.setText(_translate("logicalEdit", "Вернуться"))
        self.button_ok_logicalEdit.setText(_translate("logicalEdit", "ОК"))
        self.label.setText(_translate("logicalEdit", "Введите значение ИСТИНЫ"))
        self.label_2.setText(_translate("logicalEdit", "Введите значение ЛЖИ"))

