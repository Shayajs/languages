from connexion import version
from module.util import Online
import os

def script(args: list) -> None:

    helper = {"version": "Affiche la version du programme",
              "test": "test un paramètre personnalisé -> test [module]",
              "fileio": "Télécharger un fichier sur le cloud -> ddl [fichier] [Destination]",
              "dellogs": "Supprime tous les logs"}

    if args[1] == "-v" or args[1] == "--version":
        print(f"Version : {version}")
        exit()
    
    if args[1] == "--test":
        if args[2] == "welcome":
            from module.welcome import WelcomeWindow
            WelcomeWindow()

    if args[1] == "--help" or args[1] == "-h":
        try:
            if args[2] in helper:
                print(helper[args[2]])
            else:
                print("Cette commande n'existe pas")
        except:
            print()
            for i in helper:
                print(f"{i} : {helper[i]}", end="\n\n")

        exit()
    if args[1] == "--fileio":
        try:
            a = Online()
            a.downloadftp(args[2], args[3])
            print("Fait")
        except:
            from traceback import print_exc
            print_exc()
            print("Impossible d'accéder à ce fichier")
    
    if args[1] == "--dellogs":

            for i in os.listdir("./log/"):
                os.remove("./log/"+i)
            print("done")

    else:
        print(args[1:])
        print(f"La commande '{args[1]}' n'existe pas\nFaites -h ou --help pour accéder aux commandes disponibles.")
