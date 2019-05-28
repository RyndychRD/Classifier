from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import layouts.checkOfFullness as design
import connectionToDatabase as db


class checkFullness(QtWidgets.QMainWindow, design.Ui_checkOfFullness):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.button_ok_checkFullness.hide()
        self.button_goBack_checkFullness.clicked.connect(self.goto_return)
        self.button_ok_checkFullness.clicked.connect(self.goto_next)

    def checkFullness(self):
        self.text_checkFullness.clear()
        self.button_ok_checkFullness.hide()
        rows = db.getAllClassFeature_pair()
        checkComplete = True
        for x in rows:
            if not db.isSet(x["idFeature_Class_pair"]):
                checkComplete = False
                className = db.getClassById(x["Classes_idClasses"])
                featureName = db.getFeatureById(x["Feature_idFeature"])
                if className == None:
                    self.text_checkFullness.append("No class was added to any feature")
                    return
                if featureName == None:
                    self.text_checkFullness.append("No feature was added to any class")
                    return

                self.text_checkFullness.append("In class " + str(className["Class"]) + " the feature " +
                                               str(featureName["NameFeature"]) + " was assigned but wasn't set")
        if checkComplete:
            self.text_checkFullness.append("Everything correct, you can continue")
            self.button_ok_checkFullness.show()

    def goto_next(self):
        print();

    def goto_return(self):
        self.parent().show()
        self.close()
