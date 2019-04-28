#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

from build import mainwindow,res  # Это наш конвертированный файл дизайна
import os,subprocess 
from subprocess import Popen, PIPE
#import testsWindow

class PyCi(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self): #конструктор еб
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.changeDir.clicked.connect(self.browseFolder)
        self.changeDir2.setVisible(False)

        self.changeDir2.clicked.connect(self.browseFolder)
        #self.goToTestBtn.clicked.connect(self.goToTest)

        self.tests.currentIndexChanged.connect(self.testing)
        self.complete.setPixmap(QPixmap(":/images/icons8-cancel-16.png"))
        self.arrow.setPixmap(QPixmap(":/images/icons8-right-16.png"))


    # def goToTest(self):
    #     self.w2 = testing()
    #     self.w2.show()

    def browseFolder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select project folder")
        def complete(self, var): 
            self.dir.setText(directory)
            self.changeDir2.setVisible(var)
            self.changeDir.setVisible(not var)
            if (var == True):   
                self.complete.setPixmap(QPixmap(":/images/icons8-checked-16.png"))
            else: 
                self.complete.setPixmap(QPixmap(":/images/icons8-cancel-16.png"))
            self.dir.setEnabled(not var)
        
        if (directory != ''):
            complete(self, True)
        else:
            complete(self, False)

        #data = subprocess.Popen("git status", cwd=directory, stdout=PIPE).communicate() 
        #выдается кортеж, с первым аргументм
        #если удалось найти fatal, выдать ошибку
        #если нашли fatal, обрабатываем следующие слова и выдаем ошибку



    def testing(self): 
        if ( self.tests.currentText() == "Другое"):
            self.findedTest.setText("У нас нет тестов для тебя")
            self.goToTestBtn.setVisible(False) 
        elif ( self.tests.currentText() == "Node.js"):
            self.findedTest.setText("У нас есть тесты для тебя")
            self.goToTestBtn.setVisible(True) 
    


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = PyCi()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
 
