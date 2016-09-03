#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys, os, json
from PyQt4 import QtGui, QtCore
from glob import glob

imageFpath = '/home/wouter/Documents/website/WouterMol/images/'

# Create an PyQT4 application object.
a = QtGui.QApplication(sys.argv)
 
# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QtGui.QMainWindow()
w.setWindowTitle('Gallery preview image selecter')
 
# Set window size.
w.resize(696, 500)
w.move(200, 200)

#thumbnail container
thumbnail = QtGui.QLabel(w)
thumbnail.setGeometry(430, 11, 256, 144)

thumbnailCurrent = QtGui.QLabel(w)
thumbnailCurrent.setGeometry(430, 345, 256, 144)

#gallery source selector
combo = QtGui.QComboBox(w)
combo.addItem('albums')
combo.addItem('categories')
combo.move(10, 10)
combo.resize(200, 30)
#combo.setEditable(True)
#combo.lineEdit().setAlignment(QtCore.Qt.AlignCenter)

#create gallery group table instance
tableTypes = QtGui.QTableWidget(w)
tableTypes.move(10, 40)
tableTypes.resize(200, 450)
tableTypes.setColumnCount(1)
header1 = tableTypes.horizontalHeader()
header1.setResizeMode(QtGui.QHeaderView.Stretch)
tableTypes.setHorizontalHeaderLabels(QtCore.QString("galleries").split(';'))

#create gallery contents table instance
tableContents = QtGui.QTableWidget(w)
tableContents.move(220, 10)
tableContents.resize(200, 480)
tableContents.setColumnCount(1)
header2 = tableContents.horizontalHeader()
header2.setResizeMode(QtGui.QHeaderView.Stretch)
tableContents.setHorizontalHeaderLabels(QtCore.QString("images").split(';'))

#thumbnail setter button
setThumbButton = QtGui.QPushButton('Select as gallery thumbnail', w)
setThumbButton.move(430, 164)
setThumbButton.resize(256, 30)

#some informing text
thumbSet = QtGui.QLabel(w)

#gallery table view filler
def setGallery(text):
    gls = glob('%s/*.json'%text)
    tableTypes.setRowCount(len(gls))
    
    for i, gl in enumerate(gls):
        tableTypes.setItem(i, 0, QtGui.QTableWidgetItem((gl.split('/')[-1][:-5])))
        with open(gl, 'r') as f:
            test = json.load(f)
        if type(test) == list:
            tableTypes.item(i, 0).setBackground(QtGui.QColor(111, 19, 19))
        elif type(test) == dict:
            tableTypes.item(i, 0).setBackground(QtGui.QColor(42, 73, 43))
    
    listGallery(tableTypes.item(0, 0))

def listGallery(text):
    with open(str(combo.currentText()) + '/' + text.text() + '.json', 'r') as f:
        contents = json.load(f)
    
    if type(contents) == list:
        tableContents.setRowCount(len(contents))
        currentThumb('')
        thumbSet.setText('NO THUMBNAIL SET')
        thumbSet.setGeometry(496, 423, 144, 10)
        for i, name in enumerate(contents):
            tableContents.setItem(i, 0, QtGui.QTableWidgetItem((name['thumbnail'])))
    elif type(contents) == dict:
        tableContents.setRowCount(len(contents['images']))
        currentThumb(contents['thumbnail']['thumbnail'])
        thumbSet.setText('Current set thumbnail:')
        thumbSet.setGeometry(430, 330, 144, 10)
        for i, name in enumerate(contents['images']):
            tableContents.setItem(i, 0, QtGui.QTableWidgetItem((name['thumbnail'])))
    
    previewThumb(tableContents.item(0, 0))

def previewThumb(text):
    thumbnail.setPixmap(QtGui.QPixmap(imageFpath + text.text()))

def currentThumb(image):
    thumbnailCurrent.setPixmap(QtGui.QPixmap(imageFpath + image))

def setThumbnail(item):
    selection =  tableTypes.currentItem()
    row = tableContents.currentRow()
    
    with open(str(combo.currentText()) + '/' + selection.text() + '.json', 'r') as f:
        contents = json.load(f)
    if type(contents) == list:
        newContents = {'images':contents, 'thumbnail': contents[row]}
    elif type(contents) == dict:
        newContents = {'images':contents['images'], 'thumbnail': contents['images'][row]}
    #contents.insert(0, contents.pop(row))
    
    with open(str(combo.currentText()) + '/' + selection.text() + '.json', 'w') as f:
        json.dump(newContents, f)
    
    setGallery(combo.currentText())
    row = tableTypes.currentRow()
    listGallery(tableTypes.item(row, 0))

#event binders
combo.activated[str].connect(setGallery)
tableTypes.itemClicked.connect(listGallery)
tableContents.itemClicked.connect(previewThumb)
setThumbButton.clicked.connect(setThumbnail)

#init stuff
setGallery('albums')


#show and exit
w.show()
sys.exit(a.exec_())
