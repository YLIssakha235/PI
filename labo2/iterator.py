""" L =[1, 2, 3]
iterator = iter(L)
# print(next(iterator))

try:
    while True:
        i = next(iterator)
        print(i)
except StopIteration:
    pass """


# deux fonctions pour utiliser l'itineration 
#la premiere __getiitem__

import re

RE_WORDS = re. compile ('\w+')

class Sentence :
    def __init__ (self , text ):
        self . __text = text
        self . __words = RE_WORDS . findall ( text )

    def __getitem__ (self , i):
        return self . __words [i]
    def __len__ ( self ):
        return len ( self . __words )

s = Sentence('hello ca va')

print(s[1])
print(len(s))
for word in s:
    print(word)

""" print(list(lambda w: w[1], s)) """


""" class square:
    def __getitem__(self,i):
        return i*i
for n in square():
    print(n) """
