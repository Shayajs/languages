"""
Dernière version
Informations :
    Import total : sys, os, tkinter, threading(Thread, pickle, time(sleep), PyQt5
    PyQt5 > QtWidjets, QtGui, QtCore(Qt)
"""
# Version: 0.1
# Author: Lucas Espinar
# Copyright: Creative Common

import sys
import os
from tkinter import Tk

try:
    import PyQt5

    os.chdir(os.path.dirname(os.path.realpath("main.pyw")))
    print(os.getcwd())
except:
    print("Un problème est survenu...")
    os.system("pip install PyQt5")

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
from time import sleep
from threading import Thread
import pickle

def center(x, y) -> tuple:
    """
    Permet de centrer une fenetre avec les coordonnées de x et y de la fenetre
    """
    calc = Tk()
    width = calc.winfo_screenwidth()
    height = calc.winfo_screenheight()
    ww = (width - x) // 2
    hh = (height - y) // 2
    return ww, hh


class IntroWindow:
    """
    It's that first window with the lesser information. To load main project.
    """
    def __init__(self):
        self.tha = Thread(None, self.chargement)

        self.app = QApplication(sys.argv)
        self.win = QMainWindow()
        x, y = 800, 350
        self.pos = center(x, y)
        self.win.setGeometry(self.pos[0],self.pos[1],x,y)
        self.win.setWindowTitle("Himeji")
        self.win.setWindowFlag(Qt.FramelessWindowHint)
        self.win.show()
        self.label = QLabel(self.win)
        self.pixmap = QPixmap('.\\bin\\himeji.png')
        self.label.setPixmap(self.pixmap)
        self.win.setCentralWidget(self.label)
        self.win.setWindowIcon(QIcon("./bin/icon.png"))
        # self.win.resize(self.pixmap.width(), self.pixmap.height())

        self.label2 = QLabel(self.win)
        self.label2.setText("Ouverture en cours... Veuillez Patienter")
        self.label2.move(10, 320)
        self.label2.adjustSize()
        self.label2.show()

        self.tha.start()

        self.app.exec_()

    def chargement(self, time = 100):
        a = 0
        for i in range(time):
            sleep(0.05)
            a += 1
            self.label2.setText(f"Ouverture en cours... Veuillez Patienter {a}%")
            self.label2.adjustSize()

        sleep(2)
        self.label2.setText("Ouverture en cours...")

        self.win.setVisible(False)
        QtWidgets.qApp.quit()


class ConnectionWindow:
    """
    Fenetre de connexion simple
    """
    def __init__(self):
        ##Variables autres

        self.files_enregistrement = None
        self.connected_one = None

        try:
            with open("./bin/comptes.himeji", "rb") as file:
                depickle = pickle.Unpickler(file)
                self.files_enregistrement = depickle.load()

        except:
            with open("./bin/comptes.himeji", "wb") as file:
                self.files_enregistrement = {"uadmin":"padmin"}
                pickler = pickle.Pickler(file)
                pickler.dump(self.files_enregistrement)

        ## APPLICATION
        self.app = QApplication(sys.argv)
        self.win = QWidget()
        x,y = 550, 320
        self.posx, self.posy = center(x, y)
        self.win.setGeometry(self.posx,self.posy,x,y)
        self.win.setWindowTitle("Page de Connexion")
        self.win.setWindowFlag(Qt.FramelessWindowHint)
        self.win.setWindowIcon(QIcon("./bin/icon1.png"))
        self.win.show()

        self.label1 = QLabel(self.win)
        self.label1.setText("Connexion")
        self.label1.move(20, 20)
        self.label1.setFont(QFont('Mangal', 80))
        self.label1.adjustSize()
        self.label1.show()

        self.label2 = QLabel(self.win)
        self.label2.setText("Mauvais identifiants, réessayez.")
        self.label2.move(260, 175)
        self.label2.setFont(QFont('Mangal', 11))
        self.label2.adjustSize()
        # self.label2.show()

        self.champ1 = QLineEdit(self.win)
        self.champ1.move(20, 140)
        self.champ1.resize(220, 30)
        self.champ1.show()

        self.champ2 = QLineEdit(self.win)
        self.champ2.setEchoMode(QLineEdit.Password)
        self.champ2.move(20, 180)
        self.champ2.resize(220, 30)
        self.champ2.show()

        self.bouton1 = QPushButton(self.win)
        self.bouton1.setText(" Se connecter ")
        self.bouton1.move(20, 220)
        self.bouton1.setFont(QFont('Mangal', 20))
        self.bouton1.clicked.connect(self.connection)
        self.bouton1.show()

        self.bouton2 = QPushButton(self.win)
        self.bouton2.setText(" S'enregistrer ")
        self.bouton2.move(200, 220)
        self.bouton2.setFont(QFont('Mangal', 20))
        self.bouton2.clicked.connect(self.register)
        self.bouton2.show()

        self.bouton3 = QPushButton(self.win)
        self.bouton3.setText("Fermer")
        self.bouton3.move(20, 270)
        self.bouton3.setFont(QFont('Mangal', 11))
        self.bouton3.clicked.connect(self.quitter)
        self.bouton3.show()

        # Page d'enregistrement

        self.win2 = QWidget()
        self.win2.setGeometry(self.posx,self.posy,x,y)
        self.win2.setWindowTitle("Page de Connexion")

        sys.exit(self.app.exec_())

    def connection(self) -> None:
        """
        Module connexion
        """
        tha = Thread(None, self._timer_labe2)
        try:
            if self.files_enregistrement[self.champ1.text()] and self.files_enregistrement[self.champ1.text()] == self.champ2.text() :
                print("Connected !")
                self.label2.setText("Connecté !")
                self.label2.setStyleSheet("color : green;")
                self.label2.adjustSize()
                self.label2.show()
                tha.start()
                self.connected_one = (self.champ1.text(), True)
            else:
                print("MAUVAISE CO !")
                self.label2.setStyleSheet("color : red;")
                self.label2.show()
                tha.start()
        except:
            self.label2.show()
            self.label2.setStyleSheet("color : red;")
            tha.start()
            print("Une erreur est survenue")

    def _timer_labe2(self):
        """
        Permettre un affichage limité de l'étiquette de suivi
        """
        sleep(2.5)
        self.label2.setVisible(False)

    def quitter():
        self.app.quit()
        QtWidgets.qApp.quit()

    def register(self):
        try:
            self.win2.show()
        except:
            print("Une erreur est encore survenue")

app = IntroWindow()
connexion = ConnectionWindow()
exit()
