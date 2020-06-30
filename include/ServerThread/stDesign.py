import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from design.main import Ui_MainWindow


class Design(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.pool = []
        self.app = QtWidgets.QApplication(sys.argv)
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

    def createDesign(self, servers):
        self.window = Design()  # Создаём объект класса ExampleApp
        self.window.serverTableList.setHorizontalHeaderLabels(["ID", "Путь", "Порт"])
        self.window.serverTableList.setRowCount(len(servers))

        i = 0
        for server in servers:
            self.window.serverTableList.setItem(i, 0, QTableWidgetItem(server["id"]))
            self.window.serverTableList.setItem(i, 1, QTableWidgetItem(server["path"]))
            self.window.serverTableList.setItem(i, 2, QTableWidgetItem(str(server["port"])))
            i = i + 1

        self.window.serverTableList.resizeColumnsToContents()

        self.window.startBtn.clicked.connect(self.runServer)
        self.window.stopBtn.clicked.connect(self.stopServer)

        self.window.show()  # Показываем окно
        self.app.exec_()  # и запускаем приложение

    def setPool(self, pool):
        self.pool = pool

    def runServer(self):
        row = self.window.serverTableList.currentItem().row()
        id = self.window.serverTableList.item(row, 0).text()
        thread = self.pool.find(id)
        thread.thread.start()

    def stopServer(self):
        row = self.window.serverTableList.currentItem().row()
        id = self.window.serverTableList.item(row, 0).text()
        thread = self.pool.find(id)
        thread.thread.stop()