from PyQt5.QtWidgets import QMainWindow, QLabel, QSizePolicy,QPushButton, QSpacerItem,QLineEdit, QMessageBox, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
import resources
from main2 import StartVideo
from Alert_pan import Ui_Alert_History

class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setFixedSize(1000, 700)
        self.setWindowTitle("System Connected")
        self.centralWidget = QWidget(self)
        self.centralWidget.resize(1000, 700)
        self.centralWidget.setStyleSheet("margin: 10px 10px 10px 10px;")
        self.centralWidget.setStyleSheet("background-color:rgba(44, 41, 41, 1); margin: 10px 10px 10px 10px;")

        self.Baniere = QLabel(self.centralWidget)
        self.Baniere.setGeometry(QtCore.QRect(130, 80, 700, 90))
        self.Baniere.setText("Security System")
        self.Baniere.setAlignment(QtCore.Qt.AlignCenter)
        self.Baniere.setStyleSheet("background-color: white;color: black;border-radius: 10px; font: 80 25pt \"Ubuntu Condensed\";")
        self.logo = QLabel(self.Baniere)
        self.logo.setGeometry(QtCore.QRect(50, 5, 80, 80))
        self.logo.setStyleSheet("border-image: url(:logo.png);")

        """self.panelButton = QLabel(self.centralWidget)
        self.panelButton.setGeometry(QtCore.QRect(200, 300, 600, 300))"""
        self.startButton = QPushButton(self.centralWidget)
        self.startButton.setText("START SYSTEM")
        self.startButton.setGeometry(QtCore.QRect(350, 300, 190, 60))
        self.startButton.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(238, 238, 236);border-radius: 10px;")
        self.startButton.clicked.connect(self.startMethod)
        self.showHistory = QPushButton(self.centralWidget)
        self.showHistory.setText("SHOW HISTORY ALERT")
        self.showHistory.setGeometry(QtCore.QRect(350, 500, 190, 60))
        self.showHistory.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(238, 238, 236);border-radius: 10px;")
        self.showHistory.clicked.connect(self.history)


    def startMethod(self):
        self.window2 = StartVideo()
        self.close()
        self.window2.show()

    def history(self):
        self.form = QWidget()
        self.win = Ui_Alert_History()
        self.win.setupUi(self.form)

        self.close()
        self.form.show()