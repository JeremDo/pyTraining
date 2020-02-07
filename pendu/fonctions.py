#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-

import config
import os
import pickle
from random import randrange
from math import fabs

os.chdir('/Applications/XAMPP/xamppfiles/htdocs/pyTraining/pendu/')

#Definit la config du jeu (choisi un mot dans la liste, créé son equivalent avec des ***), stock le nom et le nombre d'essais
def initGame(name):
    indexAlea = randrange(20)
    motChoisi = config.mots[indexAlea]
    i = 0
    motCache = ""
    while i < len(motChoisi):
        motCache = motCache + "*"
        i+=1
    gameConf = {
        "player": name,
        "motChoisi": motChoisi,
        "motCache": motCache,
        "essais": config.essais,
        "win": False
    }
    return gameConf

#Le Principal process d'une partie, représente le déroulement d'une "manche" ou le joueur donne une lettre et le jeu lui dit si c'est dans le mot ou non.
def mainProcess(gameState):
    lettre = input('Quelle lettre souhaitez vous proposer ?')
    if len(lettre) > 1 or len(lettre) == 0:
        print('Merci de rentrer une seule lettre.')
        return None
    else:
        if type(lettre) is not str: #modifier par une vérif de regex ulta simple genre [a-z][A-Z] ou un truc dans le genre
            print("Merci de rentrer uniquement une lettre")
            return None
        else:
            occurences = findOccurences(gameState["motChoisi"], lettre)
            if occurences == None:
                print("Dommage, la lettre que vous avez choisie n'est pas dans le mot. {} \n".format(gameState['motCache']))
                gameState['essais'] -= 1
                return None
            else:
                gameState["motCache"] = revealLetter(gameState["motCache"], lettre, occurences)
                gameState["win"] = testWin(gameState["motCache"])
                if gameState["win"] == True:
                    return None
                else:
                    gameState['essais'] -= 1
                    print("Bravo, la lettre {} est bien dans le mot. {} essai(s) restants. {} \n".format(lettre, gameState["essais"], gameState['motCache']))

#retourne le nombre de fois et la positions de la lettre entrée par l'utilisateur 
def findOccurences(mot, lettre):
    i = 0
    indexes = []
    while i < len(mot):
        if mot[i] == lettre:
            indexes.append(i)
        i += 1
    if len(indexes) > 0:
        return indexes
    else:
        return None

#permet d'afficher les lettres au bon endroit sur le mot caché
def revealLetter(motCache, lettre, indexes):
    for ind in indexes:
        if ind == 0:
            motCache = lettre + motCache[1:]
        elif ind == 1:
            motCache = motCache[0]+lettre+motCache[2:]
        else:
            motCache = motCache[:ind]+lettre+motCache[(ind+1):]
    return motCache

#permet de vérifier si le mot a été decouvert. Grosso modo si le mot caché ne contient plus d'*, c'est gagné
def testWin(motCache):
    if motCache.find("*") == -1:
        return True
    else:
        return False

#Process principal permettant d'initialiser le jeu et de lancer les manches
def playHangman(name):
    gameState = initGame(name)
    print(gameState)
    while gameState["win"] == False:
        if gameState["essais"] > 0:
            mainProcess(gameState)
        else:
            print("lost")
            break
    if gameState['win'] == True:
        print("Bravo, vous avez trouvé en {} coups! Le mot était bien {}.".format(8-(gameState['essais']-1), gameState["motChoisi"]))
        playAgain()
    else:
        print("Dommage, vous n'avez pas réussi à trouver. Il s'agissait du mot \"{}\".".format(gameState["motChoisi"]))
        playAgain()

#gestion de la question pour recommencer une partie
def again():
    choix = input("Souhaitez vous refaire une partie ? (y/n) ")
    if choix == "Y" or choix == "y":
        return "y"
    elif choix == "N" or choix == "n":
        return "n"
    else:
        return None

#permet de boucler sur la question pour recommencer, comme ça si le joueur tape autre chose que y ou n la question lui est reposée
def playAgain():
    choix = None
    while choix == None:
        choix = again()
    if choix == "y":
        playHangman()
    else:
        print("Merci d'avoir joué !")

#sauvegarde du score du joueur
def saveScore(player, score):
    scores = '/Applications/XAMPP/xamppfiles/htdocs/pyTraining/pendu/scores'
    if os.path.exists(scores):
        with open('scores', 'rb') as scoreFile:
            scoreData = pickle.load(scoreFile)
        if player in scoreData.keys():
            scoreData[player] += score
        else:
            scoreData[player] = score
        with open('scores', 'wb') as scoreFile:
            myPickle = pickle.Pickler(scoreFile)
            myPickle.dump(scoreData)
    else:
        data = {
            player: score
        }
        with open('scores', 'wb') as scoreFile:
            myPickle = pickle.Pickler(scoreFile)
            myPickle.dump(data)
    with open('scores', "rb") as scoresList:
        scoreData = pickle.load(scoresList)
        print(scoreData)