import sys
from PyQt5.QtWidgets import QApplication
from main2 import StartVideo

app = QApplication(sys.argv)
mainStartVideo = StartVideo()
mainStartVideo.show()
rc = app.exec_()
sys.exit(rc)