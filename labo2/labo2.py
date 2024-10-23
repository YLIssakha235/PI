# Le but de ce labo consiste à vous familiariser avec les expressions régulières, outil puissant qui vous
#permet notamment de vérifier si des chaines de caractères satisfont des motifs ou non, mais aussi
#d’extraire des parties de chaines de caractères selon un motif donné.


# 2) exercice 1
#1. Écrivez un programme qui demande à l’utilisateur d’encoder une chaine de caractères et qui
#vérifie si cette dernière satisfait exactement le motif suivant :
# a)  Un numéro de téléphone de la forme +xx xxx xx xx xx où les x sont tous des chiffres.
import re
import math

#pattern = r'[0-9]{4}/[0-9]{2}\.[0-9]{2}\.[0-9]{2}'
pattern = r'\d{4}/\d{2}\.\d{2}\.\d{2}'
p = re.compile(pattern)

print(p.match('0465/89.50.43'))
print(p.match('0465/89.10.43'))
print(p.match('0465/89.50.45'))

# b) Un nombre entier, qui commence éventuellement avec un signe + ou − devant, et sans
#espaces aucun.

hen = r'[+-]?\d\d*'
p = re.compile(hen)
print(p.match('13'))
print(p.match("-16"))
print(p.match('+655'))


#c) Une plaque d’immatriculation qui peut prendre l’un des deux formes XLLLDDD ou XDDDLLL,
#où L est une lettre et D est un chiffre, et X est un chiffre optionnel (entre 1 et 9).

plaque = r'[1-9]?\d{3}[A-Z]{3}'
p = re.compile(plaque)

print(p.match('4777AMA'))
print(p.match('1677AMM'))

#  Le nom d’un volume sous windows qui est, pour rappel, de la forme C:\ (une lettre majuscule
#suivie de deux-points et backslash).
pattern = re.compile(r'[A-Z]:\\')
print(pattern.match('E:\\'))
print(pattern.match('C:\\'))




# 2)  Écrivez un programme qui ouvre un fichier texte et qui retrouve tous les nombres qui y apparaissent.
#Le programme produit en sortie un inventaire de ces nombres, séparés par des virgules et avec le
#numéro de ligne où ils apparaissent. Voici un exemple d’exécution :

import sys 

def process(filename):
    pattern = re.compile(r'[+-]?[1-9]\d*')
    with open(filename) as file:
        for i, line  in enumerate(file):
            L = pattern.findall(line)
            print('Line {}: {}'.format(i+1, ','.join(L)))

def main():
    if len(sys.argv) > 1:
        process(sys.argv[1])
    else:
        print('Usage: python labo.py <filename>')
if __name__ == '__main__':
    main()

#3. Écrivez un programme qui décomposer une URL en ses trois parties : le protocole, le nom de
#domaine de la machine et le chemin d’accès de la ressource. Faites deux versions de programme :
#la première n’utilise que les méthodes de la classe str et la seconde exploite les groupes capturants
#des expressions régulières. Voici un exemple d’exécution :

import re

def main():
    pattern = re.compile(r'(?P<protocol>[a-z]+)://(?P<domain>[^/]+)/(?P<path>.*)?')
    res = pattern.match('http://www.this.is/big/shit')
    print(res.group('protocol'))
    print(res.group('domain'))
    print(res.group('path'))

if __name__ == '__main__':
    main()


from  time import time
def timeit(f):
    def wrapper(*args, **kwargs):
        start = time()
        ret = f(*args, **kwargs)
        print('time: {}'.format(time() - start))
        return ret
    return wrapper()

@timeit
def sayhello():
    for  i in range(100000):
        print(i)
sayhello()

def checktypes(*types):
    def decorator(f):
        def wrapper(*args):
            for arg, type in zip(args, types):
                if not isinstance(arg,type):
                    raise TypeError('{} is not a {}'.format(arg,type))
            return f(*args)
        return wrapper
    return decorator

@checktypes(int,int)
def add(a,b):
    return a+b

print(add(4, 3))


from time import sleep
def delay(f):
    def decorateur(f):
        def wrapper(*args,**kwargs):
            sleep(1)
            return(f(*args,**kwargs))
        return wrapper
    return decorateur






@delay
def printnum(i):
    print(i)

cnt = 3
while cnt>0:
    printnum(cnt)
    cnt -=1
print('KA-BOOM')


from time import sleep
def delay(x):
    def decorateur(f):
        def wrapper(*args,**kwargs):
            sleep(x)
            return(f(*args,**kwargs))
        return wrapper
    return decorateur






@delay(5)
def printnum(i):
    print(i)

cnt = 3
while cnt>0:
    printnum(cnt)
    cnt -=1
print('KA-BOOM')

def binrep(n):
    while n>0:
        yield n%2
        n = n//2

  
b = binrep(12)
while True:
    try:
        print(next(b))
    except StopIteration:
        break

print(''.join(reversed([str(bit) for bit in binrep(12)])))


def call(f):
    f()

def hello():
    print('hello')


call(hello)


# def call(fun, *args, **kwargs):
#     return fun()

def call(fun, *args, **kwargs):
    return fun(*args, **kwargs)

def add(a,b):
    return a+b

print(call(add, 2, 9))


def call(fun, *args, **kwargs):
    return fun(*args, **kwargs)


def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def compute(a,b,op=add):
    return op(a,b)

print(call(compute, 2, 9))
print(call(compute, 2, 9, op=sub))