# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knowledgeEditorClassFeatureDefinition.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_classFeatureDefinition(object):
    def setupUi(self, classFeatureDefinition):
        classFeatureDefinition.setObjectName("classFeatureDefinition")
        classFeatureDefinition.resize(800, 600)
        classFeatureDefinition.setMinimumSize(QtCore.QSize(800, 600))
        classFeatureDefinition.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(classFeatureDefinition)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 50, 411, 55))
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
        self.comboBox_classChoose_classFeatureDefinition = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_classChoose_classFeatureDefinition.setObjectName("comboBox_classChoose_classFeatureDefinition")
        self.verticalLayout.addWidget(self.comboBox_classChoose_classFeatureDefinition)
        self.button_goBack_classFeatureDefinition = QtWidgets.QPushButton(self.centralwidget)
        self.button_goBack_classFeatureDefinition.setGeometry(QtCore.QRect(30, 500, 102, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_goBack_classFeatureDefinition.setFont(font)
        self.button_goBack_classFeatureDefinition.setObjectName("button_goBack_classFeatureDefinition")
        self.button_ok_classFeatureDefinition = QtWidgets.QPushButton(self.centralwidget)
        self.button_ok_classFeatureDefinition.setGeometry(QtCore.QRect(670, 500, 102, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_ok_classFeatureDefinition.setFont(font)
        self.button_ok_classFeatureDefinition.setObjectName("button_ok_classFeatureDefinition")
        self.button_featureSet_classFeatureDefinition = QtWidgets.QPushButton(self.centralwidget)
        self.button_featureSet_classFeatureDefinition.setGeometry(QtCore.QRect(650, 147, 110, 52))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_featureSet_classFeatureDefinition.setFont(font)
        self.button_featureSet_classFeatureDefinition.setObjectName("button_featureSet_classFeatureDefinition")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(410, 220, 351, 222))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.text_featureUnset_classFeatureDefinition = QtWidgets.QTextEdit(self.layoutWidget1)
        self.text_featureUnset_classFeatureDefinition.setReadOnly(True)
        self.text_featureUnset_classFeatureDefinition.setObjectName("text_featureUnset_classFeatureDefinition")
        self.verticalLayout_2.addWidget(self.text_featureUnset_classFeatureDefinition)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(44, 220, 361, 222))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.text_featureSetted_classFeatureDefinition = QtWidgets.QTextEdit(self.layoutWidget2)
        self.text_featureSetted_classFeatureDefinition.setReadOnly(True)
        self.text_featureSetted_classFeatureDefinition.setObjectName("text_featureSetted_classFeatureDefinition")
        self.verticalLayout_3.addWidget(self.text_featureSetted_classFeatureDefinition)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(42, 140, 411, 61))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.comboBox_featureChoose_classFeatureDefinition = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_featureChoose_classFeatureDefinition.setObjectName("comboBox_featureChoose_classFeatureDefinition")
        self.verticalLayout_6.addWidget(self.comboBox_featureChoose_classFeatureDefinition)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(462, 145, 181, 55))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.line_featureType_classFeatureDefinition = QtWidgets.QLineEdit(self.layoutWidget4)
        self.line_featureType_classFeatureDefinition.setReadOnly(True)
        self.line_featureType_classFeatureDefinition.setObjectName("line_featureType_classFeatureDefinition")
        self.verticalLayout_4.addWidget(self.line_featureType_classFeatureDefinition)
        classFeatureDefinition.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(classFeatureDefinition)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        classFeatureDefinition.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(classFeatureDefinition)
        self.statusbar.setObjectName("statusbar")
        classFeatureDefinition.setStatusBar(self.statusbar)

        self.retranslateUi(classFeatureDefinition)
        QtCore.QMetaObject.connectSlotsByName(classFeatureDefinition)

    def retranslateUi(self, classFeatureDefinition):
        _translate = QtCore.QCoreApplication.translate
        classFeatureDefinition.setWindowTitle(_translate("classFeatureDefinition", "Редактор знаний. Установка значений признаков"))
        self.label.setText(_translate("classFeatureDefinition", "Выберите класс"))
        self.button_goBack_classFeatureDefinition.setText(_translate("classFeatureDefinition", "Вернуться"))
        self.button_ok_classFeatureDefinition.setText(_translate("classFeatureDefinition", "ОК"))
        self.button_featureSet_classFeatureDefinition.setText(_translate("classFeatureDefinition", "Установить\n"
" значение"))
        self.label_7.setText(_translate("classFeatureDefinition", "Список не определенных признаков"))
        self.label_6.setText(_translate("classFeatureDefinition", "Список определенных признаков"))
        self.label_5.setText(_translate("classFeatureDefinition", "Выберите признак"))
        self.label_3.setText(_translate("classFeatureDefinition", "Тип признака"))

