# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Alert_panel2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import pyqtgraph as pg
from Bdconnexion import BDconnexion
import mysql.connector as mc
from mysql.connector import Error

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsView,QGraphicsScene, QTableWidgetItem

class Ui_Alert_History(object):
    def setupUi(self, Alert_History):
        Alert_History.setObjectName("Alert_History")
        Alert_History.resize(1000, 700)
        Alert_History.setStyleSheet("background-color: rgb(36, 31, 49);")
        self.tableWidget = QtWidgets.QTableWidget(Alert_History)
        self.tableWidget.setGeometry(QtCore.QRect(525, 91, 441, 521))
        self.tableWidget.setTabletTracking(False)

        self.tableWidget.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.tableWidget.setRowCount(0)
        """ **********   column  *********************"""
        self.tableWidget.setColumnCount(3)
        data = ['source', 'date', 'type_alerte']
        self.tableWidget.setHorizontalHeaderLabels(data)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.pushButton = QtWidgets.QPushButton(Alert_History)
        self.pushButton.setGeometry(QtCore.QRect(520, 620, 88, 27))
        self.pushButton.setStyleSheet("background-color: rgb(192, 191, 188);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Alert_History)
        self.label.setGeometry(QtCore.QRect(40, 90, 441, 521))
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(Alert_History)
        self.graphicsView.setGeometry(QtCore.QRect(35, 91, 451, 521))
        self.graphicsView.setObjectName("graphicsView")
        """self.pushButton_2 = QtWidgets.QPushButton(Alert_History)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 620, 88, 27))
        self.pushButton_2.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.pushButton_2.setObjectName("pushButton_2")"""
        self.comboBox = QtWidgets.QComboBox(Alert_History)
        self.comboBox.setGeometry(QtCore.QRect(30, 60, 79, 27))
        self.comboBox.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        """  Graphics view   """
        self.graphic = QtWidgets.QGraphicsView(Alert_History)
        self.graphic.setGeometry(QtCore.QRect(75,90,400,520))
        self.graphic.setObjectName("Historique des alertes")
        self.graphic.setStyleSheet("background-color: rgb(222, 221, 218);")
        """ Dessin   """
        scene = QGraphicsScene()
        self.graphic.setScene(scene)
        self.plotWgt = pg.PlotWidget()


        """ ***************** Chargement des données Données  ******************** """

        try:
            conn = mc.connect(host="localhost", user="root", password="", database="video_securite")
            mycursor = conn.cursor()
            mquery = """SELECT type_alerte_Alerte, date_alerte_Alerte, ID_camera_Systeme_Camera FROM `alerte` WHERE `type_alerte_Alerte` LIKE 'danger' ;"""
            mycursor.execute(mquery)
            result = mycursor.fetchall()
            l = len(result)

            for i in range(l):
                self.addTableRow(self.tableWidget, result[i])

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if conn.is_connected():
                mycursor.close()
                conn.close()
                print("MySQL connection is closed")


        data = [1,2,3,4,5,7,6,8,9,10]
        plotItem = self.plotWgt.plot(data)
        proxy_w = scene.addWidget(self.plotWgt)



        self.retranslateUi(Alert_History)
        QtCore.QMetaObject.connectSlotsByName(Alert_History)

    def retranslateUi(self, Alert_History):
       _translate = QtCore.QCoreApplication.translate
       Alert_History.setWindowTitle(_translate("Alert_History", "Form"))
       self.pushButton.setText(_translate("Alert_History", "Reload"))
       self.label.setText(_translate("Alert_History", "TextLabel"))
       #self.pushButton_2.setText(_translate("Alert_History", "Retour"))
       self.comboBox.setItemText(0, _translate("Alert_History", "By date"))
       self.comboBox.setItemText(1,_translate("alert_hystory","ddddd"))

    def addTableRow(self, table, row_data):
        row = table.rowCount()
        table.setRowCount(row+1)
        col = 0
        for item in row_data:
            cell = QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            col += 1
