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

        # self.takeAllFeatures()

        self.comboBox_classChoose_classExplanation.activated.connect(self.takeFeatureFromClass)
        self.button_goBack_classExplanation.clicked.connect(self.goto_return)
        self.button_addFeature_classExplanation.clicked.connect(self.addFeature)
        self.button_addAllFeatures_classExplanation.clicked.connect(self.addAllFeatures)
        self.button_deleteAllFeatures_classExplanation.clicked.connect(self.deleteAllFeatures)
        self.button_deleteFeature_classExplanation.clicked.connect(self.deleteFeature)
        self.button_ok_classExplanation.clicked.connect(self.goto_return)

    def goto_return(self):
        self.parent().show()
        self.close()

    def inst(self):
        rows = db.showAllClasses()
        self.comboBox_classChoose_classExplanation.clear()
        for row in rows:
            self.comboBox_classChoose_classExplanation.addItem(row["Class"])
        if self.comboBox_classChoose_classExplanation.count()>0:
            self.comboBox_classChoose_classExplanation.setCurrentText(rows[0]["Class"])
        self.takeFeatureFromClass()

    def updateData(self, featuresToAdd, featuresToDelete):
        self.comboBox_addFeature_classExplanation.clear()
        for row in featuresToAdd:
            self.comboBox_addFeature_classExplanation.addItem(row["NameFeature"])

        self.comboBox_deleteFeature_classExplanation.clear()
        self.text_featuresList_classExplanation.clear()
        if not featuresToDelete == None:
            for row in featuresToDelete:
                self.comboBox_deleteFeature_classExplanation.addItem(row["NameFeature"])
                self.text_featuresList_classExplanation.append(row["NameFeature"])

    def addFeature(self, featureName=""):
        className = self.comboBox_classChoose_classExplanation.currentText()
        if not featureName:
            featureName = self.comboBox_addFeature_classExplanation.currentText()
        db.addFeatureToClass_classExplanation(featureName, className)
        if not self.featureToAdd == None:
            for row in self.featureToAdd:
                if row["NameFeature"] == featureName:
                    self.featureToDelete.append(row)
                    self.featureToAdd.remove(row)
            self.updateData(self.featureToAdd, self.featureToDelete)

    def deleteFeature(self, featureName=""):
        className = self.comboBox_classChoose_classExplanation.currentText()
        if not featureName:
            featureName = self.comboBox_deleteFeature_classExplanation.currentText()
        db.deleteFeatureFromClass_classExplanation(featureName, className)

        if not self.featureToDelete==None:
            for row in self.featureToDelete:
                if row["NameFeature"] == featureName:
                    self.featureToAdd.append(row)
                    self.featureToDelete.remove(row)
            self.updateData(self.featureToAdd, self.featureToDelete)

    def takeFeatureFromClass(self):
        self.featureToDelete = db.takeFeautureFromClass_classExplanation(
            self.comboBox_classChoose_classExplanation.currentText())
        self.featureToAdd = db.showAllFeatures_classExplanation()
        if not self.featureToDelete == None:
            if len(self.featureToDelete) > 0:
                for x in self.featureToDelete:
                    if x in self.featureToAdd:
                        self.featureToAdd.remove(x)
            self.updateData(self.featureToAdd, self.featureToDelete)

    def addAllFeatures(self):
        self.takeFeatureFromClass()
        featureTemp = []
        for x in self.featureToAdd:
            featureTemp += {x["NameFeature"]}
        for x in featureTemp:
            self.addFeature(x)

    def deleteAllFeatures(self):
        self.takeFeatureFromClass()
        featureTemp = []
        for x in self.featureToDelete:
            featureTemp += {x["NameFeature"]}
        for x in featureTemp:
            self.deleteFeature(x)
