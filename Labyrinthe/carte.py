#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-

"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.name = nom
        self.labyrinthe = self.formatLabyrinthe(chaine)
        self.maxOffset = len(self.labyrinthe[0])-1
        self.maxLines = len(self.labyrinthe)-1
        self.robotPosition = self.giveRobotPosition()
        self.obstacles = self.getObstacles()

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def formatLabyrinthe(self, chaine):
        """ Retourne une liste contenant le labyrinthe découpé par lignes """
        labyrinthe = chaine.split("\n")
        return labyrinthe


    def giveRobotPosition(self):
        """ Retourne une liste contenant le numéro de ligne ou se trouve le joueur, et la position dans la ligne """
        i=0
        while i < self.maxLines:
            robotSearch = self.labyrinthe[i].find("X")
            if robotSearch != -1:
                robot = [i, int(robotSearch)]
                return robot
            i += 1
    
    def getObstacles(self):
        i = 0
        obstaclesIndexes = []
        while i < self.maxLines:
            j = 0
            while j < self.maxOffset:
                if self.labyrinthe[i][j] == ".":
                    obstaclesIndexes.append([i, j])
                j += 1
            i += 1
        return obstaclesIndexes

