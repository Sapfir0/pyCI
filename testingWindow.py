#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon

from build import testingWindow 
from build import res #ресурс файл

from tests.node.script import stressUsers, stessArticles, getMethods
counter=0

class testing(QtWidgets.QMainWindow, testingWindow.Ui_MainWindow):
    def __init__(self): #конструктор еб
        super().__init__()
        self.setupUi(self)  
        self.complete.setPixmap(QPixmap(":/images/icons8-unavailable-16.png"))
        self.startStressBtn.clicked.connect(self.startStress)
        
        self.errors.setVisible(False)
        self.progressBar.setVisible(False)


    def startStress(self):
        if ( not getMethods):
            self.description.setText("Сайт не отвечает")

        self.errors.setVisible(True)
        self.progressBar.setVisible(True)

        #stressUsers(1000)
        #stessArticles(1000)
        data = "Проверяем доступность сайта", "Создаем юзеров", "Пишем статьи"
        def insertRows():
            for i in range(0,len(data)):
                self.errors.addItem(data[i])
                self.errors.item(i).setIcon(QIcon(":/images/icons8-unavailable-16.png"))
                counter+=1
        if(counter==0):
            insertRows()

        