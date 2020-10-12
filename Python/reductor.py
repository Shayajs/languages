# Ce code nul sert juste à réduire les nombres vu à l'écran
# Exemple : 1 233 131 242 = 1,23 Md

# EXCEPTION QUAND LEVÉ POUR NOMBRES EN DESSOUS DE 0

# -*- Coding : utf-8 -*-
class UnderZeroException(Exception):
    '''\n\n~~~~~~~\nLe nombre que vous avez choisi n'est pas supérieur ou égale à Zéro\n~~~~~~~\n'''

    def __str__(self):
        return UnderZeroException.__doc__

    def __init__(self):
        print(self.__str__())


# CLASSE PRINCIPALE
class Reductor():
    ''' \nCette class reçoit un nombre à réduire : Number\n
    number > 1 000 = k\n
    number > 1 000 000 = M\n
    number > 1 000 000 000 = Md(s)\n

    Number doit forçement être de type int, ou transformable en int
    Le nombre doit être suppérieur ou égale à 0.
    '''

    def __init__(self, number):

        # Check if we can change the type
        try:
            self.number_class = int(number)
        except ValueError:
            print("Vous devez ")
            raise
        except:
            print("Une erreur inconnue s'est infiltrée")
            raise

        # Number under 0
        if self.number_class < 0:
            raise UnderZeroException()

    def __str__(self):
        # Return the doc
        return Reductor.__doc__

    def reduction(self):

        # Main Reductor

        # -k
        if self.number_class >= 1000 and self.number_class < 1000000:
            self.num_to_return = round(self.number_class / 1000, 2)
            return "{}k".format(self.num_to_return)

        # -M
        elif self.number_class >= 1000000 and self.number_class < 1000000000:
            self.num_to_return = round(self.number_class / 1000000, 2)
            return "{}M".format(self.num_to_return)

        # -Mrd/ -Mrds
        elif self.number_class >= 1000000000:
            self.num_to_return = round(self.number_class / 1000000000, 2)
            if int(self.num_to_return) <= 1:
                self.prefix = "Mrd"
            else:
                self.prefix = "Mrds"
            return "{} {}".format(self.num_to_return, self.prefix)

        # If number is under 1 000
        else:
            return "{}".format(self.number_class)

    def get_number(self):
        """Send the native number"""
        return self.number_class

    def get_number_reducted(self):
        """Send the reducted number"""
        return self.reduction()

    def set_number(self, new_number):
        """Change native number"""
        try:
            if new_number >= 0:
                self.number_class = int(new_number)
            else:
                raise UnderZeroException()
        except:
            print("Choisissez un nombre valide !")


# Start when
if __name__ == "__main__":
    try:
        b = Reductor(int(input("Choisissez un nombre positif : ")))
    except UnderZeroException as e:
        print(e)
    except:
        print("Une erreur inconnue a levé une exception")
