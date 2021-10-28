import sys
import time

class Token:
    
    def __init__(self, lim_token = 10):
        self.list_token = [self.create()]
        self.limite = lim_token
    
    def create(self):
        """TOKEN CREATE

        Returns:
            str: Renvoie un Token avec une methode de création
        """
        letters = []
        numbers = []

        for i in range(12):
            a = (i*round(int(time.time()), -1))%26
            letters.append(chr(65+a))
            

        for j in range(1, 21):
            b = (j*ord(letters[-(j%11)]))*(int(time.time()/10))%10
            numbers.append(b)


        token = ""

        while len(letters) != 0:
            token += letters.pop()
            token += str(numbers.pop())
            
        for i in numbers:
            token += str(i)
        return token
    
    def add_token(self):
        self.list_token.append(self.create())
        if len(self.list_token) >= self.limite:
            del self.list_token[0]
        
        return self
    
    def token(self):
        return self.list_token[-1]
    
    def print(self):
        print(self.list_token[-1])
        
class TokenTime(Token):
    def __init__(self, taille=10, time_out = 10):
        self.list_token = [self.create()[:taille]]
        self.time = [int(time.time())]
        self.size = taille
        self.time_out = time_out
    
    def create(self):
        """TOKEN CREATE
        size max = 34
        Returns:
            str: Renvoie un Token avec une methode de création
        """
        letters = []
        numbers = []

        for i in range(1,13):
            a = (i*round(int(time.time()*(10**(1//i))))) % 26
            letters.append(chr(65+a))

        for j in range(1, 21):
            b = (j*ord(letters[-(j % 11)]))*(int(time.time()*100)) % 10
            if b in numbers:
                d = str(int(time.time()))
                for i in d:
                    b += int(i)
            numbers.append(b)

        token = ""

        while len(letters) != 0:
            token += letters.pop()
            token += str(numbers.pop())

        for i in numbers:
            token += str(i)
        return token
    
    def getToken(self):
        if int(time.time()) - self.time[-1] >= self.time_out:
            self.time.append(int(time.time()))
            self.list_token.append(self.create()[:self.size])
        
        return self.list_token[-1]

if __name__ == "__main__":
    test = None
    test: TokenTime
    if len(sys.argv) > 1:
        test = TokenTime(taille=int(sys.argv[1]), time_out=int(sys.argv[2]))
    else:
        test = TokenTime()
    a = ""
    while a != "stop":
        
        print(test.getToken())
        a = input()
    
