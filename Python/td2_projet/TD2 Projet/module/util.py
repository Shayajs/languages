import sys
from urllib import request
from PyQt5.QtGui import QFont
from sys import platform
from time import sleep
import time
from tkinter import Tk
from urllib.request import *
import os
from sys import platform

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget
from ftplib import FTP



class Recver:
    """
    Classe de mise à jour
    """
    def monIp() -> str:
        Donnees.selfServeur = (request.urlopen(request.Request("https://api64.ipify.org/?format=py"))).read().decode("utf-8")
        return Donnees.selfServeur

    def recvtd2(self, label: QLabel):
        """
        Méthode principale pour la mise à jour
        """
        X = None

        label.setText("Connexion au serveur...")

        try:
            X = Request(
                "https://raw.githubusercontent.com/Shayajs/languages/master/Python/td2_projet/ptd2.tar.gz")
            print("Connexion publique")

            Y = urlopen(X)
            label.setText("Ouverture du lien")

            Z = Y.read()

            with open("../update.tar.gz", "wb") as recver:
                label.setText("Enregistrement en cours...")
                print("Enregistrement en cours")
                recver.write(Z)

            label.setText("Installation en cours")

            cwd = os.getcwd()
            print(cwd)
            os.chdir("../")
            print(os.getcwd())
            os.system("tar zxf update.tar.gz")

            if platform == "win32":
                os.system("del update.tar.gz")
            elif platform == "linux":
                os.system("rm update.tar.gz")
            else:
                os.system("rm update.tar.gz")

            os.chdir(cwd)

            label.setText("Installation terminée ! ")
            print(os.getcwd())

        except:
            label.setText(
                "Une erreur s'est\nproduite\nVérifiez votre connexion")
            Donnees.online = False


def uploadftp(ficdsk, ficftp=None):
    held = Online()
    held.uploadftp(ficdsk, ficftp)
    sleep(3)
    exit()

def center(x: int, y: int) -> tuple:
    """
    Permet de centrer une fenetre avec les coordonnées de x et y de la fenetre
    """
    calc = Tk()
    width = calc.winfo_screenwidth()
    height = calc.winfo_screenheight()
    ww = (width - x) // 2
    hh = (height - y) // 2
    return ww, hh


def setBackgroundColor(choice: int) -> None:
    """
    choice = 1 -> Background Color = #333d40
    choice = 2 -> No Background Color
    """

    if choice == 1:
        with open("bin/bckcolor", "w") as seter:
            seter.write("background-color: #333d40;")
            print("mode sombre")

    elif choice == 2:
        with open("bin/bckcolor", "w") as seter:
            seter.write("")
            print("mode clair")


def getBackgroundColor() -> str:
    """
    Récuopérer l'état du Background
    """
    try:
        with open("bin/bckcolor", "r") as seter:
            return seter.read()
    except:
        open("bin/bckcolor", "w").close()
        return ""


def choicedBackgroundColor() -> int:
    """
    Récupérer le choix de background
    """
    try:
        with open("bin/bckcolor", "r") as seter:
            if seter.read() == "background-color: #333d40;":

                return 1

            else:

                return 2
    except:
        try:
            open("bin/bckcolor", "w").close()
            return 2
        except:
            open("bckcolor", "w").close()
            return 2


class Donnees:
    """
    En variable de classe, elle permettent de ne pas sauvegarder sur un fichier, c'est plus simple et évite les fraudes, pour l'instant.
    Ça permet surtout pour la gestion de mémoire, touuuut à un seul endroit
    """

    current_user: dict = {}
    server_ip_port: int
    serveur_project: tuple
    version: str
    online: bool = False
    online_final: bool = None
    choice_project: int
    comptes: dict
    admin: list
    parametres = {
        "theme": getBackgroundColor(),
        "server": ("", 0)
        }
    
    ptfile: str
    nameFileProject: str
    selfServeur: str

def exceptionRaised():
    ater = "N/C"
    from traceback import print_exc
    tps = int(time.time())
    print_exc(file=open(f"./log/log_{tps}.txt", "w"))

    app_error = QApplication(sys.argv)
    win_error = QWidget()
    win_error.setGeometry(80, 80, 50, 50)
    win_error.setWindowTitle("Error Script")
    win_error.show()

    label_error = QLabel(win_error)
    label_error.setText(f"Une exception a été levée : {str(ater)}\n\n\n\n {open(f'./log/log_{tps}.txt').read()}")
    label_error.setStyleSheet("font-weight: bold;")
    label_error.setFont(QFont('Mangal', 10))
    label_error.move(20, 20)
    label_error.adjustSize()
    label_error.show()

    temp = Online()
    del temp
    
    if Donnees.online_final:
        bouton_send_error = QPushButton(win_error)
        bouton_send_error.setText("Envoyer rapport d'erreur")
        bouton_send_error.clicked.connect(lambda: uploadftp(f"log_{tps}.txt", "./log/"))
        bouton_send_error.move(20, 60)
        bouton_send_error.show()

    win_error.adjustSize()

    sys.exit(app_error.exec_())

class Online:
    """
    Classe pour discuter entre le serveur ftp et le script, enregistrer des fichier et en recevoir.
    """
    def __init__(self) -> None:
        try:
            self.clientftp = FTP(host="f29-preview.atspace.me", user="3754866_user", passwd="td2spiproject")
            Donnees.online = True
            Donnees.online_final = True
            
        except:
            Donnees.online_final = False

    def uploadftp(self, ficdsk, dossier=None):
        """télécharge le fichier ficdsk du disque dans le rép. courant du Serv. ftp
        - ficdsk: nom du fichier disque avec son chemin
        - ficftp: si mentionné => c'est le nom qui sera utilisé sur ftp
        """
        ficdsk1 = ""
        if dossier != None:
            ficdsk1 = dossier+ficdsk
        with open(ficdsk1, "rb") as f:
            self.clientftp.storbinary('STOR ' + ficdsk, f)


    def downloadftp(self, file_cible, dossier='./bin/'):
        """télécharge le fichier ficftp du serv. ftp dans le rép. repdsk du disque
       - file_cible: nom du fichier ftp dans le répertoire courant
       - repdsk: répertoire du disque dans lequel il faut placer le fichier
       - ficdsk: si mentionné => c'est le nom qui sera utilisé sur disque
        """

        ficdsk = file_cible
        with open(os.path.join(dossier, ficdsk), 'wb') as f:
            self.clientftp.retrbinary('RETR ' + file_cible, f.write)

    def __del__(self):
        try:
            self.clientftp.quit()
        except:
            self.clientftp.close()


