import os
from pickle import Unpickler
import sys

os.chdir(os.path.dirname(os.path.realpath("main.py")))
sys.path.append(os.path.dirname(os.path.realpath("connexion.py")))

"""
Binevenue dans le module principal
Etape 0 -> Importer Modules importants
Etape 1 -> Fenêtre de présentation
Etape 2 -> Fenetre de connexion
Etape 3 -> Fenêtre principale /!\ Le faire quitter éteint l'application
"""

# Etaope 0
try:
    from connexion import *
    from module.welcome import *

except:
    from tkinter import *
    main = Tk()

    label = Label(main, text = "Vous n'avez pas le module connexion.py\nou\nUne erreur autre s'est déroulée.\n\nCela arrive souvent avec l'installation de Conda et pip qui se gênent mutuellement")
    label.pack()

    main.mainloop()
    
# Etape 1
app = IntroWindow()

# Etape 2
winConnect = ConnectionWindow()

user = None
try:
    with open("./temp/c.spi", "rb") as user_connect:
        pickler = Unpickler(user_connect)
        user = pickler.load()
        user_connect.close()
except:
    exit()

# Etape 3
winWelcome = WelcomeWindow(user["user"], user["admin"], winConnect.version) # sys.exit
