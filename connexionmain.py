import sys
from PyQt5.QtWidgets import QApplication
from connexion import Connexion

app = QApplication(sys.argv)
mainStartVideo = Connexion()
mainStartVideo.show()
rc = app.exec_()
sys.exit(rc)