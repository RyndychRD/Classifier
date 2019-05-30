from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import layouts.knowledgeEditorFeatureEditor as design
import connectionToDatabase as db


class featureEditor(QtWidgets.QMainWindow, design.Ui_featureEditor):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.updateData()

        self.button_goBack_featureEditor.clicked.connect(self.goto_return)
        self.button_featureAdd_featureEditor.clicked.connect(self.addFeature)
        self.button_featureDelete_featureEditor.clicked.connect(self.deleteFeature)

    def updateData(self):
        self.line_featureAdd_classEditor.clear()
        self.comboBox_featureDelete_featureEditor.clear()
        for row in self.getAllFeatures():
            self.comboBox_featureDelete_featureEditor.addItem(row["NameFeature"])
        self.showAllFeatures()

    def addFeature(self):
        line = self.line_featureAdd_classEditor.text()
        line = line.strip()
        if line == "":
            QMessageBox.question(self, "Error", "No feature found", QMessageBox.Cancel)
        else:
            if not (db.addFeature_featureEditor(self.line_featureAdd_classEditor.text())):
                QMessageBox.question(self, "Error", "Feature already exist", QMessageBox.Cancel)
        self.updateData()

    def deleteFeature(self):
        db.deleteFeature_featureEditor(self.comboBox_featureDelete_featureEditor.currentText())
        self.updateData()


    def getAllFeatures(self):
        return db.getAllFeatures()

    def showAllFeatures(self):
        rows = self.getAllFeatures()
        self.text_featureExist_featureEditor.clear()
        for row in rows:
            self.text_featureExist_featureEditor.append(row["NameFeature"])

    def goto_return(self):
        self.parent().show()
        self.close()
