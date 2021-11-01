from socket import AF_INET, SOCK_STREAM
from socket import socket as soc

if __name__ != "__main__":
    from login.tokens import TokenTime
if __name__ == "__main__":
    from tokens import TokenTime
    
from pickle import Pickler, Unpickler
import json
from os import remove
import time
from sys import argv
from threading import Thread

class LoginHost:
    
    """
        Commandes :
        
        001 - Demande de login
        002 - Demande de logup
        003 - Demande de logout
        004 - Demande de désinscription
        
        Login
        101 Coonected
        102 Already Connected
        103 Not Logup
        104 Error
        105 Error Inconnu

        Logup
        201 Logup
        202 Already Loged up
    """
    
    def __init__(self, ip = "", port = 8081) -> None:
        
        version = "0.1 Beta"
        
        try:
            with open("connexion.login", "rb") as login:
                unpick = Unpickler(login)
                logers = unpick.load()
                logers : dict
                logers["test"]["pwd"]
                
        except IOError:
            
            with open("connexion.login", "wb") as file:
                tok = TokenTime(taille=20, time_out=1)
                
                dict_base = {
                    "uadmin": {
                        "pwd": "padmin",
                        "admin": True,
                        "token": tok.getToken()
                    },
                    
                    "test": {
                        "pwd": "test",
                        "admin": False,
                        "token": "ABCD0000000000000000"
                    }
                }
                
                picklefile = Pickler(file)
                picklefile.dump(dict_base)
        
        except:
            print("Une erreur a été relevée.")
        
        # ------------------------------------
        
        self.accounts = None
        self.accounts: dict
        
        with open("connexion.login", "rb") as file:
            pic2 = Unpickler(file)
            self.accounts = pic2.load()
            
        self.host = soc(AF_INET, SOCK_STREAM)
        self.host.bind((ip, port))
        self.host.listen(5)
        self.connected = []
        self.clients = []
        
        print(f"Version {version}")
        
        self.looper = True
        self._thread_loop(self.demand_start)
        
        self.open = True
        self.true = True
        while self.true:
            if self.open:
                Thread(None, self._thread_loop, None, (self, self.demand_start))
                Thread.start()
                self.open = False
        
    def login(self, client: soc):
        """
        Si code 101 :
        Deux receptions, deux envoi (code & token)
        
        si code 102
        Deux Receptions, un envoi (code 102), une reception
        
        Si code 103 ou 104
        Deux receptions, un envoi (code)
        """
        
        with open("connexion.login", "rb") as file:
            pic2 = Unpickler(file)
            self.accounts = pic2.load()
        
        self.client = client
        user = self.client.recv(1024).decode("utf-8")
        pwd_temp = self.client.recv(1024).decode("utf-8")
        
        try:
            user_temp = self.accounts[user]
            if user not in self.connected:
                if pwd_temp == user_temp["pwd"]:
                    self.connected.append(user)
                    token_log = TokenTime(taille=20, time_out=1)
                    token = token_log.getToken()
                    self.accounts[user]["token"] = token
                    self.client.send(b"101")
                    time.sleep(0.01)
                    self.client.send(token.encode())
                    if __name__ == "__main__":
                        print(f"{user} connected on {self.client.getpeername()} ({self.client.getsockname()})!")
                    
                    self.demand_connected(client)
                
                else:
                    self.client.send(b"104")
            
            elif user in self.connected:
                self.client.send(b"102")
                time.sleep(0.5)
                tok_temp = self.client.recv(64).decode()
                time.sleep(0.2)
                
                if tok_temp == self.accounts[user]["token"]:
                    self.client.send(b"101")
                    print(f"{user} reconnected !")
                    self.demand_connected(client)
                
                elif tok_temp == "None":
                    print(f"{user} tente de se reconnecter avec une machine différente mais n'a pas le bon token.")
                    self.client.send(b"104")
                
                elif tok_temp != self.accounts[user]["token"]:
                    self.client.send(b"104")
                
                else:
                    self.client.send(b"105")
                    
            else:
                self.client.send(b"104")
                
        except Exception as e:
            print(e.__traceback__, e.__str__(), e.__context__)
            if user not in self.accounts:
                self.client.send(b"103")
                self.logup(self.client)
            
            else:
                self.client.send(b"105")
            
            self.client.send(str(e).encode())
            
    def logup(self, client: soc):
        """infos to send :
        username, pwd
        only that
        """
        
        self.client_logup = client
        # One send
        tok2 = TokenTime(taille=20)
        
        username = self.client.recv(1024).decode("utf-8")
        time.sleep(0.02)
        pwd = self.client.recv(1024).decode("utf-8")

        if username not in self.accounts:
            self.accounts[username] = {
                "pwd": pwd,
                "admin": False,
                "token": tok2.getToken()
            }
            
            with open("connexion.login", "wb") as file:
                picklefile = Pickler(file)
                picklefile.dump(self.accounts)
            
            self.client_logup.send(b"201")
            time.sleep(0.1)
            self.client_logup.send(self.accounts[username]["token"].encode())
            self.connected.append(username)
            
        elif username in self.accounts:
            self.client_logup.send(b"202")
            time.sleep(0.02)
            self.login(client)
        
        with open("connexion.login", "wb") as file:
            picklefile = Pickler(file)
            picklefile.dump(self.accounts)
            
    def logout(self, client: soc):
        """
        301 - logout success
        302 - logout unsuccess
        """
        try:
            username = client.recv(1024).decode("utf-8")
            user_token = client.recv(2048).decode("utf-8")
            
            if self.accounts[username]["token"] == user_token:
                self.connected.pop(self.connected.index(username))
                self.clients.pop(self.clients.index(client))
                client.close()
            if __name__ == "__main__":
                print(f"{username} disconnected !")
        except:
            print("impossible de déconnecter !")
    
    def recv(self, client: soc, encoding="utf-8") -> str:
        
        return client.recv(1024).decode(encoding=encoding)

    def demand_start(self):
        a, b = self.host.accept()
        self.clients.append(a)
        code = self.recv(a)
        if code == "001":
            self.login(a)
        
        if code == "002":
            self.logup(a)
        
        self.open = True
            
    def demand_connected(self, client: soc):
        if __name__ == "__main__":
            print(f"En attente de {client.getpeername()}")
        code = client.recv(1024).decode()
        if code == "001":
            self.login(client)
        
        if code == "002":
            self.logup(client)
        
        if code == "003":
            self.logout(client)
        
    def __delattr__(self, name: str) -> None:
        
        if name == "accounts":
            with open("connexion.login", "wb") as file:
                picklefile = Pickler(file)
                picklefile.dump(self.accounts)
    
    def _thread_loop(self, func):
        while self.looper:
            func()
    

