import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets

import layouts.mainWindow as design

import knowledgeEditor.knowledgeEditor as knowledgeEditor
import detectClass.checkFullness as checkFullness


class mainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show_knowledgeEditor = knowledgeEditor.knowledgeEditor(self)
        self.show_checkFullness=checkFullness.checkFullness(self)

        self.buton_knowledgeEditor_MainWindow.clicked.connect(self.goto_knowledgeEditor)
        self.button_detectClass_MainWindow.clicked.connect(self.goto_checkFullness)

    def goto_knowledgeEditor(self):
        self.show_knowledgeEditor.show()
        self.hide()

    def goto_checkFullness(self):
        self.show_checkFullness.checkFullness()
        self.show_checkFullness.show()
        self.hide()



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = mainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main()
