from PyQt5.QtCore import Qt, QSize, QThread, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QFrame, QPushButton, QToolBar, QAction, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
import cv2
import numpy as np


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()

class StartVideo(QMainWindow):

    def __init__(self):
        super(StartVideo, self).__init__()

        self.resize(1000, 500)
        self.setWindowTitle("Start Video")
        self.display_width = 500
        self.display_height = 250
        self.setStyleSheet("background-color: gray;")
        #create panel left

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.Ecran1 = QLabel(self.centralWidget)
        #self.Ecran1.resize(self.display_width, self.display_height)
        self.Ecran2 = QLabel(self.centralWidget)
        #self.Ecran2.resize(self.display_width, self.display_height)
        self.Ecran3 = QLabel(self.centralWidget)
        #self.Ecran3.resize(self.display_width, self.display_height)
        self.Ecran4 = QLabel(self.centralWidget)
        #self.Ecran4.resize(self.display_width, self.display_height)

        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.addWidget(self.Ecran1)
        self.hBoxLayout.addWidget(self.Ecran2)
        self.vBoxLayout = QVBoxLayout(self.centralWidget)
        self.vBoxLayout.addLayout(self.hBoxLayout)
        #self.vBoxLayout.addStretch()
        self.hBoxLayout2 = QHBoxLayout()
        self.hBoxLayout2.addWidget(self.Ecran3)
        self.hBoxLayout2.addWidget(self.Ecran4)
        self.vBoxLayout.addLayout(self.hBoxLayout2)
        #self.setLayout(self.vBoxLayout)

        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.Ecran1.setPixmap(qt_img)
        self.Ecran2.setPixmap(qt_img)
        self.Ecran3.setPixmap(qt_img)
        self.Ecran4.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        P = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(P)


    def onButtonActionClicked(self):
        pass

