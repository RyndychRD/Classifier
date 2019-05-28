from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *

import layouts.knowledgeEditorDimensionalEdit as design
import connectionToDatabase as db


class Dimensional(QtWidgets.QMainWindow, design.Ui_dimensionalEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.FeatureName = ""
        self.FeatureType = "Dimensional"
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        self.button_goBack_dimensionalEdit.clicked.connect(self.goto_return)
        self.button_ok_dimensionalEdit.clicked.connect(self.save_and_return)

    def set_featureName(self, text):
        self.FeatureName = text

    def clearData(self):
        self.check_MaxValue_dimensionalEdit.setChecked(False)
        self.check_MinValue_dimensionalEdit.setChecked(False)
        self.spinBox_start_dimensionalEdit.clear()
        self.spinBox_end_dimensionalEdit.clear()

    def save_and_return(self):
        left = self.spinBox_start_dimensionalEdit.text()
        right = self.spinBox_end_dimensionalEdit.text()
        if right <= left:
            QMessageBox.question(self, "Error", " Right Value cannot be less then left (in case (left,right] too 8P )",
                                 QMessageBox.Cancel)
        ifLeftIncluded = self.check_MinValue_dimensionalEdit.isChecked()
        ifRightIncluded = self.check_MaxValue_dimensionalEdit.isChecked()
        db.addDimensionalFeatureDef(self.FeatureName, left, right, ifLeftIncluded, ifRightIncluded)
        self.parent().show()
        self.close()

    def goto_return(self):
        QMessageBox.question(self, "Error", " You have to input values. No way back",
                             QMessageBox.Cancel)

