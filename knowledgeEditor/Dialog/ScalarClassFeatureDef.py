from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *

import layouts.knowledgeEditorScalarEdit_classFeatureDef as design
import connectionToDatabase as db


class Scalar(QtWidgets.QMainWindow, design.Ui_scalarEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.FeatureName = ""
        self.FeatureId = ""
        self.idFeatureClass = ""

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.listWidget_ScalarEdit.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.button_goBack_scalarEdit.clicked.connect(self.goto_return)
        self.button_ok_scalarEdit.clicked.connect(self.save_return)

    def inst(self, featureName, idFeatureClass):
        self.FeatureName = featureName
        self.idFeatureClass = idFeatureClass
        scalar = db.showAllScalarFeatureDef(self.FeatureName)
        db.deleteScalar_FeatureClass_pair(self.idFeatureClass)
        for x in scalar:
            self.listWidget_ScalarEdit.addItem(x["Value"])
    def deleteFeature(self,idFeatureClass):
        db.deleteScalar_FeatureClass_pair(idFeatureClass)

    def save_return(self):
        for item in self.listWidget_ScalarEdit.selectedItems():
            print(item.text())
            db.setScalar_FeatureClass_pair(item.text(), self.idFeatureClass)
        self.listWidget_ScalarEdit.clear()
        self.parent().showSetFeature()
        self.parent().showUnSetFeature()
        self.parent().getValueOfFeature()
        self.parent().show()
        self.close()

    def goto_return(self):
        QMessageBox.question(self, "Error", " You have to input values. No way back",
                             QMessageBox.Cancel)
