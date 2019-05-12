from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import layouts.knowledgeEditorScalarEdit as design
import connectionToDatabase as db


class Scalar(QtWidgets.QMainWindow, design.Ui_scalarEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.FeatureName = ""

        self.button_goBack_scalarEdit.clicked.connect(self.goto_return)
        self.button_addDefinition_scalarEdit.clicked.connect(self.addDef)
        self.button_deleteScalarDef_scalarEdit.clicked.connect(self.deleteScalar)

    def updateData(self):
        self.showAllScalar()
        self.comboBox_deleteDefiniton_scalarEdit.clear()
        for row in self.getAllScalar():
            self.comboBox_deleteDefiniton_scalarEdit.addItem(row["Value"])

    def addDef(self):
        line = self.line_featureAdd_scalarEdit.text()
        line = line.strip()
        if line == "":
            QMessageBox.question(self, "Error", "No scalar found", QMessageBox.Cancel)
        else:
            if not (db.addScalarFeatureDef(self.FeatureName, self.line_featureAdd_scalarEdit.text())):
                QMessageBox.question(self, "Error", "Scalar already exist", QMessageBox.Cancel)
        self.updateData()

    def getAllScalar(self):
        return db.showAllScalarFeatureDef(self.FeatureName)

    def showAllScalar(self):
        rows = self.getAllScalar()
        self.text_added_scalarEdit.clear()
        for row in rows:
            self.text_added_scalarEdit.append(row["Value"])

    def deleteScalar(self):
        db.deleteScalarFeatureDef(self.FeatureName,self.comboBox_deleteDefiniton_scalarEdit.currentText())
        self.updateData()

    def set_featureName(self, text):
        self.FeatureName = text

    def goto_return(self):
        self.parent().show()
        self.close()
