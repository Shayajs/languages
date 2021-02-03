import os
from pickle import Pickler, Unpickler
import sys

os.chdir(os.path.dirname(os.path.realpath("main.py")))
sys.path.append(os.path.dirname(os.path.realpath("connexion.pyw")))

try:
    from connexion import *
    from module.welcome import *

except:
    from tkinter import *
    main = Tk()

    label = Label(main, text = "Vous n'avez pas le module connexion.py")
    label.pack()

    main.mainloop()



app = IntroWindow()
winConnect = ConnectionWindow()

user = None
with open("./temp/c.himeji", "rb") as user_connect:
    pickler = pickle.Unpickler(user_connect)
    user = pickler.load()
    user_connect.close()

winWelcome = WelcomeWindow(user["user"], user["admin"], winConnect.version)

try:
    os.remove("./temp/c.himeji")
    os.rmdir("temp")
except:
    pass

exit()
