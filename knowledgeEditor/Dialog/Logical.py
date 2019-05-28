from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *

import layouts.knowledgeEditorLogicallEdit as design
import connectionToDatabase as db


class Logical(QtWidgets.QMainWindow, design.Ui_logicalEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.FeatureName = ""
        self.FeatureType = "Logical"
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        self.button_goBack_logicalEdit.clicked.connect(self.goto_return)
        self.button_ok_logicalEdit.clicked.connect(self.save_and_return)

    def clearData(self):
        self.line_false_logicalEdit.clear()
        self.line_true_logicalEdit.clear()

    def set_featureName(self, text):
        self.FeatureName = text

    def save_and_return(self):
        textTrue = self.line_true_logicalEdit.text()
        textFalse = self.line_false_logicalEdit.text()
        textTrue = textTrue.strip()
        textFalse = textFalse.strip()
        if textTrue == "":
            QMessageBox.question(self, "Error", "No true found", QMessageBox.Cancel)
            return
        if textFalse == "":
            QMessageBox.question(self, "Error", "No false found", QMessageBox.Cancel)
            return
        if textFalse == textTrue:
            QMessageBox.question(self, "Error", "True is the same as false", QMessageBox.Cancel)
            return
        db.addLogicalFeatureDef(self.FeatureName, textTrue, textFalse)
        self.parent().show()
        self.close()

    def goto_return(self):
        QMessageBox.question(self, "Error", " You have to input values. No way back",
                             QMessageBox.Cancel)
