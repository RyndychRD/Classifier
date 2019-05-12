import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets

import layouts.knowledgeEditor as design
import knowledgeEditor.knowledgeEditorClassEditor as classEditor


class knowledgeEditor(QtWidgets.QMainWindow, design.Ui_knowledgeEditor):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.show_classEditor = classEditor.classEditor()

        self.button_classEditor_knowledgeEditor.clicked.connect(self.goto_classEditor)
        self.button_goBack_knowledgeEditor.clicked.connect(self.goto_return)



    def goto_classEditor(self):
        self.show_classEditor.show()
        self.hide()

    def goto_return (self):
        self.parent().show()
        self.close()


