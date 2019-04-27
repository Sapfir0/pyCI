#!/bin/bash

pyuic5 ./mainwindow.ui -o ./build/mainwindow.py
pyrcc5 ./res.qrc -o ./build/res.py
python pyCi.py