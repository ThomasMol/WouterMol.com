#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys, os, json
from PyQt4 import QtGui, QtCore

imageFpath = '/home/wouter/Documents/website/WouterMol/images/'
 
# Create an PyQT4 application object.
a = QtGui.QApplication(sys.argv)
 
# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QtGui.QMainWindow()
w.setWindowTitle('Image database attribute editor/viewer')
 
# Set window size.
w.resize(1550, 1040)

#show image
pic = QtGui.QLabel(w)
pic.setGeometry(10, 10, 1280+10, 720+10)
#pic.setPixmap(QtGui.QPixmap(os.getcwd() + '/DSC_1037.jpg'))

#create a few textboxes
tbox_name = QtGui.QLineEdit(w)
tbox_loc = QtGui.QLineEdit(w)
tbox_cat = QtGui.QLineEdit(w)
tbox_album = QtGui.QLineEdit(w)
tbox_des = QtGui.QTextEdit(w)

tbox_name.move(1300, 30)
tbox_loc.move(1300,  75)
tbox_cat.move(1300,  120)
tbox_album.move(1300,165)
tbox_des.move(1300,  210)

for tbox in [tbox_name, tbox_loc, tbox_cat, tbox_album]:
    tbox.resize(200, 20)
tbox_des.resize(200, 85)

#create textbox labels
label_title = QtGui.QLabel(w)
label_title.move(1300, 5)
label_title.setText('image title')

label_loc = QtGui.QLabel(w)
label_loc.move(1300, 50)
label_loc.setText('location')

label_cat = QtGui.QLabel(w)
label_cat.move(1300, 95)
label_cat.setText('categories')

label_album = QtGui.QLabel(w)
label_album.move(1300, 140)
label_album.setText('albums')

label_des = QtGui.QLabel(w)
label_des.move(1300, 185)
label_des.setText('description')

#create a table
table = QtGui.QTableWidget(w)
table.move(10,740)
table.resize(1530, 290)
#table.setRowCount(10)
table.setColumnCount(8)

table.setHorizontalHeaderLabels(QtCore.QString("filename;title;location;categories;albums;description;date;time").split(';'))
header = table.horizontalHeader()
header.setResizeMode(QtGui.QHeaderView.ResizeToContents)
def fillTable():
    global database
    with open('database.json','r') as f:
        database = json.load(f)
    
    table.setRowCount(len(database))
        
    for i in range(len(database)):
        table.setItem(i, 0, QtGui.QTableWidgetItem((database[i]['filename'])))
        table.setItem(i, 1, QtGui.QTableWidgetItem((database[i]['name'])))
        table.setItem(i, 2, QtGui.QTableWidgetItem((database[i]['location'])))
        table.setItem(i, 3, QtGui.QTableWidgetItem((', '.join(database[i]['categories']))))
        table.setItem(i, 4, QtGui.QTableWidgetItem((', '.join(database[i]['albums']))))
        table.setItem(i, 5, QtGui.QTableWidgetItem((database[i]['description'])))
        table.setItem(i, 6, QtGui.QTableWidgetItem((database[i]['date'])))
        table.setItem(i, 7, QtGui.QTableWidgetItem((database[i]['time'])))

def item_click(item):
    if item.column() == 0:
        pic.setPixmap(QtGui.QPixmap(imageFpath + item.text()))

def regenDatabase():
    os.rename('database.json','databaseOLD.json')
    for i in range(len(database)):
        database[i]['name'] = str(table.item(i, 1).text())
        database[i]['location'] = str(table.item(i, 2).text())
        database[i]['categories'] = str(table.item(i, 3).text()).split(', ')
        database[i]['albums'] = str(table.item(i, 4).text()).split(', ')
        database[i]['description'] = str(table.item(i, 5).text())
        
    with open('database.json','w') as f:
        json.dump(database,f)
        
export = QtGui.QPushButton('REGENERATE DATABASE',w)
export.move(1300, 700)
export.resize(170,30)
refresh = QtGui.QPushButton('Refresh table',w)
refresh.move(1300, 650)

table.itemClicked.connect(item_click)
export.clicked.connect(regenDatabase)
refresh.clicked.connect(fillTable)

fillTable()
item_click(table.item(0,0))
 
# Show window
w.show()
 
sys.exit(a.exec_())
