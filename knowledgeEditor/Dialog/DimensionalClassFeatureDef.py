from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *

import layouts.knowledgeEditorDimensionalEdit_classFeatureDef as design
import connectionToDatabase as db


class Dimensional(QtWidgets.QMainWindow, design.Ui_dimensionalEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.FeatureName = ""
        self.FeatureId = ""
        self.idFeatureClass = ""

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        self.button_goBack_dimensionalEdit.clicked.connect(self.goto_return)
        self.button_ok_dimensionalEdit.clicked.connect(self.save_return)

    def inst(self, featureName, idFeatureClass):
        self.FeatureName = featureName
        self.idFeatureClass = idFeatureClass
        leftAndRight = db.getDimensionalValueMinMax_FeatureClass_pair(db.getFeatureIdByFeatureName(featureName))
        self.spinbox_min.setMinimum(leftAndRight[0])
        self.spinbox_min.setMaximum(leftAndRight[1])
        self.spinbox_max.setMinimum(leftAndRight[0])
        self.spinbox_max.setMaximum(leftAndRight[1])
        db.deleteDimensionalValue_FeatureClass_pair(self.idFeatureClass)

    def deleteFeature(self, idFeatureClass):
        db.deleteDimensionalValue_FeatureClass_pair(idFeatureClass)

    def save_return(self):
        left = self.spinbox_min.text()
        right = self.spinbox_max.text()
        if float(right.replace(',', '.')) < float(left.replace(',', '.')):
            QMessageBox.question(self, "Error", " Right Value cannot be less then left (in case (left,right] too 8P )",
                                 QMessageBox.Cancel)
            return

        db.setDimensionalValue_FeatureClass_pair(self.idFeatureClass, left, right)
        self.parent().showSetFeature()
        self.parent().showUnSetFeature()
        self.parent().getValueOfFeature()
        self.parent().show()
        self.close()

    def goto_return(self):
        QMessageBox.question(self, "Error", " You have to input values. No way back",
                             QMessageBox.Cancel)
