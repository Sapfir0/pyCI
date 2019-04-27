#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

sys.path.insert(0, './build/mainwindow')
import mainwindow  # Это наш конвертированный файл дизайна
sys.path.insert(0, './build/res')
import res #ресурс файл
import os


class ExampleApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self): #конструктор еб
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.changeDir.clicked.connect(self.browseFolder)
        self.changeDir2.setVisible(False)
        
    def browseFolder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select project folder")
        self.dir.setText(directory)
        self.complete.setPixmap(QPixmap(":/images/icons8-checked-16.png"))


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
 
