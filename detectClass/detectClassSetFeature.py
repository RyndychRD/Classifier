from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import layouts.detectClassSetFeature as design
import connectionToDatabase as db


class detectClassSetFeatures(QtWidgets.QMainWindow, design.Ui_setFeature):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.listFeatures = []

    def inst(self, listFeatures):
        self.comboBox_featureChoose_setFeature.clear()
        self.text_featureSet_setFeature.clear()
        self.text_featureUnset_setFeature.clear()
        for x in listFeatures:
            self.comboBox_featureChoose_setFeature.addItem(x["NameFeature"])
        self.listFeatures = listFeatures

    def goto_return(self):
        self.parent().show()
        self.close()
