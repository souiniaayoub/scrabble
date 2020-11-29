import sys
import random
# Le plateau de jeu
def init_bonus():
    return [
        ['MT', '', '', 'LD', '', '', '', 'MT','', '', '', 'LD', '', '', 'MT'],
        ['', 'MD', '', '', '', 'LT', '', '','', 'LT', '', '', '', 'MD', ''],
        ['', '', 'MD', '', '', '', 'LD', '','LD', '', '', '', 'MD', '', ''],
        ['LD', '', '', 'MD', '', '', '', 'LD','', '', '', 'MD', '', '', 'LD'],
        ['', '', '', '', 'MD', '', '', '','', '', 'MD', '', '', '', ''],
        ['', 'LT', '', '', '', 'LT', '', '','', 'LT', '', '', '', 'LT', ''],
        ['', '', 'LD', '', '', '', 'LD', '','LD', '', '', '', 'LD', '', ''],
        ['MT', '', '', 'LD', '', '', '', 'MD','', '', '', 'LD', '', '', 'MT'],
        ['', '', 'LD', '', '', '', 'LD', '','LD', '', '', '', 'LD', '', ''],
        ['', 'LT', '', '', '', 'LT', '', '','', 'LT', '', '', '', 'LT', ''],
        ['', '', '', '', 'MD', '', '', '','', '', 'MD', '', '', '', ''],
        ['LD', '', '', 'MD', '', '', '', 'LD','', '', '', 'MD', '', '', 'LD'],
        ['', '', 'MD', '', '', '', 'LD', '','LD', '', '', '', 'MD', '', ''],
        ['', 'MD', '', '', '', 'LT', '', '','', 'LT', '', '', '', 'MD', ''],
        ['MT', '', '', 'LD', '', '', '', 'MT','', '', '', 'LD', '', '', 'MT'],
    ]
def init_jetons():
     return [
         ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '','', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '','', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '','', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '','', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '','', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '','', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '','', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '','', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '','', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '','', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '','', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '','', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '','', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '','', '', '', '', '', '', ''],
         ]
def bonus_logo(line,col):
    if  bonus[line][col] == '' or jeton[line][col] == '':
        return ''
    if  bonus[line][col] == 'LD':
        return '*'
    if  bonus[line][col] == 'LT':
        return '+'
    if  bonus[line][col] == 'MD':
        return '#'
    if  bonus[line][col] == 'MT':
        return '-'
def init_dico():
    return {
        "A":{"occ":9 ,"val":1},
        "B":{"occ":2 ,"val":3},
        "C":{"occ":2 ,"val":3},
        "D":{"occ":3 ,"val":2},
        "E":{"occ":15 ,"val":1},
        "F":{"occ":2 ,"val":4},
        "G":{"occ":2 ,"val":2},
        "H":{"occ":2 ,"val":4},
        "I":{"occ":8 ,"val":1},
        "J":{"occ":1 ,"val":8},
        "K":{"occ":1 ,"val":10},
        "L":{"occ":5 ,"val":1},
        "M":{"occ":3 ,"val":2},
        "N":{"occ":6 ,"val":1},
        "O":{"occ":6 ,"val":1},
        "P":{"occ":2 ,"val":3},
        "Q":{"occ":1 ,"val":8},
        "R":{"occ":6 ,"val":1},
        "S":{"occ":6 ,"val":1},
        "T":{"occ":6 ,"val":1},
        "U":{"occ":6 ,"val":1},
        "V":{"occ":2 ,"val":4},
        "W":{"occ":1 ,"val":10},
        "X":{"occ":1 ,"val":10},
        "Y":{"occ":1 ,"val":10},
        "Z":{"occ":1 ,"val":10},
        "?":{"occ":2 ,"val":0},
    }
def init_pioche(dico):
    pioche = []
    for lettre in dico:
        for _ in range(dico[lettre]['occ']):
            pioche.append(lettre)
    return pioche
def affiche_jetons(j):
    for ln , line in enumerate(j):
        for cl ,col in enumerate(line):
            sys.stdout.write(col+bonus_logo(ln,cl))
            sys.stdout.write('\t')
        if ln != 14:
            sys.stdout.write('\n\n\n')
# La pioche
def piocher(x, sac):
    jetons = []
    for i in range(x):
        rand = random.randint(0,len(sac))
        jetons.append(sac[rand])
        sac.pop(rand)
    return jetons
def completer_main(main,sac):
    if len(main) < 7 and len(sac) > 0:
        main.extend(piocher(7 - len(main),sac))
def echanger(jetons, main, sac):
    if len(sac) < len(jeton):
        return bool(False)
    if all(item in main for item in jetons) is False :
        return bool(False)
    for  lettre_jetons in jetons:
        for idxx , lettre_main in enumerate(main):
            if lettre_main == lettre_jetons:
                main.pop(idxx)
                break
    main.extend(piocher(len(jetons),sac))
    sac.extend(jetons)
    return bool(True)
# Construction de mots
def generer_dico(nf):
    f = open(nf,'r')
    mots = []
    for mot in f:
        mots.append(mot.replace('\n',''))
    f.close()
    return mots
def mot_jouable(mot, ll):
    if len(mot) > len(ll):
        return False
    mot_lettres_list = [char for char in mot.upper()]
    return ll.count('?') >= [item in ll for item in mot_lettres_list].count(False)
def mots_jouables(motsfr, ll):
    mots = []
    for m in motsfr:
        if mot_jouable(m,ll) is True:
            mots.append(m)
    return mots
# Valeur d'un mot
def valeur_mot(mot, dico):
    mot = mot.upper()
    value = 0
    if len(mot) == 7:
        value = 50
    for lettre in mot:
        value += dico[lettre]['val']
    return value
def meilleur_mot(motsfr, ll, dico):
    motsfr = mots_jouables(motsfr,ll)
    if len(motsfr) == 0:
        return ''
    values = [valeur_mot(mot,dico) for mot in motsfr]
    return motsfr[values.index(max(values))]
def meilleurs_mots(motsfr, ll, dico):
    motsfr = mots_jouables(motsfr,ll)
    if len(motsfr) == 0:
        return []
    values = [valeur_mot(mot,dico) for mot in motsfr]
    mx = max(values)
    return list(set([motsfr[idx] for idx in range(len(values)) if values[idx] == mx]))#the list set list cast is for distinct elements
# Placement de mot
def lire_coords():
    while True :
        while True:
            try:
                y = int(input('Enter the colomn between 0 and 14 : '))
                break
            except:
                pass
        while True:
            try:
                x = int(input('Enter the row between 0 and 14 : '))
                break
            except:
                pass      
        if (x > 0) and (x < 15) and (y > 0) and (y < 15) and jeton[x][y] == '':
            break
    return (x,y)
def tester_placement(plateau,i,j,dir,mot):
    return 0



#tests    
jeton = init_jetons()
bonus = init_bonus()
dico = init_dico()
sac = init_pioche(dico)
main = ['T','S','G','L','?','?']
# affiche_jetons(bonus)
# affiche_jetons(jeton)# print(sac)
# print(piocher(7,sac))
# print(sac)
# print(echanger(['T','L'],main,sac))
# print(main)
# print(sac)
# print(generer_dico("mots.txt"))
# print(mot_jouable('TKMF',main))
# print(mots_jouables(['TS','TG','TL','TM'],main))
# print( valeur_mot('BEBE',dico))
# print(meilleur_mot(['TS','T','TL','TS'],main,dico))
# print(meilleurs_mots(['TS','T','TL','TS'],main,dico))
print(lire_coords())