#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
from pathlib import Path
basePath = os.getcwd()
cartesPath = Path(basePath+"/cartes")
os.chdir(basePath)
from carte import Carte
from labyrinthe import Labyrinthe
import gameState


# On charge les cartes existantes
cartes = []
for nomFichier in os.listdir("cartes"):
    if nomFichier.endswith(".txt"):
        chemin = os.path.join(basePath+"/cartes/", nomFichier)
        nomCarte = nomFichier[:-4].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
        cartes.append(Carte(nomCarte, contenu))

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.name))

mapChoice = input('Veuillez saisir le numéro de la carte que vous souhaitez sélectionner: ')
mapChoice = int(mapChoice)-1
if mapChoice < len(cartes):
    labyrinthe = Labyrinthe(cartes[mapChoice])
    print(labyrinthe.obstacles)
    labyrinthe.drawLabyrinthe()
    while labyrinthe.isGameWon == False:
        playerMove = input('Indiquer la direction à suivre: ')
        labyrinthe.updateMap(playerMove)
    print("Bravo, le robot s'en est sorti")

