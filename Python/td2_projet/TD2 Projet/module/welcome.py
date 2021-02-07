from threading import Thread
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import os

if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.realpath("main.py")))

from module.util import center, setBackgroundColor, getBackgroundColor, choicedBackgroundColor

class WelcomeWindow:
    """
    C'est la page principale après connexion
    """
    def __init__(self, user, admin, version):
        
        try:
            os.remove("./temp/c.spi")
            os.rmdir("temp")
        except:
            pass

        self.colorText = "color: black;"

        if choicedBackgroundColor() == 1:
            self.colorText = "color: white;"

        self.user = user
        self.version = version
        self.isAdmin = admin

        self.app = QApplication(sys.argv)
        self.win = QWidget()
        x, y = 1280, 720
        self.x, self.y = center(x, y)
        self.win.setGeometry(self.x, self.y, x, y)

        if not self.isAdmin:
            self.win.setWindowTitle(f"Projets SPI — {self.user} — {self.version}")
        elif self.isAdmin:
            self.win.setWindowTitle(f"Projets SPI — {self.user} — {self.version} (Administrateur)")

        self.win.setWindowIcon(QIcon("./bin/icon1"))
        self.win.show()

        self.label0 = QLabel(self.win)
        self.label0.move(0,0)
        self.label0.resize(x, y)
        self.label0.setStyleSheet(getBackgroundColor())
        self.label0.show()

        self.label1 = QLabel(self.win)
        self.label1.setText(f"Bonjour {self.user}")
        self.label1.setStyleSheet(self.colorText)
        self.label1.move(20, 20)
        self.label1.setFont(QFont('Mangal', 50))
        self.label1.adjustSize()
        self.label1.show()

        self.label2 = QLabel(self.win)
        self.label2.setText(f"Désolé {self.user}, cette version ne permet pas de faire plus qu'afficher ces deux textes.\nAttendez une version future pour cela.")
        self.label2.move(20, 140)
        self.label2.setFont(QFont('Mangal', 15))
        self.label2.setStyleSheet(self.colorText)
        self.label2.adjustSize()
        self.label2.show()

        self.label3 = QLabel(self.win)
        self.label3.setText(f"Projets en cours :\n  * Python Together Poitiers\n    * Voiture télécommandée")
        self.label3.move(20, 210)
        self.label3.setFont(QFont('Mangal', 15))
        self.label3.setStyleSheet(self.colorText)
        self.label3.adjustSize()
        self.label3.show()

        self.radio1 = QRadioButton(self.win)
        self.radio1.setText("Mode Sombre")
        self.radio1.toggled.connect(lambda:setBackgroundColor(1))
        self.radio1.setStyleSheet(self.colorText)
        self.radio1.move(20, 660)


        if choicedBackgroundColor() == 1:
            self.radio1.setChecked(True)
        
        self.radio1.show()

        self.radio2 = QRadioButton(self.win)
        self.radio2.setText("Mode Clair")
        self.radio2.toggled.connect(lambda:setBackgroundColor(2))
        self.radio2.setStyleSheet(self.colorText)
        self.radio2.move(20, 680)

        if choicedBackgroundColor() == 2:
            self.radio2.setChecked(True)

        self.radio2.show()

        """
        PLACE POUR LES BOUTONS RADIOS
        """

        sys.exit(self.app.exec_())

if __name__ == "__main__":

    test = WelcomeWindow("Test", True, "Beta test")
    exit()
