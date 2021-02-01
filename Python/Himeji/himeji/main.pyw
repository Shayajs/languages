import os
from pickle import Pickler, Unpickler

os.chdir(os.path.dirname(os.path.realpath("main.py")))

try:
    from connexion import *
except:
    from tkinter import *
    main = Tk()

    label = Label(main, text = "Vous n'avez pas le module ou connexion.py")
    label.pack()

    main.mainloop()

app = IntroWindow()
winConnect = ConnectionWindow()

os.remove("./temp/c.himeji")

exit()
