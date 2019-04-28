#!/bin/bash

pyuic5 ./mainwindow.ui -o ./build/mainwindow.py
pyuic5 ./testingWindow.ui -o ./build/testingWindow.py

pyrcc5 ./res.qrc -o ./build/res.py
python main.py