
# 2)  Écrivez un programme qui ouvre un fichier texte et qui retrouve tous les nombres qui y apparaissent.
#Le programme produit en sortie un inventaire de ces nombres, séparés par des virgules et avec le
#numéro de ligne où ils apparaissent. Voici un exemple d’exécution :
import re
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
