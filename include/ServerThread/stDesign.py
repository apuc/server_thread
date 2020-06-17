import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from design.main import Ui_MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Design()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


class Design(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

    def createDesign(self):
        window = Design()  # Создаём объект класса ExampleApp
        window.serverTableList.setHorizontalHeaderLabels(["Имя", "Путь"])
        window.serverTableList.setColumnCount(2)
        window.serverTableList.setRowCount(2)
        window.serverTableList.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        window.serverTableList.resizeColumnsToContents()
        window.show()  # Показываем окно
        self.app.exec_()  # и запускаем приложение