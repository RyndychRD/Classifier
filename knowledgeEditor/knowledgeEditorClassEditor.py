from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import layouts.knowledgeEditorClassEditor as design
import connectionToDatabase as db


class classEditor(QtWidgets.QMainWindow, design.Ui_classEditor):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.updateData()

        self.button_classAdd_classEditor.clicked.connect(self.addClass)
        self.button_goBack_classEditor.clicked.connect(self.goto_return)
        self.button_classDelete_classEditor.clicked.connect(self.deleteClass)

    def addClass(self):
        line = self.line_classAdd_classEditor.text()
        line = line.strip()
        if line == "":
            QMessageBox.question(self, "Error", "No class found", QMessageBox.Cancel)
        else:
            if not (db.addClass_classEditor(self.line_classAdd_classEditor.text())):
                QMessageBox.question(self, "Error", "Class already exist", QMessageBox.Cancel)
        self.updateData()

    def updateData(self):
        self.line_classAdd_classEditor.clear()
        self.comboBox_classDelete_classEditor.clear()
        for row in self.getAllClasses():
            self.comboBox_classDelete_classEditor.addItem(row["Class"])
        self.showAllClasses()

    def deleteClass(self):

        db.deleteClass_classEditor(self.comboBox_classDelete_classEditor.currentText())
        self.updateData()

    def getAllClasses(self):
        return db.getAllClasses()

    def showAllClasses(self):
        rows = self.getAllClasses()
        self.text_classExist_classEditor.clear()
        for row in rows:
            self.text_classExist_classEditor.append(row["Class"])

    def goto_return(self):
        self.parent().show()
        self.close()
