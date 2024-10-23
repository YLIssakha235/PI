import re 
import math 
import sys
import json


def line(L, i):
    return L[i]
def column(L, j):
    size = len(L[0])
    return ''.join([L[i][j] for i in range(size)])

def checkregexcrossword(linesregex, columnregex, answer):
    for i, regex in enumerate(linesregex):
        pattern = re.compile(regex)
        if pattern.match(line(answer, i)) is None:
            return False
    for j, regex in enumerate(columnregex):
        pattern = re.compile(regex)
        if pattern.match(column(answer, j)) is None:
            return False    
    return True


print(checkregexcrossword(['(EC|CD)[ABS]','.[GROS]+', 'C?[KS]+']))


# # 7 points
# # Ecrivez une fonction nommée compose() qi prend un nombre variable
# # de fonctions en paramètres. elle renverra une fonction 
# # équivalente à la composition des fonctions reçues en paramètres.
# #
# #     compose(sin, cos, pow)(x, y) <=> sin(cos(pow(x, y)))

# # Votre code ici
# from math import sin, cos, pow
# def compose(sin, cos, pow):
#     def sin(a):
#         return 
    
#     def cos(b):
#         return
#     def pow(x,y):
#         return x**y
#     return pow


# if __name__ == '__main__':
#     from math import sin, cos, pow

#     fun = compose(sin, cos, pow)
#     if fun(0.42, 3) == sin(cos(pow(0.42, 3))):
#         print('OK')
#     else:
#         print('KO')


def compose(*args):
    if len(args) == 0:
        raise ValueError("At least one function must be provided for composition.")
    
    def inner_function(*args_inner):
        result = args[-1](*args_inner)
        for func in reversed(args[:-1]):
            result = func(result)
        return result
    
    return inner_function

if __name__ == '__main__':
    from math import sin, cos, pow

    fun = compose(sin, cos, pow)
    if fun(0.42, 3) == sin(cos(pow(0.42, 3))):
        print('OK')
    else:
        print('KO')

from math import sin, cos, pow

def compose(*funcs):
    def inner_function(x, y):
        result = x
        for func in reversed(funcs):
            result = func(result, y) if func == pow else func(result)
        return result
    
    return inner_function

if __name__ == '__main__':
    fun = compose(sin, cos, pow)
    x, y = 0.42, 3
    if fun(x, y) == sin(cos(pow(x, y))):
        print('OK')
    else:
        print('KO')



# 7 points
# Ecrivez un décorateur nommé "power" qui prend un nombre en paramètre.
# Ce décorateur renverra une fonction dont les valeurs de retour seront
# mises à la puissance du paramètre du décorateur.

# Votre code ici
import re
import math

def power(a):
    def decorateur(f):
        def wrapper(*args):
            return((f(*args))**a)
            
        return wrapper
    return (decorateur)
    
     



if __name__ == '__main__':
    @power(3)
    def twice(a):
        return 2*a

    print(twice(2)) # affiche 64.0 car (2*2)³ = 64



# 6 points
# Écrire une fonction nommée getPhones() qui prend une chaîne
# de caractères en paramètre et qui renvoie la liste de toutes les
# numéros de GSM trouvés dans la chaîne. Un numéro de GSM peut
# se présenter sous les formes suivantes:
# 0473/12.34.56, 0473 12 34 56, 0473/12 34 56, 0473 12.34.56 

# Exemple:
# print(getPhones("Je dois appeler le 0473/23.45.67 et puis le 0498 98 76 54"))
# affiche ['0473/23.45.67', '0498 98 76 54']

# Votre code ici
import re 
import math



def getPhones(n):
    pattern = r'\d{4}.\d{2}.\d{2}.\d{2}'
    num = r'\d{4}.\d{2}.\d{2}.\d{2}'
    m = re.compile(pattern, re.MULTILINE)
    if m is not None:
        return(m.findall(n))

    




if __name__ == '__main__':
    print(getPhones("Je dois appeler le 0473/23.45.67 et puis le 0498 98 76 54"))

import re

def getPhones(text):
    # Pattern pour les numéros de GSM
    pattern = r'\b0\d{3}[ /]?\d{2}[ ./]?\d{2}[ ./]?\d{2}\b'

    # Recherche de tous les numéros de GSM dans le texte
    phones = re.findall(pattern, text)
    
    return phones

if __name__ == '__main__':
    print(getPhones("Je dois appeler le 0473/23.45.67 et puis le 0498 98 76 54"))



# 7 points
# Ecrivez un décorateur nommé "power" qui prend un nombre en paramètre.
# Ce décorateur renverra une fonction dont les valeurs de retour seront
# mises à la puissance du paramètre du décorateur.

# Votre code ici
import re
import math

def power(a):
    def decorateur(f):
        def wrapper(*args, **kwargs):
            return((f(*args, **kwargs))**a)
            
        return wrapper
    return (decorateur)
    
     



if __name__ == '__main__':
    @power(3)
    def twice(a):
        return 2*a

    print(twice(2)) # affiche 64.0 car (2*2)³ = 64



def mult(factor):
    def decorator(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs) * factor
        return wrapper
    return decorator

if __name__ == '__main__':
    @mult(3)
    def add(a, b):
        return a + b

    print(add(1, 2))  # affiche 9 car (1 + 2) * 3 = 9
