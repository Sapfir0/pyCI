#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

from build import testsWindow 
from build import res #ресурс файл

import tests.node.script

class testing(QtWidgets.QMainWindow, tests.Ui_MainWindow):
    def __init__(self): #конструктор еб
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.complete.setPixmap(QPixmap(":/images/icons8-cancel-16.png"))

    


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = testing()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
 
