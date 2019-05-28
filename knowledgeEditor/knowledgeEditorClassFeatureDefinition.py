from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import layouts.knowledgeEditorClassFeatureDefinition as design
import connectionToDatabase as db
import knowledgeEditor.Dialog.ScalarClassFeatureDef as ScalarEdit
import knowledgeEditor.Dialog.LogicalClassFeatureDef as LogicalEdit


class classFeatureDefinition(QtWidgets.QMainWindow, design.Ui_classFeatureDefinition):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.featureOfClass = []
        self.inst()
        self.show_ScalarEditor = ScalarEdit.Scalar(self)
        self.show_LogicalEditor = LogicalEdit.Logical(self)

        self.comboBox_classChoose_classFeatureDefinition.activated.connect(self.takeFeaturesFromClass)
        self.button_goBack_classFeatureDefinition.clicked.connect(self.goto_return)
        self.comboBox_featureChoose_classFeatureDefinition.activated.connect(self.takeTypeOfFeature)
        self.button_ok_classFeatureDefinition.clicked.connect(self.goto_return)
        self.comboBox_classChoose_classFeatureDefinition.activated.connect(self.showSetFeature)
        self.comboBox_classChoose_classFeatureDefinition.activated.connect(self.showUnSetFeature)
        self.button_featureSet_classFeatureDefinition_2.clicked.connect(self.setFeatureDef)
        self.button_featureUnSet_classFeatureDefinition.clicked.connect(self.unsetFeatureDef)

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
            self.takeTypeOfFeature()
            return features
        else:
            return []

    def setFeatureDef(self):
        featureType = self.takeTypeOfFeature()
        if featureType == 1:
            self.goto_ScalarEdit()
        if featureType == 2:
            self.goto_LogicalEdit()
        if featureType == 3:
            self.goto_DimensionalEdit()

    def goto_ScalarEdit(self):
        self.show_ScalarEditor.inst(self.comboBox_featureChoose_classFeatureDefinition.currentText(),
                                    db.getIdFeatureClass_pairByClassNameFeatureName(
                                        self.comboBox_featureChoose_classFeatureDefinition.currentText(),
                                        self.comboBox_classChoose_classFeatureDefinition.currentText()))
        self.show_ScalarEditor.show()
        self.hide()

    def goto_LogicalEdit(self):
        self.show_LogicalEditor.inst(self.comboBox_featureChoose_classFeatureDefinition.currentText(),
                                    db.getIdFeatureClass_pairByClassNameFeatureName(
                                        self.comboBox_featureChoose_classFeatureDefinition.currentText(),
                                        self.comboBox_classChoose_classFeatureDefinition.currentText()))
        self.show_LogicalEditor.show()
        self.hide()


    def goto_DimensionalEdit(self):
        print()

    def unsetFeatureDef(self):
        print()

    def showSetFeature(self):

        print("word")

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

    def takeTypeOfFeature(self):
        self.line_featureType_classFeatureDefinition.clear()
        feature = self.comboBox_featureChoose_classFeatureDefinition.currentText()
        featureType = db.takeTypeOfFeature(feature)
        if featureType['Type'] == 1:
            self.line_featureType_classFeatureDefinition.setText("Скалярный")
            return 1
        if featureType['Type'] == 2:
            self.line_featureType_classFeatureDefinition.setText("Логический")
            return 2
        if featureType['Type'] == 3:
            self.line_featureType_classFeatureDefinition.setText("Размерный")
            return 3
        return -1

    def goto_return(self):
        self.parent().show()
        self.close()
