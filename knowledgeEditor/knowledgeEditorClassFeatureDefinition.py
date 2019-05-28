from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import layouts.knowledgeEditorClassFeatureDefinition as design
import connectionToDatabase as db


class classFeatureDefinition(QtWidgets.QMainWindow, design.Ui_classFeatureDefinition):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.button_goBack_classFeatureDefinition.clicked.connect(self.goto_return)
        self.button_ok_classFeatureDefinition.clicked.connect(self.goto_return)

    def goto_return(self):
        self.parent().show()
        self.close()