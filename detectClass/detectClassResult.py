from PyQt5 import QtWidgets

import layouts.detectClassResult as design
import connectionToDatabase as db


class detectClassResult(QtWidgets.QMainWindow, design.Ui_result):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.features=[]
        self.listFeaturesToCheck = []
        self.button_goBack_result.clicked.connect(self.goto_return)

    def checkOneClass(self, oneClass):
        print(oneClass)
        print("\n")
        classFeatures=db.getFeautureFromClass_classExplanation(oneClass["Class"])
        print(classFeatures)

    def returnRes(self):
        classes = db.getAllClasses()
        self.features=db.getAllFeatures()
        print(classes)
        print("\n")
        for x in classes:
            self.checkOneClass(x)


    def inst(self, list):
        self.text_impossibleClasses_result.clear()
        self.line_possibleClass_result.clear()
        self.listFeaturesToCheck = list
        self.returnRes()

    def goto_return(self):
        self.parent().show()
        self.close()
