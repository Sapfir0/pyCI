#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

from build import mainwindow, res  # Это наш конвертированный файл дизайна
from testingWindow import testing
import os
from subprocess import Popen, PIPE


class PyCi(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self): #конструктор еб
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.changeDir.clicked.connect(self.browseFolder)
        self.changeDir2.setVisible(False)

        self.changeDir2.clicked.connect(self.browseFolder)
        self.goToTestBtn.clicked.connect(self.goToTest)

        self.tests.currentIndexChanged.connect(self.testing)
        
        self.complete.setPixmap(QPixmap(":/images/icons8-cancel-16.png"))
        self.complete_2.setPixmap(QPixmap(":/images/icons8-cancel-16.png"))
        self.complete_3.setPixmap(QPixmap(":/images/icons8-cancel-16.png"))

        # def setImg(self, widget, pixmap, countSimilarWidget):
        #     for i in range(0, countSimilarWidget+1):
        #         #widget.setPixmap(QPixmap(pixmap))
        #         widget+=

        #setImg(self.arrow, "arrow", ":/images/icons8-right-16.png", 2)    
        self.arrow.setPixmap(QPixmap(":/images/icons8-right-16.png"))
        self.arrow_2.setPixmap(QPixmap(":/images/icons8-right-16.png"))

    def goToTest(self):
        # self.w2 = testing()
        # self.w2.show()
        myDialog = testing()
        

    def browseFolder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select project folder")
        def complete(self, bool, string=""): 
            self.dir.setText(directory)
            self.description.setText(string)
            self.changeDir2.setVisible(bool)
            self.changeDir.setVisible(not bool)
            if (bool  == True):   
                self.complete.setPixmap(QPixmap(":/images/icons8-checked-16.png"))
            else: 
                self.complete.setPixmap(QPixmap(":/images/icons8-cancel-16.png"))
            self.dir.setEnabled(not bool)
        
        if (directory != ''):
            complete(self, True)
        else:
            complete(self, False, "Директория не найдена")
            return

        data = subprocess.Popen("git status", cwd=directory, stdout=PIPE, stderr=PIPE).communicate() 
        
        string = ""
        for i in range(0, len(data)):
            string += str(data[i])
        print(string)
        print(string.find("fatal:"))

        if ( string.find("fatal:") != -1 ): #ух 
            complete(self, False, "Git репозиторий не найден")
        


    def testing(self): 
        if ( self.tests.currentText() == "Другое"):
            self.findedTest.setText("У нас нет тестов для тебя")
            self.goToTestBtn.setVisible(False) 
        elif ( self.tests.currentText() == "Node.js"):
            self.findedTest.setText("У нас есть тесты для тебя")
            self.goToTestBtn.setVisible(True) 

