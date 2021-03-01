"""
Dernière version
Informations :
    Import total : sys, os, tkinter, threading(Thread, pickle, time(sleep), PyQt5
    PyQt5 > QtWidjets, QtGui, QtCore(Qt)
"""
# Version: 0.3.1
# Author: Lucas Espinar & Lysandre
# Copyright: Creative Common


version = '0.3.1'



import sys
import os

try:
    from PyQt5.QtCore import Qt

    os.chdir(os.path.dirname(os.path.realpath("main.pyw")))
    # print(os.getcwd())

except:
    os.system("python -m pip install PyQt5")
    print("Un problème est survenu...")

from PyQt5.QtWidgets import QAction, QApplication, QMenu, QRadioButton, QWidget, QLabel, QLineEdit, QPushButton, QMainWindow,qApp
from PyQt5.QtGui import QFont, QIcon, QPixmap, QMovie
from PyQt5.QtCore import Qt, QSize
import sys
from time import sleep
from threading import Thread
import pickle

import urllib.request

from module.util import Donnees, Online, Recver, exceptionRaised, center, getBackgroundColor, choicedBackgroundColor
try:
    with open("./bin/version.vspi", "w") as v:
        v.write(version)
        Donnees.version = version
except:
   with open("version.vspi", "w") as v:
        v.write(version)
        Donnees.version = version    

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
        self.win.setWindowIcon(QIcon("./bin/icon.png"))
        self.win.show()
        self.label = QLabel(self.win)

        self.movie = QMovie("./bin/intro.gif")

        self.label.setMovie(self.movie)
        self.movie.start()

        self.win.setCentralWidget(self.label)

        self.label2 = QLabel(self.win)
        self.label2.setFont(QFont('Mangal', 11))
        self.label2.setStyleSheet("color: white; font-weight: bold;")
        self.label2.setText("Ouverture en cours... Veuillez Patienter")
        self.label2.move(10, 295)
        self.label2.adjustSize()
        self.label2.show()

        self.tha.start()

        self.app.exec_()

    def chargement(self, time = 15):

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
                sleep(0.5)
                self.label2.setText("Ouverture en cours...")

        sleep(1)


        self.win.setVisible(False)
        qApp.quit()
# -------- Principal -----------

