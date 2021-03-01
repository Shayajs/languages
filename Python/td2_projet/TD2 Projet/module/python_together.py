from module.util import Recver, exceptionRaised


try:
    from module.util import Donnees, Online, center, setBackgroundColor, getBackgroundColor, choicedBackgroundColor
    from pathlib import Path
    from PyQt5.QtCore import QMargins
    from PyQt5.QtWidgets import QAction, QApplication, QBoxLayout, QLineEdit, QMainWindow, QMenu, QMenuBar, QTextEdit, QWidget, QPushButton, QLabel, QVBoxLayout
    from PyQt5.QtGui import QIcon, QFont
    import sys
    import time
    from threading import Thread

    class PythonTogether:
        
        def __init__(self,
                    win: QMainWindow,
                    winParent: QWidget,
                    open: QWidget) -> None:
            """
            Tous les utilitaires pour PTProject
            """

            self.win = win
            self.winParent = winParent
            self.open = open

            self.online = Online()

            self.winParent.setVisible(False)
            self.win.setWindowTitle("Python Together")

            self.a, self.b = 1280, 720
            self.x, self.y = center(self.a, self.b)
            self.win.setGeometry(self.x, self.y, self.a, self.b)
            self.win.show()

            self.label = QLabel(self.win)
            self.label.setText("Python Together 0.1")
            self.label.setFont(QFont('Mangal', 50))
            self.label.adjustSize()
            self.label.show()
            self.label.move(20,10)

            self.bouton1 = QPushButton(self.win)
            self.bouton1.setText("Revenir en arrière")
            self.bouton1.move(20, 100)
            self.bouton1.adjustSize()
            self.bouton1.clicked.connect(
                lambda: (self.winParent.setVisible(True), self.win.close()))
            self.bouton1.show()

            self.winEdit = QWidget(self.win)
            self.winEdit.setGeometry(0, 120, 1260, 600)
            self.winEdit.adjustSize()
            self.winEdit.show()
            self.layout = QVBoxLayout(self.winEdit)

            self.textEdit = QTextEdit()
            # self.text.move(20, 120)
            self.textEdit.setFont(QFont('Mangal', 15))
            self.textEdit.show()

            self.layout.addWidget(self.textEdit)
            self.winEdit.setLayout(self.layout)

            self.menuBar = QMenuBar(self.win)
            self.win.setMenuBar(self.menuBar)

            # Menu Bar
            self.fileMenu = QMenu("&Fichier", self.win)

            self.openAction = QAction("&Ouvrir", self.win)
            self.openAction.triggered.connect(self.openproject)
            self.openAction.setShortcut("Ctrl+O")

            self.saveAction = QAction("&Sauvegarder", self.win)
            self.saveAction.triggered.connect(self.saveFile)
            self.saveAction.setShortcut("Ctrl+S")

            self.saveOnlineAction = QAction("&Sauver en ligne", self.win)
            self.saveOnlineAction.triggered.connect(self.saveOnline)
            self.saveOnlineAction.setShortcut("Ctrl+Shift+S")

            self.loadOnlineAction = QAction("&Charger en ligne (Soon)", self.win)
            self.loadOnlineAction.triggered.connect(self.loadOnline)
            self.loadOnlineAction.setShortcut("Ctrl+Shift+O")

            self.fileMenu.addAction(self.openAction)
            self.fileMenu.addAction(self.saveAction)
            
            if Donnees.online:
                self.fileMenu.addAction(self.saveOnlineAction)
                self.fileMenu.addAction(self.loadOnlineAction)

            self.menuBar.addMenu(self.fileMenu)

        def openproject(self):

            self.open.setGeometry(50,50,200,200)
            self.open.setWindowTitle("Ouvrir")
            self.open.show()

            self.label11 = QLabel(self.open)
            self.label11.setText("Ouvrir fichier local\n(dans dossier ptprojects)")
            self.label11.move(20, 20)
            self.label11.show()

            self.champ = QLineEdit(self.open)
            self.champ.move(20, 60)
            self.champ.resize(160, 20)
            self.champ.show()

            self.bouton = QPushButton(self.open)
            self.bouton.setText("Ouvrir")
            self.bouton.move(20,90)
            self.bouton.clicked.connect(self.openFile)
            self.bouton.show()

        def openFile(self):
            try:
                with open("./module/ptprojects/"+self.champ.text(), "r") as f:
                    Donnees.ptfile = f.read()
                    Donnees.nameFileProject = self.champ.text()
                    self.label.setText(self.champ.text())
                    self.label.adjustSize()
                    self.textEdit.setText(Donnees.ptfile)
                    self.open.close()
            except:
                from traceback import print_exc
                print_exc()
                self.label11.setText("Impossible d'ouvrir")
        
        def saveFile(self):

            try:
                with open("./module/ptprojects/"+Donnees.nameFileProject, "w") as f:
                    f.write(self.textEdit.toPlainText())

            except:
                if Donnees.online:
                    a = f"{Donnees.current_user['user']}_python_{int(time.time())}.py"
                    with open(f"./module/ptprojects/{a}", "w") as f:
                        f.write(self.textEdit.toPlainText())
                        Donnees.nameFileProject = a
                        self.label.setText(a)
                        self.label.adjustSize()
                
                elif not Donnees.online:
                    a = f'python_{int(time.time())}.py'
                    with open(f"./module/ptprojects/{a}", "w") as f:
                        f.write(self.textEdit.toPlainText())
                        Donnees.nameFileProject = a
                        self.label.setText(a)
                        self.label.adjustSize()
        
        def saveOnline(self):
            self.online.uploadftp(Donnees.nameFileProject, "./module/ptprojects/")
            self.saveFile()
        
        def loadOnline(self):
            pass
            
except:
    exceptionRaised()
