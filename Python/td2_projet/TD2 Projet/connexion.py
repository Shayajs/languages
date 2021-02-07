"""
Dernière version
Informations :
    Import total : sys, os, tkinter, threading(Thread, pickle, time(sleep), PyQt5
    PyQt5 > QtWidjets, QtGui, QtCore(Qt)
"""
# Version: 0.2.4
# Author: Lucas Espinar
# Copyright: Creative Common


version = '0.2.4'


import sys
import os
from tkinter import Tk

try:
    from PyQt5.QtCore import Qt

    os.chdir(os.path.dirname(os.path.realpath("main.pyw")))
    print(os.getcwd())
except:
    print("Un problème est survenu...")
    os.system("python3 -m pip imstall pip --upgrade")
    os.system("python3 -m pip install PyQt5")
    os.system("conda install -c dsdale24 pyqt5")

try:
    import PyQt5
except:
    os.system("pip uninstall PyQt5 && pip uninstall PyQt5-sip && pip uninstall PyQtWebEngine")
    os.system("pip install PyQt5 && pip install PyQt5-sip && pip install PyQtWebEngine")

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMainWindow,qApp
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt
import sys
from time import sleep
from threading import Thread
import pickle

import urllib.request

from module.util import Recver, center, getBackgroundColor, choicedBackgroundColor

with open("./bin/version.vspi", "w") as v:
    v.write(version)

## DEBUT PROGRAMME ------------------------------

def verif_ver() -> str:
    try:
        url = urllib.request.Request("https://raw.githubusercontent.com/Shayajs/languages/master/Python/td2_projet/TD2%20Projet/bin/version.vspi")
        url_open = urllib.request.urlopen(url)
        send = url_open.read().decode('utf-8')
        send = send.split("\n")[0]
        print(f"> Dernière version en ligne {send} <")
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
        self.win.setWindowTitle("TD2 Projects")
        self.win.setWindowFlag(Qt.FramelessWindowHint)
        self.win.show()
        self.label = QLabel(self.win)
        self.pixmap = QPixmap('.\\bin\\intro.png')
        self.label.setPixmap(self.pixmap)
        self.win.setCentralWidget(self.label)
        self.win.setWindowIcon(QIcon("./bin/icon.png"))
        # self.win.resize(self.pixmap.width(), self.pixmap.height())

        self.label2 = QLabel(self.win)
        self.label2.setFont(QFont('Mangal', 11))
        self.label2.setStyleSheet("color: white; font-weight: bold;")
        self.label2.setText("Ouverture en cours... Veuillez Patienter")
        self.label2.move(10, 295)
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
        qApp.quit()



# -------- Principal -----------

