#!/bin/bash

pyuic5 ./mainwindow.ui -o ./build/mainwindow.py
pyuic5 ./testsWindow.ui -o ./build/testsWindow.py

pyrcc5 ./res.qrc -o ./build/res.py
python mainwindow.py