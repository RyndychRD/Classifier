from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import layouts.knowledgeEditorClassFeatureDefinition as design
import connectionToDatabase as db


class classFeatureDefinition(QtWidgets.QMainWindow, design.Ui_classFeatureDefinition):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.featureOfClass = []
        self.inst()

        self.comboBox_classChoose_classFeatureDefinition.activated.connect(self.takeFeaturesFromClass)
        self.button_goBack_classFeatureDefinition.clicked.connect(self.goto_return)
        self.button_ok_classFeatureDefinition.clicked.connect(self.goto_return)
        self.comboBox_classChoose_classFeatureDefinition.activated.connect(self.showSetFeature)
        self.comboBox_classChoose_classFeatureDefinition.activated.connect(self.showUnSetFeature)

    def inst(self):
        self.comboBox_classChoose_classFeatureDefinition.clear()
        classes = db.showAllClasses()
        for row in classes:
            self.comboBox_classChoose_classFeatureDefinition.addItem(row["Class"])
        self.comboBox_classChoose_classFeatureDefinition.setCurrentText(classes[0]["Class"])
        self.takeFeaturesFromClass()
        self.showSetFeature()
        self.showUnSetFeature()

    def takeFeaturesFromClass(self):
        self.comboBox_featureChoose_classFeatureDefinition.clear()
        features = db.takeFeautureFromClass_classExplanation(
            self.comboBox_classChoose_classFeatureDefinition.currentText())
        if len(features) > 0:
            for row in features:
                self.comboBox_featureChoose_classFeatureDefinition.addItem(row["NameFeature"])
            self.comboBox_featureChoose_classFeatureDefinition.setCurrentText(features[0]["NameFeature"])
            self.takeTypeOfFeature(self.comboBox_featureChoose_classFeatureDefinition.currentText())
            return features
        else:
            return []

    def showSetFeature(self):
        print()

    def showUnSetFeature(self):
        self.text_featureUnset_classFeatureDefinition.clear()
        AllFeatures = self.takeFeaturesFromClass()
        if len(AllFeatures) > 0:
            for row in AllFeatures:
                self.text_featureUnset_classFeatureDefinition.append(row["NameFeature"])

    #
    # if row["Type"] == 1:
    #     return 'Scalar'
    # if row["Type"] == 2:
    #     return 'Logical'
    # if row["Type"] == 3:
    #     return 'Dimensional'

    def takeTypeOfFeature(self, feature=""):
        self.line_featureType_classFeatureDefinition.clear()
        if not feature:
            feature = self.comboBox_featureChoose_classFeatureDefinition.currentText()
        featureType = db.takeTypeOfFeature(feature)
        if featureType['Type'] == 1:
            self.line_featureType_classFeatureDefinition.setText("Скалярный")
        if featureType['Type'] == 2:
            self.line_featureType_classFeatureDefinition.setText("Логический")
        if featureType['Type'] == 3:
            self.line_featureType_classFeatureDefinition.setText("Размерный")

    def goto_return(self):
        self.parent().show()
        self.close()
