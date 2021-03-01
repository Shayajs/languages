from pathlib import Path
import os
import sys
import time
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from tkinter import Tk, Label
from module.util import Online
from module.script import script

os.chdir(Path(__file__).parent)
sys.path.append(Path(__file__).parent)


"""
Binevenue dans le module principal
Etape 0 -> Importer Modules importants
Etape 1 -> Fenêtre de présentation
Etape 2 -> Fenetre de connexion
Etape 3 -> Fenêtre principale /!\ La faire quitter éteint l'application
"""

# Etape 0
try:
    from connexion import *
    from module.welcome import *
    from module.util import *

except:
    main = Tk()
    label = Label(main, text= "Une erreur s'est produite.\n\nCela arrive souvent avec l'installation de Conda et pip qui se gênent mutuellement")
    label.pack()

    main.mainloop()

try:
    if len(sys.argv) == 1:
        # Etape 1
        app = IntroWindow()

        # Etape 2
        winConnect = ConnectionWindow()

        # Etape 3
        if Donnees.current_user["user"] != None:
            winWelcome = WelcomeWindow() # sys.exit
        else:
            exit()
    
    else:
        script(sys.argv)
        pass
    
except Exception as ater:
    from traceback import print_exc
    from module.util import uploadftp
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
except SystemExit:
    pass

except:
    print(f"Unespected Error: {sys.exc_info()[0]}")

