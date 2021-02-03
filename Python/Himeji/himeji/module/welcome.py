from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import os

if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.realpath("main.py")))

from connexion import center

class WelcomeWindow:
    """
    C'est la page principale après connexion
    """
    def __init__(self, user, admin, version):


        if __name__ != "__main__":
            os.remove("./temp/c.himeji")
            os.rmdir("temp")

        self.user = user
        self.version = version
        self.isAdmin = admin

        self.app = QApplication(sys.argv)
        self.win = QWidget()
        x, y = 1280, 720
        self.x, self.y = center(x, y)
        self.win.setGeometry(self.x, self.y, x, y)

        if not self.isAdmin:
            self.win.setWindowTitle(f"Himeji — {self.user} — {self.version}")
        elif self.isAdmin:
            self.win.setWindowTitle(f"Himeji — {self.user} — {self.version} (Administrateur)")

        self.win.setWindowIcon(QIcon("./bin/icon1"))
        self.win.show()

        self.label1 = QLabel(self.win)
        self.label1.setText(f"Bonjour {self.user}")
        self.label1.move(20, 20)
        self.label1.setFont(QFont('Mangal', 50))
        self.label1.adjustSize()
        self.label1.show()

        self.label1 = QLabel(self.win)
        self.label1.setText(f"Désolé {self.user}, cette version ne permet pas de faire plus qu'afficher ces deux textes.\nAttendez une version future pour cela.")
        self.label1.move(20, 100)
        self.label1.setFont(QFont('Mangal', 15))
        self.label1.adjustSize()
        self.label1.show()


        self.app.exec_()

if __name__ == "__main__":

    test = WelcomeWindow("Test", True, "Beta test")
    exit()
