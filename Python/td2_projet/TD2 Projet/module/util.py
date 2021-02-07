from tkinter import Tk
from urllib.request import *
import os

from PyQt5.QtWidgets import QLabel

class Recver:
    def recvtd2(self, label: QLabel):
        X = None

        label.setText("Connexion au serveur...")
        try:
            X = Request("http://92.146.57.188:80/ptd2.tar.gz")
            print("Connexion publique")
        except:
            X = Request("http://192.168.1.2:8080/ptd2.tar.gz")
            print("Connexion privée")
        else:
            X = Request("http://localhost:8080/ptd2.tar.gz")
            print("Connexion locale")
        
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
        
        os.system("rd venv")
        os.chdir("../")
        os.system("rd ")
        print(os.getcwd())
        os.system("tar zxf update.tar.gz")
        os.system("del update.tar.gz")

        os.chdir(cwd)

        label.setText("Installation terminée ! ")
        print(os.getcwd())

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
            print("mode clair")
            seter.write("")


def getBackgroundColor() -> str:
    try:
        with open("bin/bckcolor", "r") as seter:
            return seter.read()
    except:
        open("bin/bckcolor", "w").close()
        return ""

def choicedBackgroundColor() -> int:
    try:
        with open("bin/bckcolor", "r") as seter:
            if seter.read() == "background-color: #333d40;":
                
                return 1
            
            else:
                
                return 2
    except:
        open("bin/bckcolor", "w").close()
        return 2
