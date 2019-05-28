from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *

import layouts.knowledgeEditorLogicallEdit_classFeatureDef as design
import connectionToDatabase as db


class Logical(QtWidgets.QMainWindow, design.Ui_logicalEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.FeatureName = ""
        self.FeatureId = ""
        self.idFeatureClass = ""

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        self.button_goBack_logicalEdit.clicked.connect(self.goto_return)
        self.button_ok_logicalEdit.clicked.connect(self.save_return)

    def inst(self, featureName, idFeatureClass):
        self.FeatureName = featureName
        self.idFeatureClass = idFeatureClass
        lineTrueAndFalse = db.getLogicalTrueFalse_FeatureClass_pair(db.getFeatureIdByFeatureName(self.FeatureName))
        lineTrue = lineTrueAndFalse[0]
        lineFalse = lineTrueAndFalse[1]
        self.checkBox_false.setText(lineFalse)
        self.checkBox_true.setText(lineTrue)
        db.deleteLogical_FeatureClass_pair(self.idFeatureClass)

    def save_return(self):
        if not self.checkBox_false.isChecked() and not self.checkBox_true.isChecked():
            QMessageBox.question(self, "Error", " You have to input values. Just any. Pleeease",
                                 QMessageBox.Cancel)
            return
        if self.checkBox_false.isChecked() and not self.checkBox_true.isChecked():
            db.setLogicalTrueFalse_FeatureClass_pair(self.idFeatureClass, False, self.checkBox_false.text())
        if not self.checkBox_false.isChecked() and self.checkBox_true.isChecked():
            db.setLogicalTrueFalse_FeatureClass_pair(self.idFeatureClass, self.checkBox_true.text(), False)
        if self.checkBox_false.isChecked() and self.checkBox_true.isChecked():
            db.setLogicalTrueFalse_FeatureClass_pair(self.idFeatureClass, self.checkBox_true.text(),
                                                     self.checkBox_false.text())
        self.checkBox_true.setChecked(False)
        self.checkBox_false.setChecked(False)
        self.parent().showSetFeature()
        self.parent().showUnSetFeature()
        self.parent().show()
        self.close()

    def goto_return(self):
        QMessageBox.question(self, "Error", " You have to input values. No way back",
                             QMessageBox.Cancel)
