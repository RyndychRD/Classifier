from PyQt5 import QtWidgets

import layouts.detectClassResult as design
import connectionToDatabase as db


class detectClassResult(QtWidgets.QMainWindow, design.Ui_result):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.features = []
        self.maxClass = 0
        self.listFeaturesToCheck = []
        self.button_goBack_result.clicked.connect(self.goto_return)

    def checkOneClass(self, oneClass):
        classFeatures = db.getFeautureFromClass_classExplanation(oneClass["Class"])
        isThisClass = True
        currentClass = 0
        for x in classFeatures:
            currentFeature = x["NameFeature"]
            if currentFeature in self.listFeaturesToCheck:
                if x["Type"] == 1:
                    featurePairId = db.getIdFeatureClass_pairByClassNameFeatureName(currentFeature, oneClass["Class"])
                    featureDifFromClass = db.getClassFeatureDefById_Scalar(featurePairId)
                    isThisClass = False
                    for y in featureDifFromClass:
                        if self.listFeaturesToCheck[currentFeature] == y["Value"]:
                            isThisClass = True
                            currentClass += 1
                    if not isThisClass:
                        self.text_impossibleClasses_result.append("Class " + oneClass["Class"] +
                                                                  " is impossible because feature " + currentFeature +
                                                                  " is not in scalar values for this class")

                if x["Type"] == 2:
                    featurePairId = db.getIdFeatureClass_pairByClassNameFeatureName(currentFeature, oneClass["Class"])
                    featureDifFromClass = db.getClassFeatureDefById_Logical(featurePairId)
                    currentClass += 1
                    if not (self.listFeaturesToCheck[currentFeature] == featureDifFromClass["True_Value"]
                            or self.listFeaturesToCheck[currentFeature] == featureDifFromClass["False_Value"]):
                        isThisClass = False
                        self.text_impossibleClasses_result.append("Class " + oneClass["Class"] +
                                                                  " is impossible because feature " + currentFeature +
                                                                  " is not in true or false for this class")

                if x["Type"] == 3:
                    featurePairId = db.getIdFeatureClass_pairByClassNameFeatureName(currentFeature, oneClass["Class"])
                    featureDifFromClass = db.getClassFeatureDefById_Dimensional(featurePairId)
                    currentClass += 1
                    if not (float(featureDifFromClass["LeftValue"]) <=
                            float(self.listFeaturesToCheck[currentFeature])
                            <=
                            float(featureDifFromClass["RightValue"])):
                        isThisClass = False
                        self.text_impossibleClasses_result.append("Class " + oneClass["Class"] +
                                                                  " is impossible because feature " + currentFeature +
                                                                  " is not in " +
                                                                  str(featureDifFromClass["LeftValue"]) + ".." +
                                                                  str(featureDifFromClass["RightValue"]))
            currentFeature = ""
        if isThisClass:
            if currentClass > self.maxClass:
                self.line_possibleClass_result.clear()
                self.line_possibleClass_result.setText(oneClass["Class"])
                self.maxClass = currentClass

    def returnRes(self):
        classes = db.getAllClasses()
        self.features = db.getAllFeatures()
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
