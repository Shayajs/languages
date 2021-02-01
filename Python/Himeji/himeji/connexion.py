"""
Dernière version
Informations :
    Import total : sys, os, tkinter, threading(Thread, pickle, time(sleep), PyQt5
    PyQt5 > QtWidjets, QtGui, QtCore(Qt)
"""
# Version: 0.1.33
# Author: Lucas Espinar
# Copyright: Creative Common


version = '0.1.34'


import sys
import os
from tkinter import Tk

try:
    import PyQt5

    os.chdir(os.path.dirname(os.path.realpath("connexion.py")))
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

import urllib.request


## DEBUT PROGRAMME ------------------------------

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

def verif_ver() -> str:
    try:
        url = urllib.request.Request("https://raw.githubusercontent.com/Shayajs/languages/master/Python/Himeji/himeji/bin/version.vhimeji")
        url_open = urllib.request.urlopen(url)
        send = url_open.read().decode('utf-8')
        send = send.split("\n")[0]
        print(f"> Dernière version {send} <")
        return send
    except:
        return None


## DEBUT CLASS ---------------------------------

class IntroWindow:
    """
    It's that first window with the lesser information. To load main project.
    """
    def __init__(self):
        global version
        self.version = version

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
        self.label2.move(10, 310)
        self.label2.adjustSize()
        self.label2.show()

        self.tha.start()

        self.app.exec_()

    def chargement(self, time = 52):
        a = "   "

        for i in range(time):
            sleep(0.1)
            if i % 4 == 3:
                a = "..."
            elif i % 4 == 2:
                a = ".. "
            elif i % 4 == 1:
                a = ".  "
            elif i % 4 == 0:
                a = "   "

            self.label2.setText(f"Version {self.version}\nVeuillez Patienter {a}")
            self.label2.adjustSize()

            if i == time - 1:
                sleep(2)
                self.label2.setText("Ouverture en cours...")

        sleep(2)


        self.win.setVisible(False)
        QtWidgets.qApp.quit()



# -------- Principal -----------

