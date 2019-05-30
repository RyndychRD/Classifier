from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import layouts.detectClassInputFeatures as design
import connectionToDatabase as db
import detectClass.detectClassSetFeature as next


class detectClassInputFeatures(QtWidgets.QMainWindow, design.Ui_inputFeatures):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.featureToAdd = []
        self.featureToDelete = []
        self.AllFeatures = []
        self.show_next = next.detectClassSetFeatures(self)

        self.button_addFeature_inputFeatures.clicked.connect(self.addFeature)
        self.button_deleteFeature_inputFeatures.clicked.connect(self.deleteFeature)
        self.button_ok_inputFeatures.clicked.connect(self.goto_next)
        self.button_goBack_inputFeatures.clicked.connect(self.goto_return)

    def addFeature(self):
        currentName = self.comboBox_addFeature_inputFeatures.currentText()
        if currentName == "":
            return
        currentFeature = []
        for x in self.featureToAdd:
            if x["NameFeature"] == currentName:
                currentFeature = x
        self.featureToAdd.remove(currentFeature)
        self.featureToDelete.append(currentFeature)
        self.updateData()

    def updateData(self):
        self.text_featuresList_inputFeatures.clear()
        self.comboBox_addFeature_inputFeatures.clear()
        self.comboBox_deleteFeature_inputFeatures.clear()
        for x in self.featureToAdd:
            self.comboBox_addFeature_inputFeatures.addItem(x["NameFeature"])
        for x in self.featureToDelete:
            self.comboBox_deleteFeature_inputFeatures.addItem(x["NameFeature"])
            self.text_featuresList_inputFeatures.append(x["NameFeature"])

    def deleteFeature(self):
        currentName = self.comboBox_deleteFeature_inputFeatures.currentText()
        if currentName == "":
            return
        currentFeature = []
        for x in self.featureToDelete:
            if x["NameFeature"] == currentName:
                currentFeature = x
        self.featureToAdd.append(currentFeature)
        self.featureToDelete.remove(currentFeature)
        self.updateData()

    def goto_next(self):
        self.show_next.inst(self.featureToDelete)
        self.show_next.show()
        self.hide()

    def inst(self):
        self.comboBox_addFeature_inputFeatures.clear()
        self.comboBox_deleteFeature_inputFeatures.clear()
        self.text_featuresList_inputFeatures.clear()
        self.featureToDelete.clear()
        self.featureToAdd=[]
        self.AllFeatures = db.getAllFeatures()
        for x in self.AllFeatures:
            self.comboBox_addFeature_inputFeatures.addItem(x["NameFeature"])
        self.featureToAdd = self.AllFeatures
        self.comboBox_addFeature_inputFeatures.setCurrentText(self.AllFeatures[0]["NameFeature"])

    def goto_return(self):
        self.parent().show()
        self.close()
