from PyQt5 import QtWidgets


import layouts.detectClassResult as design
import connectionToDatabase as db


class detectClassResult(QtWidgets.QMainWindow, design.Ui_result):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.listFeaturesToCheck=[]
        self.button_goBack_result.clicked.connect(self.goto_return)

    def returnRes(self):
        res=db.getAllClassesAndFeatureDeff()



    def inst(self,list):
        self.text_impossibleClasses_result.clear()
        self.line_possibleClass_result.clear()
        self.listFeaturesToCheck=list
        self.returnRes()

    def goto_return(self):
        self.parent().show()
        self.close()
