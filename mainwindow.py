#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

from build import mainwindow, res  # Это наш конвертированный файл дизайна
from testingWindow import testing
import os
from subprocess import Popen, PIPE
import subprocess

class PyCi(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    directory = ""

    def __init__(self): #конструктор еб
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.changeDir.clicked.connect(self.browseFolder)
        self.changeDir2.setVisible(False)

        self.changeDir2.clicked.connect(self.browseFolder)
        self.goToTestBtn.clicked.connect(self.goToTest)

        self.tests.currentIndexChanged.connect(self.testing)

        self.deploymentBtn.clicked.connect(self.deployment)
        self.deploymentBtn.setEnabled(False)
        
        self.complete.setPixmap(QPixmap(":/images/icons8-cancel-16.png"))
        self.complete_2.setPixmap(QPixmap(":/images/icons8-cancel-16.png"))
        self.complete_3.setPixmap(QPixmap(":/images/icons8-cancel-16.png"))

        self.arrow.setPixmap(QPixmap(":/images/icons8-right-16.png"))
        self.arrow_2.setPixmap(QPixmap(":/images/icons8-right-16.png"))
    def subOpen(self, query, directory=None):
        data = subprocess.Popen(query, cwd=directory, stdout=PIPE, stderr=PIPE).communicate() 
        return data

    def goToTest(self):
        self.w2 = testing()
        self.w2.show()

    def deployment(self):
        data = subprocess.Popen("heroku login", cwd=self.directory, stdout=PIPE, stderr=PIPE).communicate() 
        print(data)
        #heroku git:remote -a metida
        #git push master heroku
        #heroku addons:create cleardb:ignite
        #heroku config | grep CLEARDB_DATABASE_URL #вводим это, и парсим строку
        # mysql://username:password@host/database?reconnect=true
        
        

    def browseFolder(self):
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select project folder")
        def complete(self, bool, string=""): 
            self.dir.setText(self.directory)
            self.description.setText(string)
            self.changeDir2.setVisible(bool)
            self.changeDir.setVisible(not bool)
            if (bool  == True):   
                self.complete.setPixmap(QPixmap(":/images/icons8-checked-16.png"))
            else: 
                self.complete.setPixmap(QPixmap(":/images/icons8-cancel-16.png"))
            self.dir.setEnabled(not bool)
        

        def isGitRepository(directory):
            data = subprocess.Popen("git status", cwd=directory, stdout=PIPE, stderr=PIPE).communicate() 
            string = ""
            for i in range(0, len(data)):
                string += str(data[i])

            if ( string.find("fatal:") != -1 ): #ух 
                complete(self, False, "Git репозиторий не найден")

        def isDirectory(directory):
            if (directory != ''):
                self.deploymentBtn.setEnabled(True)
                complete(self, True)
            else:
                self.deploymentBtn.setEnabled(False)
                complete(self, False, "Директория не найдена")
                return
                
        isDirectory(self.directory)
        isGitRepository(self.directory)



    def testing(self): 
        if ( self.tests.currentText() == "Другое"):
            self.findedTest.setText("У нас нет тестов для тебя")
            self.goToTestBtn.setVisible(False) 
        elif ( self.tests.currentText() == "Node.js"):
            self.findedTest.setText("У нас есть тесты для тебя")
            self.goToTestBtn.setVisible(True) 


    def allIsOk(self, directory):
        buttonReply = QtWidgets.QMessageBox.question(self, 'Оповещение', "C этого момента к директории <b>" + directory + "</b> подключена непрерывная интеграция. <br> Я надеюсь, что была указана корневая папка в репозитории. Я временно исчезну, появлюсь только после создания первого локального коммита. <br> Если все  верно, жмякаем да", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            print('Yes clicked.')
            return True
        else:
            print('No clicked.')
            return False
