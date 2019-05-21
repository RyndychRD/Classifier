import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets

import layouts.knowledgeEditor as design

import knowledgeEditor.knowledgeEditorClassEditor as classEditor
import knowledgeEditor.knowledgeEditorFeatureEditor as featureEditor
import knowledgeEditor.knowledgeEditorFeaturePossibleDefinition as featurePossibleDef
import knowledgeEditor.knowledgeEditorClassExplanation as classExplanation


class knowledgeEditor(QtWidgets.QMainWindow, design.Ui_knowledgeEditor):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.show_classEditor = classEditor.classEditor(self)
        self.show_featureEditor = featureEditor.featureEditor(self)
        self.show_featurePossibleDef = featurePossibleDef.featurePossibleDefinition(self)
        self.show_classExplanation = classExplanation.classExplanation(self)

        self.button_classEditor_knowledgeEditor.clicked.connect(self.goto_classEditor)
        self.button_featureEditor_knowledgeEditor.clicked.connect(self.goto_featureEditor)
        self.button_goBack_knowledgeEditor.clicked.connect(self.goto_return)
        self.button_featurePossibleDefinition_knowledgeEditor.clicked.connect(self.goto_featurePossibleDef)
        self.button_classExplanation_knowledgeEditor.clicked.connect(self.goto_classExplanation)

    def goto_classExplanation(self):
        self.show_classExplanation.show()
        self.hide()

    def goto_featurePossibleDef(self):
        self.show_featurePossibleDef.show()
        self.hide()

    def goto_classEditor(self):
        self.show_classEditor.show()
        self.hide()

    def goto_featureEditor(self):
        self.show_featureEditor.show()
        self.hide()

    def goto_return(self):
        self.parent().show()
        self.close()
