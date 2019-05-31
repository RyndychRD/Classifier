from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit

import layouts.detectClassSetFeature as design
import connectionToDatabase as db
import detectClass.detectClassResult as next


class detectClassSetFeatures(QtWidgets.QMainWindow, design.Ui_setFeature):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.listFeatures = []
        self.featureSet = {}
        self.show_next = next.detectClassResult(self);

        self.button_goBack_setFeature.clicked.connect(self.goto_return)
        self.comboBox_featureChoose_setFeature.activated.connect(self.takeTypeOfFeature)
        self.button_featureSet_setFeature.clicked.connect(self.setFeature)
        self.button_ok_setFeature.clicked.connect(self.goto_next)

    def getDouble(self):
        d, okPressed = QInputDialog.getDouble(self, "Set double value for dimensional value", "Value:", 0, -100000000,
                                              1000000000, 3)
        if okPressed:
            return d

    def goto_next(self):
        if len(self.featureSet)==0:
            QMessageBox.question(self, "Error", " You have to input 1 or more value",
                                 QMessageBox.Cancel)
            return
        self.show_next.inst(self.featureSet)
        self.show_next.show()
        self.hide()

    def getChoice(self):
        res = db.showAllScalarFeatureDef(self.comboBox_featureChoose_setFeature.currentText())
        items = ()
        for x in res:
            items += (x["Value"],)
        items = list(set(items))
        item, okPressed = QInputDialog.getItem(self, "Get item for scalar value", "Value:", items, 0, False)
        if okPressed and item:
            return item

    def getChoiceLogical(self):
        res = db.getAllLogical()
        items = ()
        for x in res:
            items += (x["True_Value"],)
            items += (x["False_Value"],)

        items = list(set(items))
        item, okPressed = QInputDialog.getItem(self, "Get item for logical value", "Value:", items, 0, False)
        if okPressed and item:
            return item

    def setFeature(self):
        feature = self.comboBox_featureChoose_setFeature.currentText()
        if feature is "":
            return
        featureType = db.takeTypeOfFeature(feature)
        if featureType['Type'] == 1:
            self.featureSet[feature] = self.getChoice()
        if featureType['Type'] == 2:
            self.featureSet[feature] = self.getChoiceLogical()
        if featureType['Type'] == 3:
            self.featureSet[feature] = self.getDouble()

        self.text_featureSet_setFeature.append(feature)
        for x in self.listFeatures:
            if x["NameFeature"] == feature:
                self.listFeatures.remove(x)
        self.text_featureUnset_setFeature.clear()
        self.comboBox_featureChoose_setFeature.clear()
        for x in self.listFeatures:
            self.text_featureUnset_setFeature.append(x["NameFeature"])
            self.comboBox_featureChoose_setFeature.addItem(x["NameFeature"])
        self.takeTypeOfFeature()

    def inst(self, listFeatures):
        self.comboBox_featureChoose_setFeature.clear()
        self.text_featureSet_setFeature.clear()
        self.text_featureUnset_setFeature.clear()

        for x in listFeatures:
            self.comboBox_featureChoose_setFeature.addItem(x["NameFeature"])
            self.text_featureUnset_setFeature.append(x["NameFeature"])
        self.listFeatures = listFeatures
        self.comboBox_featureChoose_setFeature.setCurrentText(listFeatures[0]["NameFeature"])
        self.takeTypeOfFeature()

    def takeTypeOfFeature(self):
        self.line_featureType_setFeature.clear()
        feature = self.comboBox_featureChoose_setFeature.currentText()
        if feature is "":
            return
        featureType = db.takeTypeOfFeature(feature)
        if featureType['Type'] == 1:
            self.line_featureType_setFeature.setText("Скалярный")
            return 1
        if featureType['Type'] == 2:
            self.line_featureType_setFeature.setText("Логический")
            return 2
        if featureType['Type'] == 3:
            self.line_featureType_setFeature.setText("Размерный")
            return 3
        return -1

    def goto_return(self):
        self.parent().inst()
        self.parent().show()
        self.close()
