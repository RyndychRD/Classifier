from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import layouts.knowledgeEditorClassEditor as design
import connectionToDatabase as db


class classEditor(QtWidgets.QMainWindow, design.Ui_classEditor):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


        self.button_classAdd_classEditor.clicked.connect(self.addClass)
        self.button_goBack_classEditor.clicked.connect(self.goto_return)


    def addClass(self):
        line = self.line_classAdd_classEditor.text()
        line = line.strip()
        if line == "":

            QMessageBox.question(self, "Error", "No class found", QMessageBox.Cancel)

        else:
            db.addClass(self.line_classAdd_classEditor.text())

    def deleteClass(self):
        print()

    def goto_return(self):
        self.parent().show()
        self.close()