class ConnectionWindow:

    """
    Fenetre de connexion simple
    """


    def __init__(self):
        ##Variables autres
        global version

        self.version = version
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
        self.label2.move(260, 150)
        self.label2.setFont(QFont('Mangal', 11))
        self.label2.adjustSize()
        # self.label2.show()

        self.label3 = QLabel(self.win)
        self.label3.setText("Vérification de version en cours...")
        self.label3.move(260, 190)
        self.label3.setFont(QFont('Mangal', 11))
        self.label3.adjustSize()
        self.label3.show()
        self.threadLabel3 = Thread(None, self.version_search)
        self.threadLabel3.start()

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
        self.bouton2.clicked.connect(self.register_window)
        self.bouton2.show()

        self.bouton3 = QPushButton(self.win)
        self.bouton3.setText("Fermer")
        self.bouton3.move(20, 270)
        self.bouton3.setFont(QFont('Mangal', 11))
        self.bouton3.clicked.connect(self.quitter)
        self.bouton3.show()

        # --------------- Page d'enregistrement

        self.win2 = QWidget()
        x2, y2 = 270, 400
        self.posx2, self.posy2 = center(x2, y2)
        self.win2.setGeometry(self.posx2,self.posy2,x2,y2)
        self.win2.setWindowTitle("S'enregistrer")
        self.win2.setWindowIcon(QIcon("./bin/icon1.png"))

        self.labelWin21 = QLabel(self.win2)
        self.labelWin21.setText("S'enregistrer")
        self.labelWin21.move(20, 10)
        self.labelWin21.setFont(QFont('Mangal', 30))
        self.labelWin21.adjustSize()
        self.labelWin21.show()

        self.labelWin22 = QLabel(self.win2)
        self.labelWin22.setText("Nouveau nom d'utilisateur")
        self.labelWin22.move(20, 70)
        self.labelWin22.setFont(QFont('Mangal', 12))
        self.labelWin22.adjustSize()
        self.labelWin22.show()

        self.champWin21 = QLineEdit(self.win2)
        self.champWin21.setText("username")
        self.champWin21.move(20, 90)
        self.champWin21.resize(220, 30)
        self.champWin21.show()

        self.labelWin23 = QLabel(self.win2)
        self.labelWin23.setText("Mot de passe")
        self.labelWin23.move(20, 130)
        self.labelWin23.setFont(QFont('Mangal', 12))
        self.labelWin23.adjustSize()
        self.labelWin23.show()

        self.champWin22 = QLineEdit(self.win2)
        self.champWin22.setEchoMode(QLineEdit.Password)
        self.champWin22.move(20, 150)
        self.champWin22.resize(220, 30)
        self.champWin22.show()

        self.labelWin24 = QLabel(self.win2)
        self.labelWin24.setText("Retapez le mot de passe")
        self.labelWin24.move(20, 190)
        self.labelWin24.setFont(QFont('Mangal', 12))
        self.labelWin24.adjustSize()
        self.labelWin24.show()

        self.champWin23 = QLineEdit(self.win2)
        self.champWin23.setEchoMode(QLineEdit.Password)
        self.champWin23.move(20, 210)
        self.champWin23.resize(220, 30)
        self.champWin23.show()

        self.labelWin25 = QLabel(self.win2)
        self.labelWin25.setText("Retapez le mot de passe")
        self.labelWin25.move(20, 250)
        self.labelWin25.setFont(QFont('Mangal', 12))
        self.labelWin25.adjustSize()

        self.boutonWin21 = QPushButton(self.win2)
        self.boutonWin21.setText("S'enregistrer")
        self.boutonWin21.move(20, 300)
        self.boutonWin21.setFont(QFont('Mangal', 13))
        self.boutonWin21.clicked.connect(self.register)
        self.boutonWin21.show()

        sys.exit(self.app.exec_())

    def connection(self) -> None:
        """
        Module connexion
        """
        tha = Thread(None, self._timer_labe2)
        try:
            if self.files_enregistrement[self.champ1.text()] and self.files_enregistrement[self.champ1.text()] == self.champ2.text() :

                self.label2.setText("Connecté !")
                self.label2.setStyleSheet("color : green;")
                self.label2.adjustSize()
                self.label2.show()
                tha.start()
                self.connected_one = (self.champ1.text(), True)
                ThConn = Thread(None, self.quitter_timer)
                ThConn.start()

            else:

                self.label2.setStyleSheet("color : red;")
                self.label2.show()
                tha.start()

        except:
            self.label2.show()
            self.label2.setStyleSheet("color : red;")
            tha.start()

    def version_search(self) -> None:
        """
        Vérifie si le logiciel est à jour
        """
        a = 0
        b = 0

        verif = verif_ver()

        splited1 = verif.split(".")
        splited2 = self.version.split(".")

        for i in range(0, 3):
            if splited1[i] == splited2[i]:
                pass
            elif splited1[i] > splited2[i]:
                a = 1
            elif splited1[i] < splited2[i]:
                b = 1

        if b == a:
            self.label3.setText("Vous êtes à jour")
            self.label3.adjustSize()
            self.label3.setStyleSheet("color: green;")

        elif b < a:
            self.label3.setText(f"La version {verif} est disponible !")
            self.label3.adjustSize()
            self.label3.setStyleSheet("color: steelblue;")

        elif b > a:
            self.label3.move(250, 170)
            self.label3.setText(f"Votre version ({self.version}) est une version beta !\n(Version en ligne : {verif})")
            self.label3.setStyleSheet("color: goldenrod;")
            self.label3.adjustSize()

        else:
            self.label3.setText("Impossible de vérifier les mises à jours.")

    def _timer_labe2(self) -> None:
        """
        Permettre un affichage limité de l'étiquette de connexion
        """
        sleep(2.5)
        self.label2.setVisible(False)

    def quitter_timer(self) -> None:
        """
        Quitter l'application, mais avec Timer
        """
        sleep(0.5)
        self.app.quit()
        QtWidgets.qApp.quit()

    def quitter(self) -> None:
        """
        Quitter l'application
        """
        self.app.quit()
        QtWidgets.qApp.quit()

    def register_window(self) -> None:
        """
        Ouvrir la page d'enregistrement
        """
        try:
            self.win2.show()
            self.champWin21.setText("")
            self.champWin22.setText("")
            self.champWin23.setText("")
            self.labelWin25.setVisible(False)
        except:
            self.label2.setText("Une erreur est survenue")
            threadExceptLabel2 = Thread(None, _timer_labe2)
            threadExceptLabel2.start()

    def register(self):
        a = 0
        try:
            self.files_enregistrement[self.champWin21.text()]
            a = 1
        except:
            a = 2

        if a == 1:
            self.labelWin25.setText("Vous êtes déjà enregistrer !")
            self.labelWin25.setStyleSheet("color: red;")
            self.labelWin25.adjustSize()
            self.labelWin25.show()

        elif a == 2:
            if self.champWin22.text() == self.champWin23.text() and (self.champWin22.text() != "" and self.champWin23.text() != ""):

                self.files_enregistrement[self.champWin21.text()] = self.champWin22.text()

                self.labelWin25.setText("Enregistrement en cours ...")

                with open("./bin/comptes.himeji", "wb") as file:
                    pickler = pickle.Pickler(file)
                    pickler.dump(self.files_enregistrement)

                self.labelWin25.setText("Enregistrer")
                self.labelWin25.setStyleSheet("color: green;")
                self.labelWin25.adjustSize()
                self.labelWin25.show()

            elif self.champWin22.text() != self.champWin23.text():
                self.labelWin25.setText("Vous n'avez pas renseigné deux\nfois le même mot de passe !")
                self.labelWin25.setStyleSheet("color: red;")
                self.labelWin25.adjustSize()
                self.labelWin25.show()

            elif self.champWin22.text() == "" and self.champWin23.text() == "":
                self.labelWin25.setText("Renseignez un mot de passe")
                self.labelWin25.setStyleSheet("color: red;")
                self.labelWin25.adjustSize()
                self.labelWin25.show()

            else:
                self.labelWin25.setText("Une erreur s'est déroulée")
                self.labelWin25.setStyleSheet("color: red;")
                self.labelWin25.adjustSize()
                self.labelWin25.show()

# ----- Fin class principale ------

if __name__ == "__main__":
    app = IntroWindow()
    connexion = ConnectionWindow()
    exit()
