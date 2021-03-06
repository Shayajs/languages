from module.util import Online, Recver, exceptionRaised


try:
    from module.util import Donnees, center, setBackgroundColor, getBackgroundColor, choicedBackgroundColor
    from module.python_together import PythonTogether
    from pathlib import Path
    from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QGridLayout
    from PyQt5.QtGui import QIcon, QFont
    from connexion import version
    import sys
    import os
    from pickle import Pickler
    from PyQt5.QtCore import QMargins
    from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

    try:
        if __name__ == "__main__":
            from module.util import Donnees, center, setBackgroundColor, getBackgroundColor, choicedBackgroundColor
            os.chdir(Path(__file__).parent)
            sys.path.append("..")
            sys.path.append("..")
        pass

    except:
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

            if not self.isAdmin:
                self.win.setWindowTitle(f"Projets SPI — {self.user} — {self.version}")
            elif self.isAdmin:
                self.win.setWindowTitle(f"Projets SPI — {self.user} — {self.version} (Administrateur)")

            self.win.setWindowIcon(QIcon("./bin/icon1"))
            self.win.show()

            self.boutonBckColor = ""

            if choicedBackgroundColor() == 1:
                self.colorText = "color: white;"
                self.win.setStyleSheet(getBackgroundColor())
                self.boutonBckColor = "background-color: #202729;"

            self.label1 = QLabel(f"Vous êtes {self.user}",self.win)
            self.label1.setStyleSheet(self.colorText)
            self.label1.setFont(QFont('Mangal', 50))

            self.label2 = QLabel("Choissisez un projet",self.win)
            if self.user != "Hors Ligne":
                self.label2.setText(f"Choisissez un projet {self.user}")
                self.label1.setText(f"Bonjour {self.user}")
            self.label2.setFont(QFont('Mangal', 15))
            self.label2.setStyleSheet(self.colorText)
            
            self.bouton1 = QPushButton("Paramètres",self.win)
            self.bouton1.setStyleSheet(self.colorText+self.boutonBckColor)
            self.bouton1.clicked.connect(self.parameters)
            self.bouton1.setFixedWidth(100)

            if self.isAdmin:
                self.boutonadmin = QPushButton(self.win)
                self.boutonadmin.setText("Gestions Utilisateurs")
                self.boutonadmin.move(900, 60)
                self.boutonadmin.setStyleSheet(self.colorText+self.boutonBckColor)
                self.boutonadmin.clicked.connect(self.management)
                #self.boutonadmin.adjustSize()
                self.boutonadmin.setFixedWidth(100)
                #self.boutonadmin.show()

            self.bouton2 = QPushButton("Python Together",self.win)
            self.bouton2.setFont(QFont('Mangal', 20))
            self.bouton2.setStyleSheet(self.colorText+self.boutonBckColor)
            self.bouton2.clicked.connect(self.pythonTogether)
            self.bouton2.setFixedWidth(400)

            self.bouton3 = QPushButton("Voiture Télécommandée",self.win)
            self.bouton3.setEnabled(False)
            self.bouton3.setFont(QFont('Mangal', 20))
            self.bouton3.setStyleSheet("color: gray;"+self.boutonBckColor)
            # self.bouton3.clicked.connect(self.pythonTogether)
            self.bouton3.setFixedWidth(400)

            self.label3 = QLabel("Projets en cours :\n  * Python Together (Projet à ses débuts)\n  * Voiture télécommandée",self.win)
            self.label3.setFont(QFont('Mangal', 15))
            self.label3.setStyleSheet(self.colorText)

            self.label4 = QLabel(self.win)
            if Donnees.online:
                self.label4.setText(Recver.monIp())

            self.label4.setStyleSheet(self.colorText)

            grid_layout = QGridLayout()
            self.win.setLayout(grid_layout)

            grid_layout.addWidget(self.label1, 0, 0, 1, 4)
            grid_layout.addWidget(self.label2, 2, 0, 1, 1)
            grid_layout.addWidget(self.bouton1, 0, 5, 1, 1)
            grid_layout.addWidget(self.bouton2, 4, 0, 1, 1)
            grid_layout.addWidget(self.bouton3, 5, 0, 1, 1)
            grid_layout.addWidget(self.label3, 6, 0, 1, 1)
            if self.isAdmin:
                grid_layout.addWidget(self.boutonadmin, 1, 5, 1, 1)
            grid_layout.addWidget(self.label4, 0, 4, 1, 1)

            grid_layout.setContentsMargins(40, 20, 20, 20)

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

            self.label12 = QLabel("Thème",self.win2)
            self.label12.setFont(QFont('Mangal', 15))

            self.radio1 = QRadioButton("Mode Sombre",self.win2)
            self.radio1.toggled.connect(lambda: setBackgroundColor(1))

            self.radio2 = QRadioButton("Mode Clair",self.win2)
            self.radio2.toggled.connect(lambda: setBackgroundColor(2))

            self.label22 = QLabel("Serveur",self.win2)
            self.label22.setFont(QFont('Mangal', 15))

            self.champ12 = QLineEdit(self.win2)
            try:
                self.champ12.setText(Donnees.serveur_project)
            except:
                pass
            self.champ12.setFixedWidth(120)

            self.champ22 = QLineEdit(self.win2)
            try:
                self.champ22.setText(str(Donnees.server_ip_port))
            except:
                pass
            self.champ22.setFixedWidth(30)

            self.bouton12 = QPushButton("Appliquer",self.win2)
            self.bouton12.clicked.connect(self.changeServer)
            self.bouton12.setFixedWidth(100)
            
            self.label32 = QLabel(self.win2)

            self.label42 = QLabel("Vider le dossier log",self.win2)
            self.label42.setFont(QFont('Mangal', 15))

            self.bouton22 = QPushButton("Appliquer",self.win2)
            self.bouton22.clicked.connect(self.supprLogs)
            self.bouton22.setFixedWidth(100)
            
            self.label52 = QLabel(self.win2)
            
            if choicedBackgroundColor() == 1:
                self.colorText = "color: white;"
                self.win2.setStyleSheet(getBackgroundColor())
                self.radio1.setChecked(True)
            else:
                self.colorText = "color: black;"
                self.radio2.setChecked(True)
            
            self.label12.setStyleSheet(self.colorText)
            self.radio1.setStyleSheet(self.colorText)
            self.radio2.setStyleSheet(self.colorText)
            self.label22.setStyleSheet(self.colorText)
            self.champ12.setStyleSheet(self.colorText)
            self.champ22.setStyleSheet(self.colorText)
            self.bouton12.setStyleSheet(self.colorText+self.boutonBckColor)
            self.label42.setStyleSheet(self.colorText)
            self.bouton22.setStyleSheet(self.colorText+self.boutonBckColor)
            self.label52.setStyleSheet(self.colorText)
            self.label32.setStyleSheet(self.colorText)
            
            self.h_box1 = QHBoxLayout()
            self.h_box1.addWidget(self.champ12)
            self.h_box1.addWidget(self.champ22)
            self.h_box1.addStretch()
            
            self.h_box2 = QHBoxLayout()
            self.h_box2.addWidget(self.bouton12)
            self.h_box2.addWidget(self.label32)
            self.h_box2.addStretch()
            
            self.h_box3 = QHBoxLayout()
            self.h_box3.addWidget(self.bouton22)
            self.h_box3.addWidget(self.label52)
            self.h_box3.addStretch()
            
            self.v_box = QVBoxLayout()
            self.v_box.addWidget(self.label12)
            self.v_box.addWidget(self.radio1)
            self.v_box.addWidget(self.radio2)
            self.v_box.addWidget(self.label22)
            self.v_box.addLayout(self.h_box1)
            self.v_box.addLayout(self.h_box2)
            self.v_box.addWidget(self.label42)
            self.v_box.addLayout(self.h_box3)
            self.v_box.addStretch()
            self.win2.setLayout(self.v_box)

        def changeServer(self):
            """
            Changer de serveur
            """
            if self.champ12.text() != "" and self.champ22.text() != "":
                Donnees.serveur_project = self.champ12.text()
                Donnees.server_ip_port = self.champ22.text()
                self.label32.setText("Fait")
            else:
                self.label32.setText("Champ 1 : Adresse // Champ 2 : Port\nVérifiez vos données")
        
        def supprLogs(self):
            for i in os.listdir("./log/"):
                os.remove("./log/"+i)
            self.label52.setText("Fait")
            
except:
    exceptionRaised()
