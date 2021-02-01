import os
from time import sleep

try:
    from connexion import *
except:
    from tkinter import *
    main = Tk()

    label = Label(main, text = "Vous n'avez pas le module connexion.pyw ou connexion.py")
    label.pack()

    main.mainloop()

app = IntroWindow()
winConnect = ConnectionWindow()

if os.path.exists("./temp/c.himeji"):
    os.remove("./temp/c.himeji")
else:
    print("Erreur")

exit()