class LoginClient:
    
    def __init__(self, server = "shayajs1.ddns.net", port=21):
        self.username = ...
        self.pwd = ...
        self.token = "None"
        self.server = server
        self.port = port
        self.client = soc(AF_INET, SOCK_STREAM)
        self.connected = False
        self.connected_client = False
        self.last_code = str()

        
    def send(self, message: str):
        try:
            time.sleep(0.01)
            self.client.send(message.encode())
        except:
            self.client.connect((self.server, self.port))
            self.connected = True
            time.sleep(0.01)
            self.client.send(message.encode())
        
        
    def login(self, username: str, pwd: str) -> ...:
        
        self.username = username
        if self.last_code != "202":
            self.send("001")
        if __name__ == "__main__":
            time.sleep(0.5)
        self.send(username)
        if __name__ == "__main__":
            time.sleep(0.5)
        self.send(pwd)
        respond = self.client.recv(1024).decode()
        if __name__ == "__main__":
            print(respond)
        
        if respond == "101":
            if __name__ == "__main__":
                print("Connected")
            self.token = self.client.recv(1024).decode()
            self.connected_client = True
            self.username = username
        
        if respond == "102":
            if __name__ == "__main__":
                print("Already Connected")
                response = input("Avez-vous un Token ? (Si oui insérer Token, si non, faites enter, si un token est déjà dans la base de donné de cette machine faites enter de même): ")
                if len(response) == 20:
                    self.token = response
            
            self.send(self.token)
            resp2 = self.client.recv(8).decode()
            
            if resp2 == "101":
                self.connected_client = True
            
            else:
                print("Error, impossible de se connecter")
        
        if respond == "103":
            
            print("Vous n'êtes pas enregistré.")
            yon = input("Voulez-vous vous enregistrer ? (O/n): ")
            if yon.capitalize() == "O":
                self.logup(username=username, pwd=pwd)
            else:
                self.client.close()
        
        if respond == "105":
            msg = self.client.recv(2048).decode()
            print(msg)
        
        if respond == "104":
            print("Impossible de se connecter")
    
    def logup(self, username, pwd):
        self.send("002")
        time.sleep(0.02)
        self.send(username)
        time.sleep(0.02)
        self.send(pwd)
        code = self.client.recv(8).decode()
        print(code)
        if code == "201":
            self.token = self.client.recv(2048).decode()
            self.connected_client = True
        
        if code == "202":
            time.sleep(0.02)
            self.login(username, pwd)
    
    def logout(self):
        self.client.send(b"003")
        time.sleep(0.2)
        self.client.send(self.username.encode())
        time.sleep(0.02)
        self.client.send(self.token.encode())


if __name__ == "__main__":
    argv.pop(0)
    if argv[0] == "host":
        host = LoginHost()
    
    elif argv[0] == "client":
        loopnot = ""
        token = "None"
        while loopnot != "stop":
            client = LoginClient("localhost", 8081)
            client.token = token
            client.login(input("Insert your username : "), input("Insert your password : "))
            token = client.token
            print(f"Connected :{client.connected_client}, token {client.token}")
            loopnot = input("Tape 'stop' to stop the loop or any else if you won't : ")
            if loopnot == "stop":
                client.logout()