from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import layouts.knowledgeEditorFeaturePossibleDefinition as design
import connectionToDatabase as db
import knowledgeEditor.Dialog.Logical as Logical
import knowledgeEditor.Dialog.Dimensional as Dimensional
import knowledgeEditor.Dialog.Scalar as Scalar


class featurePossibleDefinition(QtWidgets.QMainWindow, design.Ui_featurePossibleDefinition):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        for row in self.getAllFeatures():
            self.comboBox_featureChoose_featurePossibleDefinition.addItem(row["NameFeature"])
        self.typeCheckAndPut(self.comboBox_featureChoose_featurePossibleDefinition.currentText())
        self.show_Logical_featurePossibleDef = Logical.Logical(self)
        self.show_Dimensional_featurePossibleDef = Dimensional.Dimensional(self)
        self.show_Scalar_featurePossibleDef = Scalar.Scalar(self)

        self.button_goBack_featurePossibleDefinition.clicked.connect(self.goto_return)
        self.button_Ok_featurePossibleDefinition.clicked.connect(self.okButtonPressed)
        self.comboBox_featureChoose_featurePossibleDefinition.activated[str].connect(self.typeCheckAndPut)

    def typeCheckAndPut(self, text):
        answer = db.getTypeAlreadySelect(text)
        print(answer)

        for btn in [self.radioBut_logic_featurePossibleDefinition,
                    self.radioBut_dimensional_featurePossibleDefinition,
                    self.radioBut_scalar_featurePossibleDefinition]:
            btn.setAutoExclusive(False)
            btn.setChecked(False)
            btn.repaint()
            btn.setAutoExclusive(True)

        if answer == 'Scalar':
            self.radioBut_scalar_featurePossibleDefinition.setChecked(True)
            self.radioBut_dimensional_featurePossibleDefinition.setChecked(False)
            self.radioBut_logic_featurePossibleDefinition.setChecked(False)
            return
        if answer == 'Logical':
            self.radioBut_scalar_featurePossibleDefinition.setChecked(False)
            self.radioBut_dimensional_featurePossibleDefinition.setChecked(False)
            self.radioBut_logic_featurePossibleDefinition.setChecked(True)
            return
        if answer == 'Dimensional':
            self.radioBut_scalar_featurePossibleDefinition.setChecked(False)
            self.radioBut_dimensional_featurePossibleDefinition.setChecked(True)
            self.radioBut_logic_featurePossibleDefinition.setChecked(False)
            return

    def okButtonPressed(self):
        # TODO add cascad deletion if changed
        if self.radioBut_scalar_featurePossibleDefinition.isChecked():
            db.setTypeOfFeature(self.comboBox_featureChoose_featurePossibleDefinition.currentText(), "Scalar")
            self.goto_Scalar_featurePossibleDef()

        if self.radioBut_logic_featurePossibleDefinition.isChecked():
            db.setTypeOfFeature(self.comboBox_featureChoose_featurePossibleDefinition.currentText(), "Logical")
            self.goto_Logical_featurePossibleDef()

        if self.radioBut_dimensional_featurePossibleDefinition.isChecked():
            db.setTypeOfFeature(self.comboBox_featureChoose_featurePossibleDefinition.currentText(), "Dimensional")
            self.goto_Dimensional_featurePossibleDef()

    def goto_Logical_featurePossibleDef(self):
        self.show_Logical_featurePossibleDef.set_featureName(
            self.comboBox_featureChoose_featurePossibleDefinition.currentText())
        self.show_Logical_featurePossibleDef.clearData()
        self.show_Logical_featurePossibleDef.show()
        self.hide()

    def goto_Dimensional_featurePossibleDef(self):
        self.show_Dimensional_featurePossibleDef.set_featureName(
            self.comboBox_featureChoose_featurePossibleDefinition.currentText())
        self.show_Dimensional_featurePossibleDef.clearData()
        self.show_Dimensional_featurePossibleDef.show()
        self.hide()

    def goto_Scalar_featurePossibleDef(self):
        self.show_Scalar_featurePossibleDef.set_featureName(
            self.comboBox_featureChoose_featurePossibleDefinition.currentText())
        self.show_Scalar_featurePossibleDef.updateData()
        self.show_Scalar_featurePossibleDef.show()
        self.hide()

    def getAllFeatures(self):
        return db.showAllFeatures()

    def goto_return(self):
        self.parent().show()
        self.close()
