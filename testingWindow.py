#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon

from build import testingWindow 
from build import res #ресурс файл

from tests.node.script import stressUsers, stessArticles, getMethods, signIn

import os
import urllib.request
from threading import Thread

from PyQt5.QtCore import QBasicTimer
import time


class testing(QtWidgets.QMainWindow, testingWindow.Ui_MainWindow):
    def __init__(self): #конструктор еб
        super().__init__()
        self.setupUi(self)  
        self.complete.setPixmap(QPixmap(":/images/icons8-unavailable-16.png"))
        self.startStressBtn.clicked.connect(self.startStress)
        #self.errors.setVisible(False)
        self.progressBar.setVisible(False)

        data = "Проверяем доступность сайта", "Создаем юзеров", "Пишем статьи"
        for i in range(0,len(data)):
            self.errors.addItem(data[i])
            self.errors.item(i).setIcon(QIcon(":/images/icons8-unavailable-16.png"))

    def startStress(self):
        if ( not getMethods):
            self.description.setText("Сайт не отвечает")
        else:
            self.errors.item(0).setIcon(QIcon(":/images/icons8-checked-16.png"))

        getMethods()
        #self.errors.setVisible(True)
        self.progressBar.setVisible(True)
        self.progressBar.setValue(0)
    
        stressCount = 45
#в среднем, юзер создается за 0.3с, статья 0.0089с
        sleepTime = ((0.34+0.0089)*stressCount)/100
        def setProgress(val):
            if (val>=100):
                return
            val=val+1
            print(val)
            self.progressBar.setValue(val)
            time.sleep(sleepTime)
            setProgress(val)

        
        thread1 = Thread(target=stressUsers, args=(stressCount,))
        thread2= Thread(target=stessArticles, args=(stressCount,))
        thread3 = Thread(target=setProgress, args=(1,))


        threads = [thread1, thread2, thread3]

        for i in threads:
            i.start()

        for i in threads:
            i.join()

        self.errors.item(1).setIcon(QIcon(":/images/icons8-checked-16.png"))
        # signIn()
        self.errors.item(2).setIcon(QIcon(":/images/icons8-checked-16.png"))




        