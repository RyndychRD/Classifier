from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import layouts.knowledgeEditorClassExplanation as design
import connectionToDatabase as db


class classExplanation(QtWidgets.QMainWindow, design.Ui_classExplanation):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.featuresAll = []
        self.featureToAdd = []
        self.featureToDelete = []
        self.inst()

        self.takeAllFeatures()

        self.comboBox_classChoose_classExplanation.activated.connect(self.takeFeatureFromClass)
        self.button_goBack_classExplanation.clicked.connect(self.goto_return)
        self.button_addFeature_classExplanation.clicked.connect(self.addFeature)
        self.button_addAllFeatures_classExplanation.clicked.connect(self.addAllFeatures)
        self.button_deleteAllFeatures_classExplanation.clicked.connect(self.deleteAllFeatures)
        self.button_deleteFeature_classExplanation.clicked.connect(self.deleteFeature)

    def goto_return(self):
        self.parent().show()
        self.close()

    def inst(self):
        rows = db.showAllClasses()
        self.comboBox_classChoose_classExplanation.clear()
        for row in rows:
            self.comboBox_classChoose_classExplanation.addItem(row["Class"])

    def updateData(self, featuresToAdd, featuresToDelete):
        self.comboBox_addFeature_classExplanation.clear()
        for row in featuresToAdd:
            self.comboBox_addFeature_classExplanation.addItem(row["NameFeature"])

        self.comboBox_deleteFeature_classExplanation.clear()
        self.text_featuresList_classExplanation.clear()
        for row in featuresToDelete:
            self.comboBox_deleteFeature_classExplanation.addItem(row["NameFeature"])
            self.text_featuresList_classExplanation.append(row["NameFeature"])



    def takeAllFeatures(self):
        self.featuresAll = db.showAllFeatures()
        self.featureToAdd = self.featuresAll
        self.updateData(self.featureToAdd, self.featureToDelete)


    def addFeature(self):
        className = self.comboBox_classChoose_classExplanation.currentText()
        featureName = self.comboBox_addFeature_classExplanation.currentText()
        db.addFeatureToClass_classExplanation(featureName, className)

        for row in self.featureToAdd:
            if row["NameFeature"] == featureName:
                self.featureToDelete.append(row)
                self.featureToAdd.remove(row)
        self.updateData(self.featureToAdd,self.featureToDelete)

    def deleteFeature(self):
        className = self.comboBox_classChoose_classExplanation.currentText()
        featureName = self.comboBox_deleteFeature_classExplanation.currentText()
        db.deleteFeatureFromClass_classExplanation(featureName,className)

        for row in self.featureToDelete:
            if row["NameFeature"] == featureName:
                self.featureToAdd.append(row)
                self.featureToDelete.remove(row)
        self.updateData(self.featureToAdd,self.featureToDelete)

    def takeFeatureFromClass(self):
        featuresToDelete=db.takeFeautureFromClass_classExplanation(self.comboBox_classChoose_classExplanation.currentText())
        self.takeAllFeatures()
        if len(featuresToDelete)>0:
            self.featureToAdd=list(set(self.featureToAdd)-set(featuresToDelete))
        self.updateData(self.featureToAdd,featuresToDelete)

    def addAllFeatures(self):
        print()

    def deleteAllFeatures(self):
        print()
