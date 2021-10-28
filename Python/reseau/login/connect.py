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
    
    def __init__(self) -> None:
        
        
        
        with open("already.login.temp", "w"):
            pass # Just create and reinitialization of alp
        
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
        self.host.bind(("", 8081))
        self.host.listen(5)
        self.connected = []
        self.clients = []
        
    
    def login(self, client: soc):
        """
        Si code 101 :
        Deux receptions, deux envoi (code & token)
        
        si code 102
        Deux Receptions, un envoi (code 102), une reception
        
        Si code 103 ou 104
        Deux receptions, un envoi (code)
        """
        
        self.client = client
        user = self.client.recv(1024).decode("utf-8")
        
        try:
            user_temp = self.accounts[user]
            pwd_temp = self.client.recv(1024).decode("utf-8")
            if user not in self.connected:
                if pwd_temp == user_temp["pwd"]:
                    self.connected.append("user")
                    token_log = TokenTime(taille=20, time_out=1)
                    token = token_log.getToken()
                    self.accounts[user]["token"] = token
                    self.client.send(b"101")
                    time.sleep(0.01)
                    self.client.send(token.encode())
            
            elif user in self.connected:
                self.client.send(b"102")
                tok_temp = self.client.recv(64).decode()
                
                if tok_temp == self.accounts[user]["token"]:
                    self.client.send(b"101")
                
                else:
                    self.client.send(b"104")
                    
            else:
                self.client.send(b"104")
                
        except Exception as e:
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
        
        logup_infos_recv = self.client.recv(1024).decode("utf-8")
        logup_infos = json.loads(logup_infos_recv)
        if logup_infos["username"] not in self.accounts:
            self.accounts[logup_infos["username"]] = {
                "pwd": logup_infos["pwd"],
                "admin": False,
                "token": tok2.getToken()
            }
            
            self.client_logup.send(b"201")
            self.client_logup.send(self.accounts[logup_infos["username"]]["token"])
        
        else:
            self.client_logup.send(b"202")
        
        with open("connexion.login", "wb") as file:
            picklefile = Pickler(file)
            picklefile.dump(self.accounts)
    
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
        
    def __delattr__(self, name: str) -> None:
        
        if name == "accounts":
            with open("connexion.login", "wb") as file:
                picklefile = Pickler(file)
                picklefile.dump(self.accounts)
        
    def __del__(self):
        
        remove("already.login.temp")
    

class LoginClient:
    
    def __init__(self, server = "shayajs1.ddns.net", port=21):
        self.username = ...
        self.pwd = ...
        self.token = ""
        self.server = server
        self.port = port
        self.client = soc(AF_INET, SOCK_STREAM)
        self.connected = False
        self.connected_client = False

        
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
        
        if respond == "102":
            if __name__ == "__main__":
                print("Already Connected")
            self.send(self.token)
            
            resp2 = self.client.recv(8).decode()
            
            if resp2 == "101":
                self.connected_client = True
            
            else:
                print("Error, impossible de se connecter")
        
        if respond == "103":
            self.send("002")
            self.logup(username=username, pwd=pwd)
        
        if respond == "105":
            msg = self.client.recv(2048).decode()
            print(msg)
    
    def logup(self, username, pwd):
        acc = {"username": username,
             "pwd": pwd}
        self.send(json.dumps(acc).encode())
        self.token = self.client.recv(2064)

if __name__ == "__main__":
    client = LoginClient("localhost", 8081)
    client.login("test", "test")
    print(client.connected_client, client.token)