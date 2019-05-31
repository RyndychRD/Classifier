from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import layouts.knowledgeEditorClassFeatureDefinition as design
import connectionToDatabase as db
import knowledgeEditor.Dialog.ScalarClassFeatureDef as ScalarEdit
import knowledgeEditor.Dialog.LogicalClassFeatureDef as LogicalEdit
import knowledgeEditor.Dialog.DimensionalClassFeatureDef as DimensionalEdit


class classFeatureDefinition(QtWidgets.QMainWindow, design.Ui_classFeatureDefinition):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.featureOfClass = []
        self.inst()
        self.show_ScalarEditor = ScalarEdit.Scalar(self)
        self.show_LogicalEditor = LogicalEdit.Logical(self)
        self.show_DimensionalEditor = DimensionalEdit.Dimensional(self)

        self.comboBox_classChoose_classFeatureDefinition.activated.connect(self.takeFeaturesFromClass)
        self.button_goBack_classFeatureDefinition.clicked.connect(self.goto_return)
        self.comboBox_featureChoose_classFeatureDefinition.activated.connect(self.takeTypeOfFeature)
        self.comboBox_featureChoose_classFeatureDefinition.activated.connect(self.getValueOfFeature)
        self.button_ok_classFeatureDefinition.clicked.connect(self.goto_return)
        self.comboBox_classChoose_classFeatureDefinition.activated.connect(self.showSetFeature)
        self.comboBox_classChoose_classFeatureDefinition.activated.connect(self.showUnSetFeature)
        self.button_featureSet_classFeatureDefinition_2.clicked.connect(self.setFeatureDef)
        self.button_featureUnSet_classFeatureDefinition.clicked.connect(self.unsetFeatureDef)

    def inst(self):
        self.comboBox_classChoose_classFeatureDefinition.clear()
        classes = db.getAllClasses()
        for row in classes:
            self.comboBox_classChoose_classFeatureDefinition.addItem(row["Class"])
        if self.comboBox_classChoose_classFeatureDefinition.count() > 0:
            self.comboBox_classChoose_classFeatureDefinition.setCurrentText(classes[0]["Class"])
        self.takeFeaturesFromClass()
        self.getValueOfFeature()
        self.showSetFeature()
        self.showUnSetFeature()

    def takeFeaturesFromClass(self):
        self.comboBox_featureChoose_classFeatureDefinition.clear()
        features = db.getFeautureFromClass_classExplanation(
            self.comboBox_classChoose_classFeatureDefinition.currentText())
        if not features == None:
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
        self.show_DimensionalEditor.inst(self.comboBox_featureChoose_classFeatureDefinition.currentText(),
                                         db.getIdFeatureClass_pairByClassNameFeatureName(
                                             self.comboBox_featureChoose_classFeatureDefinition.currentText(),
                                             self.comboBox_classChoose_classFeatureDefinition.currentText()))
        self.show_DimensionalEditor.show()
        self.hide()

    def unsetFeatureDef(self):
        feature = self.comboBox_featureChoose_classFeatureDefinition.currentText()
        featureType = db.takeTypeOfFeature(feature)
        if featureType['Type'] == 1:
            self.show_ScalarEditor.deleteFeature(db.getIdFeatureClass_pairByClassNameFeatureName(
                                            self.comboBox_featureChoose_classFeatureDefinition.currentText(),
                                            self.comboBox_classChoose_classFeatureDefinition.currentText()))
            self.inst()
        if featureType['Type'] == 2:
            self.show_LogicalEditor.inst(self.comboBox_featureChoose_classFeatureDefinition.currentText(),
                                         db.getIdFeatureClass_pairByClassNameFeatureName(
                                             self.comboBox_featureChoose_classFeatureDefinition.currentText(),
                                             self.comboBox_classChoose_classFeatureDefinition.currentText()))
            self.inst()
        if featureType['Type'] == 3:
            self.show_DimensionalEditor.inst(self.comboBox_featureChoose_classFeatureDefinition.currentText(),
                                             db.getIdFeatureClass_pairByClassNameFeatureName(
                                                 self.comboBox_featureChoose_classFeatureDefinition.currentText(),
                                                 self.comboBox_classChoose_classFeatureDefinition.currentText()))
            self.inst()

    def showSetFeature(self):
        print()

    def showUnSetFeature(self):
        self.text_featureUnset_classFeatureDefinition.clear()
        self.text_featureSetted_classFeatureDefinition.clear()
        AllFeatures = self.takeFeaturesFromClass()
        if not AllFeatures==None:
            if len(AllFeatures) > 0:
                for row in AllFeatures:
                    if db.isSet(db.getIdFeatureClass_pairByClassNameFeatureName(
                            row["NameFeature"],
                            self.comboBox_classChoose_classFeatureDefinition.currentText())):
                        self.text_featureSetted_classFeatureDefinition.append(row["NameFeature"])
                    else:
                        self.text_featureUnset_classFeatureDefinition.append(row["NameFeature"])

    #
    # if row["Type"] == 1:
    #     return 'Scalar'
    # if row["Type"] == 2:
    #     return 'Logical'
    # if row["Type"] == 3:
    #     return 'Dimensional'

    def getValueOfFeature(self):
        self.text_Definition.clear()
        feature = self.comboBox_featureChoose_classFeatureDefinition.currentText()
        className=self.comboBox_classChoose_classFeatureDefinition.currentText()
        self.text_Definition.clear()
        featureType = db.takeTypeOfFeature(feature)
        idFeatureClass=db.getIdFeatureClass_pairByClassNameFeatureName(feature,className)
        if featureType is not None:
            if featureType['Type'] == 1:
                values = db.getClassFeatureDefById_Scalar(idFeatureClass)
                for x in values:
                    self.text_Definition.append(x["Value"])

            if featureType['Type'] == 2:
                values = db.getClassFeatureDefById_Logical(idFeatureClass)
                self.text_Definition.append("True value:=" + str(values["True_Value"]))
                self.text_Definition.append("False value:=" + str(values["False_Value"]))
            if featureType['Type'] == 3:
                values = db.getClassFeatureDefById_Dimensional(idFeatureClass)
                self.text_Definition.append(str(values["LeftValue"])+" <= Value for class <= " +str(values["RightValue"]))

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
