#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-

from random import randrange
from math import ceil

def faitesVosJeux(pognon):
    maMise = None
    monPari = None
    while maMise == None:
        maMise = initMise(pognon)
    while monPari == None:
        monPari = initPari()
    print("Ok c'est parti,",maMise,"sur le", monPari,"!\n")
    rienNeVaPlus(maMise, monPari, pognon)


def initMise(pognon):
    mise = input("Combien souhaitez-vous miser ? -> ")
    try:
        mise = int(mise)
        if mise > 0:
            if mise <= pognon:
                print('\n')
                return mise
            else:
                print("t'es trop fauché pour ça !\n")
                return None
        else:
            print("Y'a un minimum, t'es au courant ?\n")
            return None
    except:
        print("Non ça ne va pas... il faut un nombre !\n")
        return None

def initPari():
    pari = input("Sur quoi on mise ? entre 0 et 49 -> ")
    try:
        pari = int(pari)
        if pari >= 0:
            if pari <= 49:
                return pari
            else:
                print("t'es du genre marseillais toi non ?\n")
                return None
        else:
            print("J'ai essayé te tourner la roulette dans l'autre sens, les nombres négatifs, ça marche pas\n")
            return None
        return pari
    except:
        print('Faut rentrer un nombre hein...\n')
        return None

def again(pognon):
    if pognon > 0:
        choix = input("On remet ça ? (Y/N) -> ")
        if choix == "Y" or choix == "y":
            return "y"
        elif choix == "N" or choix == "n":
            return "n"
        else:
            return None
    else:
        return "lost"


def rienNeVaPlus(mise, pari, pognon):
    pognon -= mise
    print("*bruit de roulette qui tourne*")
    if pari % 2 == 0:
        couleurJoueur = "rouge"
    else:
        couleurJoueur = "noir"
    roulette = randrange(50)
    if roulette % 2 == 0:
        couleurRoulette = "rouge"
    else:
        couleurRoulette = "noir"
    print("Résultat de la roulette:",roulette,"(couleur:",couleurRoulette,")")
    if mise == roulette:
        print("Hmmm la chance du débutant surement. Tiens voilà ton fric.\n")
        pognon += mise*3
        playAgain(pognon)
    elif couleurJoueur == couleurRoulette:
        print("Pas mal, tu l'as eu à la couleur.\n")
        pognon += ceil(mise/2)
        playAgain(pognon)
    else:
        print("Dommaaaaage, envoie le blé papi\n")
        playAgain(pognon)

def playAgain(pognon):
    print('Ton solde:',pognon)
    retry = None
    while retry == None:
        retry = again(pognon)
    if retry == "y":
        print("\n")
        faitesVosJeux(pognon)
    elif retry == "n":
        print("C'est toi le chef, chef. Tu as fini avec",pognon,"brouzoufs")
    else:
        print("J't'aurais bien proposé d'en refaire une, mais t'es trop pauvre. Reviens quand tu pèseras dans l'game !")

