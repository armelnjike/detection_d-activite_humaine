from PyQt5.QtCore import Qt, QSize, QThread, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QFrame, QPushButton, QToolBar, QAction, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model

from modele import *

input_video_file_path = "E:\Test Video.mp4"

output_video_file_path = "E:\\predicted.mp4"

#predict_on_video(input_video_file_path, output_video_file_path, SEQUENCE_LENGTH)



class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray, np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        cap = cv2.VideoCapture(input_video_file_path)
        predict_on_video(input_video_file_path, output_video_file_path, SEQUENCE_LENGTH)
        cap2 = cv2.VideoCapture(output_video_file_path)
        while self._run_flag:
            ret, cv_img = cap.read()
            ret2, cv_img2 = cap2.read()
            if ret and ret2:
                self.change_pixmap_signal.emit(cv_img, cv_img2)
                cv2.waitKey(60)
        cap.release()
        cap2.release()

    def stop(self):
        self._run_flag = False
        self.wait()

class StartVideo(QWidget):

    def __init__(self):
        super(StartVideo, self).__init__()

        self.className = ""
        self.setFixedSize(1000, 700)
        self.setWindowTitle("Start Video")
        self.display_width = 440
        self.display_height = 350
        self.setStyleSheet("background-color: gray;")

        #panel left
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(0.6)
        self.frame.setGeometry(QtCore.QRect(0, 0, 120, 700))
        self.frame.setStyleSheet("background-color: rgba(44, 41, 41, 1);")
        #self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        #button in frame
        self.pushButton = QPushButton("Start System",self.frame)
        self.pushButton.setStyleSheet("background-color: rgba(0, 0, 0, 1);border-radius:5px; color: white; font-size:16px;")
        self.pushButton_2 = QPushButton("Stop System", self.frame)
        self.pushButton_2.setStyleSheet("background-color: rgba(0, 0, 0, 1);border-radius:5px; color: white; font-size:18px;")
        self.pushButton.clicked.connect(self.Run)
        self.pushButton_2.clicked.connect(self.Stop)
        self.vBoxLayout = QVBoxLayout(self.frame)
        self.vBoxLayout.addWidget(self.pushButton)
        self.vBoxLayout.addSpacing(500)
        self.vBoxLayout.addWidget(self.pushButton_2)

        #def central widget
        self.centralWidget = QLabel(self)
        #self.setCentralWidget(self.centralWidget)
        #self.centralWidget = QFrame(self)
        #self.centralWidget.setFrameShape(QFrame.StyledPanel)
        #self.centralWidget.contentsMargins()
        self.centralWidget.setGeometry(QtCore.QRect(120, 0, 880, 700))
        self.Ecran1 = QLabel(self.centralWidget)
        self.Ecran1.setStyleSheet("border-radius:11px;border : solid rgba(0, 0, 0, 1); border-width : 6px ;")
        # self.Ecran1.resize(self.display_width, self.display_height)
        self.Ecran2 = QLabel(self.centralWidget)
        self.Ecran2.setStyleSheet("border-radius:11px;border : solid rgba(0, 0, 0, 1); border-width : 6px ;")
        # self.Ecran2.resize(self.display_width, self.display_height)
        self.Ecran3 = QLabel(self.centralWidget)
        self.Ecran3.setStyleSheet("border-radius:11px;border : solid rgba(0, 0, 0, 1); border-width : 6px ;")
        # self.Ecran3.resize(self.display_width, self.display_height)
        self.Ecran4 = QLabel(self.centralWidget)
        self.Ecran4.setStyleSheet("border-radius:11px;border : solid rgba(0, 0, 0, 1); border-width : 6px ;")
        # self.Ecran4.resize(self.display_width, self.display_height)
        self.Ecran1.setGeometry(QtCore.QRect(0, 0, self.display_width, self.display_height))
        self.Ecran2.setGeometry(QtCore.QRect(self.display_width, 0, self.display_width , self.display_height))
        self.Ecran3.setGeometry(QtCore.QRect(0, self.display_height, self.display_width, self.display_height))
        self.Ecran4.setGeometry(QtCore.QRect(self.display_width, self.display_height, self.display_width,self.display_height))

        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)



    def Run(self):
        self.thread.start()
        #self.className = predict_on_video("E:\THL 1.mp4", SEQUENCE_LENGTH)
        #print("La classe prédicte est : ", self.thread.className)

    def Stop(self):
        self.thread.stop()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @pyqtSlot(np.ndarray, np.ndarray)
    def update_image(self, cv_img, cv_img2):
        qt_img = self.convert_cv_qt(cv_img, cv_img2)[0]
        qt_img2 = self.convert_cv_qt(cv_img, cv_img2)[1]
        self.Ecran1.setPixmap(qt_img)
        self.Ecran2.setPixmap(qt_img)
        self.Ecran3.setPixmap(qt_img2)
        self.Ecran4.setPixmap(qt_img2)

    def convert_cv_qt(self, cv_img, cv_img2):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        rgb_image2 = cv2.cvtColor(cv_img2, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        h2, w2, ch2 = rgb_image2.shape
        bytes_per_line = ch * w
        bytes_per_line2 = ch2 * w2
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        convert_to_Qt_format2 = QtGui.QImage(rgb_image2.data, w2, h2, bytes_per_line2, QtGui.QImage.Format_RGB888)
        P = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        P2 = convert_to_Qt_format2.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(P), QPixmap.fromImage(P2)

