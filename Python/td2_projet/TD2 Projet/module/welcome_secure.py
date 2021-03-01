from module.util import Recver, exceptionRaised


try:
    from pickle import Pickler
    from module.util import Donnees, Online, center, setBackgroundColor, getBackgroundColor, choicedBackgroundColor
    from module.python_together import PythonTogether
    from PyQt5.QtCore import QMargins
    from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QTableWidget, QTableWidgetItem, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton
    from PyQt5.QtGui import QIcon, QFont
    import sys
    import os
    from module.util import Donnees, center, setBackgroundColor, getBackgroundColor, choicedBackgroundColor
    
    class WelcomeWindow:
        """
        C'est la page principale après connexion
        """

        def __init__(self):

            self.colorText = "color: black;"

            if choicedBackgroundColor() == 1:
                self.colorText = "color: white;"
            try:
                self.user = Donnees.current_user['user']
            except:
                self.user = "Test"
            try:
                self.version = Donnees.version
            except:
                self.version = version
            
            try:
                self.isAdmin = Donnees.current_user['admin']
            except:
                self.isAdmin = False

            self.app = QApplication(sys.argv)
            self.win = QWidget()
            x, y = 1280, 720
            self.x, self.y = center(x, y)
            self.win.setGeometry(self.x, self.y, x, y)
            self.win.setFixedSize(x, y)

            if not self.isAdmin:
                self.win.setWindowTitle(f"Projets SPI — {self.user} — {self.version}")
            elif self.isAdmin:
                self.win.setWindowTitle(f"Projets SPI — {self.user} — {self.version} (Administrateur)")

            self.win.setWindowIcon(QIcon("./bin/icon1"))
            self.win.show()

            self.label0 = QLabel(self.win)
            self.label0.move(0, 0)
            self.label0.resize(x, y)
            self.label0.setStyleSheet(getBackgroundColor())
            self.label0.show()
            self.v_box = QVBoxLayout()
            self.v_box.addWidget(self.label0)
            self.v_box.setSpacing(0)
            self.v_box.setContentsMargins(QMargins(0,0,0,0))
            self.win.setLayout(self.v_box)

            self.label1 = QLabel(self.win)
            if self.user != "Hors Ligne":
                self.label1.setText(f"Bonjour {self.user}")
            else:
                self.label1.setText(f"Vous êtes {self.user}")
            self.label1.setStyleSheet(self.colorText)
            self.label1.move(20, 20)
            self.label1.setFont(QFont('Mangal', 50))
            self.label1.adjustSize()
            self.label1.show()

            self.label2 = QLabel(self.win)
            if self.user != "Hors Ligne":
                self.label2.setText(f"Choisissez un projet {self.user}")
            else:
                self.label2.setText("Choissisez un projet")
            self.label2.move(20, 140)
            self.label2.setFont(QFont('Mangal', 15))
            self.label2.setStyleSheet(self.colorText)
            self.label2.adjustSize()
            self.label2.show()

            self.bouton1 = QPushButton(self.win)
            self.bouton1.setText("Paramètres")
            self.bouton1.move(900, 20)
            self.bouton1.clicked.connect(self.parameters)
            self.bouton1.show()

            if self.isAdmin:
                self.boutonadmin = QPushButton(self.win)
                self.boutonadmin.setText("Gestions Utilisateurs")
                self.boutonadmin.move(900, 60)
                self.boutonadmin.clicked.connect(self.management)
                self.boutonadmin.adjustSize()
                self.boutonadmin.show()

            self.bouton2 = QPushButton(self.win)
            self.bouton2.setText("Python Together")
            self.bouton2.setFont(QFont('Mangal', 20))
            self.bouton2.move(40, 210)
            self.bouton2.clicked.connect(self.pythonTogether)
            self.bouton2.adjustSize()
            self.bouton2.show()

            self.bouton3 = QPushButton(self.win)
            self.bouton3.setText("Voiture télécommandée")
            self.bouton3.setEnabled(False)
            self.bouton3.setFont(QFont('Mangal', 20))
            self.bouton3.move(40, 260)
            self.bouton3.clicked.connect(self.pythonTogether)
            self.bouton3.adjustSize()
            self.bouton3.show()

            self.label3 = QLabel(self.win)
            self.label3.setText("Projets en cours :\n  * Python Together (Projet à ses débuts)\n  * Voiture télécommandée")
            self.label3.move(40, 320)
            self.label3.setFont(QFont('Mangal', 15))
            self.label3.setStyleSheet(self.colorText)
            self.label3.adjustSize()
            self.label3.show()

            self.label4 = QLabel(self.win)

            if Donnees.online:
                self.label4.setText(Recver.monIp())
                
            self.label4.move(1050, 20)
            self.label4.setStyleSheet(self.colorText)
            self.label4.show()

            sys.exit(self.app.exec_())
        
        def pythonTogether(self):

            self.win3 = QMainWindow()
            self.open = QWidget()
            PythonTogether(self.win3, self.win, self.open)
        
        def management(self):
            
            def save():
                print(Donnees.admin)
                print("Test : Saved")
                for i in range(Row):
                    test = self.table.item(i, 1).text()
                    if test == "True":
                        test = True
                    
                    else:
                        if self.table.item(i, 0).text() == "Shayajs" or self.table.item(i, 0).text() == "uadmin":
                            test = True
                            if self.table.item(i, 1).text() == "False":
                                self.label001.show()
                                
                        else:
                            test = False
                    
                    if test and self.table.item(i, 0).text() not in Donnees.admin:
                        Donnees.admin.append(self.table.item(i, 0).text())
                    elif not test and self.table.item(i, 0).text() in Donnees.admin:
                        Donnees.admin.remove(self.table.item(i, 0).text())

                print(Donnees.admin)
                with open("./bin/admin.spi", "wb") as adminfile:
                    a = Pickler(adminfile)
                    a.dump(Donnees.admin)

                b = Online()
                b.uploadftp("admin.spi", "./bin/")
                    

            self.winadmin = QWidget()
            self.winadmin.setGeometry(50, 50, 500, 800)
            self.winadmin.setWindowTitle("Admin Param")
            self.winadmin.show()
            self.box = QVBoxLayout()

            self.table = QTableWidget()
            self.table.setColumnCount(3)
            Row = 0
            comptes = []
            for i in Donnees.comptes:
                comptes.append(i)
                Row += 1
            
            self.table.setRowCount(Row)
            
            self.box.addWidget(self.table)
            self.box.setContentsMargins(QMargins(100, 5, 5, 5))
            self.winadmin.setLayout(self.box)
            
            self.table.show()
    
            for i in range(len(comptes)):
                self.table.setItem(i, 0, QTableWidgetItem(comptes[i]))
                self.table.setItem(i, 1, QTableWidgetItem())

                if comptes[i] in Donnees.admin:
                    self.table.setItem(i, 1, QTableWidgetItem(str(True)))
                
                else:
                    self.table.setItem(i, 1, QTableWidgetItem(str(False)))
            
            self.bouton001 = QPushButton(self.winadmin)
            self.bouton001.setText("Enregistrer\nEt\nEnvoyer")
            self.bouton001.clicked.connect(save)
            self.bouton001.move(10, 50)
            self.bouton001.adjustSize()
            self.bouton001.show()

            self.label001 = QLabel(self.winadmin)
            self.label001.setText("'Shayajs'\nne peut être\nmodifié")
            self.label001.move(10, 80)

        def parameters(self):
            """
            Module des paramètres
            """
            if choicedBackgroundColor() == 1:
                self.colorText = "color: white;"
            
            else:
                self.colorText = "color: black;"

            self.win2 = QWidget()
            x, y = 450, 720
            self.x, self.y = center(x, y)
            self.win2.setGeometry(self.x, self.y, x, y)

            if not self.isAdmin:
                self.win2.setWindowTitle(f"Paramètres — {self.user}")
            elif self.isAdmin:
                self.win2.setWindowTitle(f"Paramètres — {self.user} (Administrateur)")

            self.win2.setWindowIcon(QIcon("./bin/icon1"))
            self.win2.show()

            self.label02 = QLabel(self.win2)
            self.label02.move(0, 0)
            self.label02.resize(x, y)
            self.label02.setStyleSheet(getBackgroundColor())
            self.label02.show()

            self.label12 = QLabel(self.win2)
            self.label12.setText("Thème")
            self.label12.move(20, 20)
            self.label12.setFont(QFont('Mangal', 15))
            self.label12.setStyleSheet(self.colorText)
            self.label12.adjustSize()
            self.label12.show()

            self.radio1 = QRadioButton(self.win2)
            self.radio1.setText("Mode Sombre")
            self.radio1.toggled.connect(lambda: setBackgroundColor(1))
            self.radio1.setStyleSheet(self.colorText)
            self.radio1.move(20, 60)

            if choicedBackgroundColor() == 1:
                self.radio1.setChecked(True)

            self.radio1.show()

            self.radio2 = QRadioButton(self.win2)
            self.radio2.setText("Mode Clair")
            self.radio2.toggled.connect(lambda: setBackgroundColor(2))
            self.radio2.setStyleSheet(self.colorText)
            self.radio2.move(20, 80)

            if choicedBackgroundColor() == 2:
                self.radio2.setChecked(True)

            self.radio2.show()

            self.label22 = QLabel(self.win2)
            self.label22.setText("Serveur")
            self.label22.move(20, 110)
            self.label22.setFont(QFont('Mangal', 15))
            self.label22.setStyleSheet(self.colorText)
            self.label22.adjustSize()
            self.label22.show()

            self.champ12 = QLineEdit(self.win2)
            try:
                self.champ12.setText(Donnees.serveur_project)
            except:
                pass
            self.champ12.move(20, 140)
            self.champ12.resize(120, 30)
            self.champ12.show()

            self.champ22 = QLineEdit(self.win2)
            try:
                self.champ22.setText(str(Donnees.server_ip_port))
            except:
                pass
            self.champ22.move(150, 140)
            self.champ22.resize(30, 30)
            self.champ22.show()

            self.bouton12 = QPushButton(self.win2)
            self.bouton12.setText("Appliquer")
            self.bouton12.move(20, 180)
            self.bouton12.clicked.connect(self.changeServer)
            self.bouton12.show()

            self.label32 = QLabel(self.win2)
            self.label32.move(110, 180)
            self.label32.setStyleSheet(self.colorText)
            self.label32.adjustSize()

            self.label42 = QLabel(self.win2)
            self.label42.setText("Vider le dossier log")
            self.label42.move(20, 220)
            self.label42.setFont(QFont('Mangal', 15))
            self.label42.setStyleSheet(self.colorText)
            self.label42.adjustSize()
            self.label42.show()

            self.bouton22 = QPushButton(self.win2)
            self.bouton22.setText("Appliquer")
            self.bouton22.move(20, 250)
            self.bouton22.clicked.connect(self.supprLogs)
            self.bouton22.show()

            self.label52 = QLabel(self.win2)
            self.label52.move(110, 255)
            self.label52.setStyleSheet(self.colorText)
            self.label52.adjustSize()

        
        def changeServer(self):
            """
            Changer de serveur
            """
            if self.champ12.text() != "" and self.champ22.text() != "":
                Donnees.serveur_project = self.champ12.text()
                Donnees.server_ip_port = self.champ22.text()
                self.label32.setText("Fait")
                self.label32.move(110, 185)
                self.label32.adjustSize()
                self.label32.show()

            else:
                self.label32.setText("Champ 1 : Adresse // Champ 2 : Port\nVérifiez vos données")
                self.label32.adjustSize()
                self.label32.show()
        
        def supprLogs(self):
            for i in os.listdir("./log/"):
                os.remove("./log/"+i)
            
            self.label52.setText("Fait")
            self.label52.adjustSize()
            self.label52.show()

    if __name__ == "__main__":
        Donnees.current_user = {'user': "Test", "admin": True}

        version: str
        with open("./bin/version.vspi", "w") as v:
            v.write(version)
            Donnees.version = version
        Donnees.version = version
        test = WelcomeWindow()
        exit()
except:
    exceptionRaised()