class ConnectionWindow:

    """
    Fenetre de connexion en local. Impossible pour le moment de se connecter à un réseau
    et de s'enregistrer dedans 
    """


    def __init__(self):
        ## Variables autres -----------------------
        global version

        self.colorText = "color: black;"

        if choicedBackgroundColor() == 1:
            self.colorText = "color: white;"

        self.version = version
        self.files_enregistrement = None
        self.connected_one = None

        try:
            with open("./bin/comptes.spi", "rb") as file:
                depickle = pickle.Unpickler(file)
                self.files_enregistrement = depickle.load()

        except:
            with open("./bin/comptes.spi", "wb") as file:
                self.files_enregistrement = {"uadmin":"padmin"}
                pickler = pickle.Pickler(file)
                pickler.dump(self.files_enregistrement)

        ## APPLICATION ----------------------------

        self.app = QApplication(sys.argv)
        self.win = QWidget()
        x,y = 550, 320
        self.posx, self.posy = center(x, y)
        self.win.setGeometry(self.posx,self.posy,x,y)
        self.win.setWindowTitle("Page de Connexion")
        self.win.setWindowFlag(Qt.FramelessWindowHint)
        self.win.setWindowIcon(QIcon("./bin/icon1.png"))
        self.win.show()

        self.label0 = QLabel(self.win)
        self.label0.move(0,0)
        self.label0.resize(x, y)
        self.label0.setStyleSheet(getBackgroundColor())
        self.label0.show()

        self.label1 = QLabel(self.win)
        self.label1.setText("Connexion")
        self.label1.move(20, 20)
        self.label1.setFont(QFont('Mangal', 80))
        self.label1.setStyleSheet(self.colorText)
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
        self.label3.setStyleSheet(self.colorText)
        self.label3.adjustSize()
        self.label3.show()
        self.threadLabel3 = Thread(None, self.version_search)
        self.threadLabel3.start()

        self.champ1 = QLineEdit(self.win)
        self.champ1.move(20, 140)
        self.champ1.resize(220, 30)
        self.champ1.setFont(QFont('Mangal', 15))
        self.champ1.show()

        self.champ2 = QLineEdit(self.win)
        self.champ2.setEchoMode(QLineEdit.Password)
        self.champ2.move(20, 180)
        self.champ2.setFont(QFont('Mangal', 15))
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
        self.bouton2.move(220, 220)
        self.bouton2.setFont(QFont('Mangal', 20))
        self.bouton2.clicked.connect(self.register_window)
        self.bouton2.show()

        self.bouton3 = QPushButton(self.win)
        self.bouton3.setText("Fermer")
        self.bouton3.move(20, 270)
        self.bouton3.setFont(QFont('Mangal', 11))
        self.bouton3.clicked.connect(self.quitter)
        self.bouton3.show()

        self.bouton4 = QPushButton(self.win)
        self.bouton4.setText("Télécharger ?")
        self.bouton4.move(400, 220)
        self.bouton4.setFont(QFont('Mangal', 20))
        self.bouton4.setStyleSheet(self.colorText)
        self.bouton4.clicked.connect(self.updateDownload)

        # --------------- Page d'enregistrement --------------

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

        self.app.exec_()

    def connection(self) -> None:
        """
        Module connexion
        """
        admin = False
        admin_list = None

        try:
            with open("./bin/admin.spi", "rb") as adm:
                pic = pickle.Unpickler(adm)
                admin_list = pic.load()
        except:
            with open("./bin/admin.spi", "wb") as adm:
                pic = pickle.Pickler(adm)
                pic.dump(["uadmin", "Shayajs"])

        tha = Thread(None, self._timer_labe2)
        try:
            if self.files_enregistrement[self.champ1.text()] and self.files_enregistrement[self.champ1.text()] == self.champ2.text() :

                self.label2.setText("Connecté !")
                self.label2.setStyleSheet("color : green;")
                self.label2.adjustSize()
                self.label2.show()
                self.connected_one = (self.champ1.text(), True)

                if os.path.exists('./temp/'):
                    pass
                else:
                    os.mkdir("temp")

                if self.champ1.text() in admin_list:
                    admin = True

                with open("./temp/c.spi", "wb") as connectOPEN:
                    current = {"user": self.champ1.text(), "admin":admin}
                    pick = pickle.Pickler(connectOPEN)
                    pick.dump(current)
                    connectOPEN.close()

                self.quitter()
                self.win.setVisible(False)

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

        try:
            verif = verif_ver()

            splited1 = verif.split(".")
            splited2 = self.version.split(".")

            for i in range(0, 3):
                if splited1[i] == splited2[i]:
                    pass
                elif splited1[i] > splited2[i]:
                    a = 1
                    break
                elif splited1[i] < splited2[i]:
                    b = 1
                    break

            if b == a:
                self.label3.setText("Vous êtes à jour")
                self.label3.adjustSize()
                self.label3.setStyleSheet("color: green;")

            elif b < a:
                self.label3.setText(f"La version {verif} est disponible !")
                self.label3.adjustSize()
                self.label3.setStyleSheet("color: steelblue;")
                self.bouton4.show()

            elif b > a:
                self.label3.move(250, 170)
                self.label3.setText(f"Votre version ({self.version}) est une version beta !\n(Version en ligne : {verif})")
                self.label3.setStyleSheet("color: goldenrod;")
                self.label3.adjustSize()

            else:
                self.label3.setText("Impossible de vérifier les mises à jours.")
        except:
            self.label3.setText("Impossible de vérifier les mises à jours.")
            self.label3.adjustSize()

    def _timer_labe2(self) -> None:
        """
        Permettre un affichage limité de l'étiquette de connexion
        """
        sleep(2.5)
        self.label2.setVisible(False)
        self.win2.setVisible(False)

    def quitter(self) -> None:
        """
        Quitter l'application
        """
        self.app.quit()
        # QtWidgets.qApp.quit()

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
            threadExceptLabel2 = Thread(None, self._timer_labe2)
            threadExceptLabel2.start()

    def register(self):
        """
        Page d'enregistrement
        """
        a = 0
        try:
            self.files_enregistrement[self.champWin21.text()]
            a = 1
        except:
            a = 2

        if a == 1:
            self.labelWin25.setText("Ce compte est déjà enregistré !")
            self.labelWin25.setStyleSheet("color: red;")
            self.labelWin25.adjustSize()
            self.labelWin25.show()

        elif a == 2:
            if self.champWin22.text() == self.champWin23.text() and (self.champWin22.text() != "" and self.champWin23.text() != ""):

                self.files_enregistrement[self.champWin21.text()] = self.champWin22.text()

                self.labelWin25.setText("Enregistrement en cours ...")

                with open("./bin/comptes.spi", "wb") as file:
                    pickler = pickle.Pickler(file)
                    pickler.dump(self.files_enregistrement)

                self.labelWin25.setText("Enregistré")
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
                self.labelWin25.setStyleSheet("color: steelblue;")
                self.labelWin25.adjustSize()
                self.labelWin25.show()

    def updateThread(self):

        self.champ1.setVisible(False)
        self.champ2.setVisible(False)
        self.bouton4.setVisible(False)
        self.label3.setText("Téléchargement en cours...")
        self.label3.setFont(QFont('Mangal', 30))
        self.label3.move(30, 140)
        self.label3.adjustSize()
        self.bouton1.setVisible(False)
        self.bouton2.setVisible(False)

    def updateStateTwo(self):
        self.label3.setText("Installation en cours")

    def updateDownload(self):

        sender = Recver()
        tha = Thread(None, self.updateThread)
        tha.start()
        thb = Thread(None, sender.recvtd2, None, (self.label3,))

        try:
            thb.start()
        except:
            self.label3.setStyleSheet("color: red;")
            self.label3.setText("Le serveur est down")

# ----- Fin class principale ------

if __name__ == "__main__":
    # app = IntroWindow()
    connexion = ConnectionWindow()
    sleep(2)
    try:
        os.remove("./temp/c.spi")
        os.rmdir("temp")
    except:
        print("Vous avez fermé la fenêtre avant de vous connecter")
    exit()
