import json


S = '{"ARG":74,"GRT":34,"AGT":6,"AFT":45,"RGY":555,"ERT":46}'
xfrgt = json.loads(S)
dicotrie = sorted(xfrgt.items(),
                  key = lambda t:t[1])
print(dicotrie) 
print(dicotrie[1])


def affichage(numero,nom,score):
    #prend en entr�e la position du joueur sur le classement et son nom et score et affiche avec methode de pyautogui un label a la bonne postion qui contient le infos
    print("numero",numero," a un score de ",score,"Bravo ", nom,"!")
def envoi(dicotrie):
    #appelle la methode affichage avec les num�ros allant de & jusque 5 et donne les doneees des 5 meilleurs joueurs 
    for i in range(5):
        affichage(i+1,dicotrie[len(dicotrie)-1-i][0],dicotrie[len(dicotrie)-1-i][1])
def save(scorefinal):
    #rejoute le score en parametre au dictionaire et ecrit le dictionaire dans json
    return 0



envoi(dicotrie)