class ConnectionWindow:

    """
    Fenetre de connexion en local. Impossible pour le moment de se connecter à un réseau
    et de s'enregistrer dedans 
    """
    current_user = None

    def __init__(self):
        ## Variables autres -----------------------
        global version

        self.colorText = ""
        if sys.platform == "win32":
            self.colorText = "color: #334d9b"

        if choicedBackgroundColor() == 1:
            self.colorText = "color: white;"

        self.version = version
        self.files_enregistrement = None
        self.connected_one = None

        self.ftp = Online()
        # self.ftp.downloadftp("comptes.spi")
        
        self.ftp.downloadftp("admin.spi")

        try:
            with open("./bin/comptes.spi", "rb") as file:
                depickle = pickle.Unpickler(file)
                self.files_enregistrement = depickle.load()
                Donnees.comptes = self.files_enregistrement

        except:
            with open("./bin/comptes.spi", "wb") as file:
                pickler = pickle.Pickler(file)
                pickler.dump({"uadmin": "padmin"})
                Donnees.comptes, self.files_enregistrement = {"uadmin": "padmin"}

        ## APPLICATION ----------------------------

        self.app = QApplication(sys.argv)
        self.win = QWidget()
        x,y = 650, 320
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
        self.label1.setText("Choix")
        self.label1.move(20, 10)
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
        self.label3.move(20, 190)
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
        # self.champ1.show()

        self.champ2 = QLineEdit(self.win)
        self.champ2.setEchoMode(QLineEdit.Password)
        self.champ2.move(20, 180)
        self.champ2.setFont(QFont('Mangal', 15))
        self.champ2.resize(220, 30)
        # self.champ2.show()

        self.bouton1 = QPushButton(self.win)
        self.bouton1.setText(" Se connecter ")
        self.bouton1.move(20, 220)
        self.bouton1.setFont(QFont('Mangal', 20))
        self.bouton1.clicked.connect(self.connection)

        self.openAction = QAction("&ouvrir", self.win)
        self.openAction.setShortcut("Return")
        self.openAction.triggered.connect(self.connection)
        self.win.addAction(self.openAction)
        # self.bouton1.show()

        self.bouton2 = QPushButton(self.win)
        self.bouton2.setText(" S'enregistrer ")
        self.bouton2.move(220, 220)
        self.bouton2.setFont(QFont('Mangal', 20))
        self.bouton2.clicked.connect(self.register_window)
        # self.bouton2.show()

        self.bouton3 = QPushButton(self.win)
        self.bouton3.setText("Fermer")
        self.bouton3.move(20, 270)
        self.bouton3.setFont(QFont('Mangal', 11))
        self.bouton3.clicked.connect(self.quitterNet)
        self.bouton3.show()

        self.bouton4 = QPushButton(self.win)
        self.bouton4.setText("Télécharger ?")
        self.bouton4.move(400, 220)
        self.bouton4.setFont(QFont('Mangal', 20))
        self.bouton4.setStyleSheet(self.colorText)
        self.bouton4.clicked.connect(self.updateDownload)

        self.radio1 = QRadioButton(self.win)
        self.radio1.setText("En Ligne")
        self.radio1.move(120, 275)
        self.radio1.setStyleSheet(self.colorText)
        self.radio1.adjustSize()
        self.radio1.toggled.connect(self.onlineOrNot)
        self.radio1.show()

        self.radio2 = QRadioButton(self.win)
        self.radio2.setText("Hors Ligne")
        self.radio2.move(200, 275)
        self.radio2.setStyleSheet(self.colorText)
        self.radio2.adjustSize()
        self.radio2.toggled.connect(self.onlineOrNot)
        self.radio2.show()

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

    def onlineOrNot(self) -> None:
        if Donnees.online_final == False:
            self.radio1.setCheckable(False)
            self.radio1.setStyleSheet("color : red;")


        if self.radio1.isChecked():
            
            self.bouton2.show()
            self.bouton1.show()
            self.label1.setText("Connexion")
            self.label1.adjustSize()
            self.bouton1.setText(" Se connecter ")
            self.bouton1.adjustSize()
            self.bouton2.setVisible(True)
            self.champ1.setVisible(True)
            self.champ2.setVisible(True)
            self.label3.setVisible(True)
            self.label3.move(250, 170)
            self.label3.show()
            Donnees.online = True
            self.ftp.downloadftp("comptes.spi")
        
        elif self.radio2.isChecked():

            self.label1.setText("Offline")
            self.label1.adjustSize()
            self.bouton1.setText(" Se connecter Hors Ligne ")
            self.bouton1.show()
            self.bouton1.adjustSize()
            self.bouton2.setVisible(False)
            self.champ1.setVisible(False)
            self.champ2.setVisible(False)
            self.label3.setVisible(False)

            Donnees.online = False

    def connection(self) -> None:
        """
        Module connexion
        """
        admin = False
        admin_list = None
        if self.radio1.isChecked():
            try:
                with open("./bin/admin.spi", "rb") as adm:
                    pic = pickle.Unpickler(adm)
                    admin_list = pic.load()
                    Donnees.admin = admin_list
            except:
                with open("./bin/admin.spi", "wb") as adm:
                    pic = pickle.Pickler(adm)
                    pic.dump(["uadmin", "Shayajs"])
                    Donnees.admin = ["uadmin", "Shayajs"]

            tha = Thread(None, self._timer_labe2)
            try:
                if self.files_enregistrement[self.champ1.text()] and self.files_enregistrement[self.champ1.text()] == self.champ2.text() :

                    self.label2.setText("Connecté !")
                    self.label2.setStyleSheet("color : green;")
                    self.label2.adjustSize()
                    self.label2.show()
                    self.connected_one = (self.champ1.text(), True)

                    if self.champ1.text() in admin_list:
                        admin = True

                    Donnees.current_user = {"user": self.champ1.text(), "admin":admin}

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
        elif self.radio2.isChecked():
            self.quitter()
            self.win.setVisible(False)
            Donnees.current_user = {"user": "Hors Ligne", "admin":False}

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
                if int(splited1[i]) == int(splited2[i]):
                    pass
                elif int(splited1[i]) > int(splited2[i]):
                    a = 1
                    break
                elif int(splited1[i]) < int(splited2[i]):
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
                # self.label3.move(250, 170)
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
        self.win.setVisible(False)
        # self.app.quit()
        qApp.quit()

    def quitterNet(self):
        """
        Quitter l'application
        """
        Donnees.current_user = {"user": None, "admin": False}
        self.win.setVisible(False)
        # self.app.quit()
        qApp.quit()
        del self

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
            exceptionRaised()

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
                
                sleep(1)

                Donnees.comptes = self.files_enregistrement
                self.ftp.uploadftp("comptes.spi")

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
        self.radio1.setVisible(False)
        self.radio2.setVisible(False)
        self.bouton3.setText("Annuler")

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
    
    def __del__(self):
        print("Sortie sans connexion")
# ----- Fin class principale ------

if __name__ == "__main__":
    # app = IntroWindow()
    connexion = ConnectionWindow()

    sleep(2)
    try:
        print(Donnees.current_user)
    except:
        print("Pas eu de connexion !")
    exit()