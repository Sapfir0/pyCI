#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

from build import testingWindow 
from build import res #ресурс файл

#import tests.node.script
from tests.node.script import stressUsers, stessArticles

class testingWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self): #конструктор еб
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.complete.setPixmap(QPixmap(":/images/icons8-unavailable-16.png"))
        self.startStress.clicked.connect(self.startStress)
        self.errors.setVisible(False)
        


    def startStress(self):
        self.errors.setVisible(True)
        stressUsers()
        
        stessArticles()
        #self.errors.set#выставить иконки процесса, выполнения и провала

        


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = testing()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
 
