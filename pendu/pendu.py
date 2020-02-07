#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-

import fonctions

print("Bienvenue au jeu du pendu. Je vais choisir un mot et vous devrez le deviner, vous avez 8 essais pour le découvrir.")
player = input("Tout d'abord, quel est votre nom ? ")
fonctions.playHangman(player)
