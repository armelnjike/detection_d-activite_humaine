from PyQt5.QtWidgets import QMainWindow, QLabel, QSizePolicy,QPushButton, QSpacerItem,QLineEdit, QMessageBox, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5 import QtCore
from sonia import Ui_Form
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
import resources
import mysql.connector as mc
from mysql.connector import Error

class Connexion(QMainWindow):
    def __init__(self):
        super(Connexion, self).__init__()
        self.resize(1000, 700)
        self.setWindowTitle("LOGIN PAGE")
        self.setStyleSheet("margin: 10px 10px 10px 10px;")

        self.centralWidget = QWidget(self)
        self.centralWidget.setStyleSheet("margin: 10px 10px 10px 10px;")
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setStyleSheet("background-color:rgba(44, 41, 41, 1);")

        self.Baniere = QLabel(self.centralWidget)
        self.Baniere.setGeometry(QtCore.QRect(130, 80, 700, 90))
        self.Baniere.setText("Security System")
        self.Baniere.setAlignment(QtCore.Qt.AlignCenter)
        self.Baniere.setStyleSheet("background-color: white;color: black;border-radius: 10px; font: 80 25pt \"Ubuntu Condensed\";")
        self.logo = QLabel(self.Baniere)
        self.logo.setGeometry(QtCore.QRect(50, 5, 80, 80))
        self.logo.setStyleSheet("border-image: url(:logo.png);")

        self.loginForm = QLabel(self.centralWidget)
        self.loginForm.setGeometry(QtCore.QRect(200, 300, 600, 300))
        self.loginForm.setStyleSheet("background-color: rgb(196, 196, 196);border-radius : 10px;margin: 3px 3px 3px 3px;")

        self.vBoxLayout = QVBoxLayout(self.loginForm)
        self.lineUsername = QLineEdit(self.loginForm)
        self.lineUsername.resize(190, 40)
        self.lineUsername.setStyleSheet("background-color:rgba(0, 0, 0, 0);border:none;border-bottom:2px solid rgba(46, 82, 101, 200);color:rgba(0, 0, 0, 240);padding-bottom:7px;")
        self.lineUsername.setPlaceholderText("Username")

        self.linePassword = QLineEdit(self.loginForm)
        self.linePassword.setEchoMode(QLineEdit.Password)
        self.linePassword.resize(190, 40)
        self.linePassword.setStyleSheet("background-color:rgba(0, 0, 0, 0);border:none;border-bottom:2px solid rgba(46, 82, 101, 200);color:rgba(0, 0, 0, 240);padding-bottom:7px;")
        self.linePassword.setPlaceholderText("Password")
        self.vBoxLayout.addWidget(self.lineUsername)
        self.vBoxLayout.addWidget(self.linePassword)

        self.Buttonvalider = QPushButton(self.loginForm)
        self.Buttonvalider.setText("Valider")
        self.Buttonvalider.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(238, 238, 236);border-radius: 10px;")
        self.Buttonvalider.setGeometry(QtCore.QRect(500, 250, 90, 30))
        self.Buttonvalider.clicked.connect(self.connexion)


    def connexion(self):
        try:
            name = self.lineUsername.text()
            password = self.linePassword.text()
            db = mc.connect(host="localhost", user="root", password="", database="video_securite")
            mycursor = db.cursor()
            mquery = """SELECT User_Name_Utilisateur, Password_Utilisateur FROM personnel_technique where User_Name_Utilisateur = %s AND Password_Utilisateur = %s ;"""
            mycursor.execute(mquery,(name,password))
            result = mycursor.fetchall()

            if result != []:
                self.window2 = Ui_Form()
                self.close()
                self.window2.show()

            else:
                QMessageBox.information(self, "Alert", "Message : username or password is incorrect")
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if db.is_connected():
                mycursor.close()
                db.close()
                print("MySQL connection is closed")