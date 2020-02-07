#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, carte):
        self.robot = carte.robotPosition
        self.obstacles = carte.obstacles
        self.labyrinthe = carte.labyrinthe
        self.maxOffset = carte.maxOffset
        self.maxLines = carte.maxLines
        self.mapName = carte.name
        self.isGameWon = False

    def drawLabyrinthe(self):
        """ Redessine le labyrinthe """
        print("\n")
        for line in self.labyrinthe:
            print(line)
        print("\n")

    def giveRobotPosition(self):
        """ Retourne une liste contenant le numéro de ligne ou se trouve le joueur, et la position dans la ligne """
        i=0
        while i < self.maxLines:
            robotSearch = self.labyrinthe[i].find("X")
            if robotSearch != -1:
                robot = [i, int(robotSearch)]
                return robot
            i += 1

    def isPathClear(self, robot, checkMe):
        """ indique si le déplacement donné par le joueur est valide ou non """
        #----------------------------------------------------------------------------------------------------------------------------------
        if checkMe[0] == "z": #si on veut monter
            if self.labyrinthe[robot[0]-checkMe[1]][robot[1]] == " " or self.labyrinthe[robot[0]-checkMe[1]][robot[1]] == "U": #si la destination est dispo ou l'arrivée
                startLine = int(robot[0])
                while startLine >= startLine-checkMe[1] and startLine >= 0: #on vérifie qu'entre la destination et le départ tout est correct
                    if self.labyrinthe[startLine][robot[1]] == "0" or self.labyrinthe[startLine][robot[1]] == "O":
                        return False
                    startLine -=1
                return True
            else:
                return False
        #----------------------------------------------------------------------------------------------------------------------------------
        elif checkMe[0] == "s":#si on veut descendre
            if self.labyrinthe[robot[0]+checkMe[1]][robot[1]] == " " or self.labyrinthe[robot[0]+checkMe[1]][robot[1]] == "U":
                startLine = int(robot[0])
                while startLine <= startLine+checkMe[1] and startLine <= self.maxLines:
                    if self.labyrinthe[startLine][robot[1]] == "0" or self.labyrinthe[startLine][robot[1]] == "O": #or self.labyrinthe[startLine][robot[1]] == "."
                        return False
                    startLine +=1
                return True
            else: 
                return False
        #----------------------------------------------------------------------------------------------------------------------------------
        elif checkMe[0] == "q": #si on veut aller à gauche
            chunkToCheck = self.labyrinthe[robot[0]][robot[1]-checkMe[1]:robot[1]] #récupère le fragment de la str à analyser
            if self.labyrinthe[robot[0]][robot[1]-checkMe[1]] == " " or self.labyrinthe[robot[0]][robot[1]-checkMe[1]] == "U": #si la destination est libre
                if chunkToCheck.find("0") == -1 and chunkToCheck.find('O') == -1: #et si on à pas d'obstacle entre la destination et le départ
                    return True
                else: 
                    return False
            else:
                return False
        #----------------------------------------------------------------------------------------------------------------------------------
        elif checkMe[0] == "d": #si on veut aller à droite
            chunkToCheck = self.labyrinthe[robot[0]][robot[1]:robot[1]+checkMe[1]]
            if self.labyrinthe[robot[0]][robot[1]+checkMe[1]] == " " or self.labyrinthe[robot[0]][robot[1]+checkMe[1]] == "U":
                if chunkToCheck.find("0") == -1 and chunkToCheck.find('O') == -1:
                    return True
                else:
                    return False
            else:
                return False
        #----------------------------------------------------------------------------------------------------------------------------------
        else:
            return "{} n'est pas une commande valide".format(checkMe[0]) #en cas d'input non reconnu

    def isWon(self, robot, checkMe):
        """ indique si le robot arrive sur la sortie """
        #----------------------------------------------------------------------------------------------------------------------------------
        if checkMe[0] == "z": #si on veut monter
            if self.labyrinthe[robot[0]-checkMe[1]][robot[1]] == "U": #si la destination est dispo
                return True
            else:
                return False
        #----------------------------------------------------------------------------------------------------------------------------------
        elif checkMe[0] == "s":#si on veut descendre
            if self.labyrinthe[robot[0]+checkMe[1]][robot[1]] == "U":
                return True
            else:
                return False
        #----------------------------------------------------------------------------------------------------------------------------------
        elif checkMe[0] == "q": #si on veut aller à gauche
            if self.labyrinthe[robot[0]][robot[1]-checkMe[1]] == "U": #si la destination est libre
                return True
            else:
                return False
        #----------------------------------------------------------------------------------------------------------------------------------
        elif checkMe[0] == "d": #si on veut aller à droite
            if self.labyrinthe[robot[0]][robot[1]+checkMe[1]] == "U":
                return True
            else:
                return False
        #----------------------------------------------------------------------------------------------------------------------------------

    def updateMap(self, userInput):
        """ Met à jour le labyrinthe en enlevant la derniere position du robot, et en appliquant le déplacement spécifié par le joueur et affiche la carte."""
        inputLen = len(userInput)
        if inputLen >= 2: #si on a au moins 2 caractères, le premier caractere indique la direction, le(s) suivant(s) indique(nt) le pas.
            checkMe = [userInput[0], int(userInput[1:])]
        else: #si on a qu'un seul caractere, le pas sera de 1
            checkMe = [userInput, 1]
        robot = self.giveRobotPosition()#on recupere la position du robot
        if self.isPathClear(robot, checkMe):
            if self.isWon(robot, checkMe):
                self.isGameWon = True
            self.labyrinthe[robot[0]] = self.labyrinthe[robot[0]][:robot[1]]+" "+self.labyrinthe[robot[0]][int(robot[1])+1:] #on remplace la position de départ du robot par un espace.
            if checkMe[0] == "z": #on veut monter
                self.labyrinthe[robot[0]-checkMe[1]] = self.labyrinthe[robot[0]-checkMe[1]][:robot[1]]+"X"+self.labyrinthe[robot[0]-checkMe[1]][int(robot[1])+1:]
            if checkMe[0] == "s":#on veut descendre
                self.labyrinthe[robot[0]+checkMe[1]] = self.labyrinthe[robot[0]+checkMe[1]][:robot[1]]+"X"+self.labyrinthe[robot[0]+checkMe[1]][int(robot[1])+1:]
            if checkMe[0] == "q":#on veut aller à gauche
                self.labyrinthe[robot[0]] = self.labyrinthe[robot[0]][:int(robot[1])-int(checkMe[1])]+"X"+self.labyrinthe[robot[0]][int(robot[1])-(int(checkMe[1])-1):]
            if checkMe[0] == "d":#on veut aller à droite
                self.labyrinthe[robot[0]] = self.labyrinthe[robot[0]][:int(robot[1])+int(checkMe[1])]+"X"+self.labyrinthe[robot[0]][int(robot[1])+(int(checkMe[1])+1):]
            self.drawLabyrinthe()
        else:
            print('Impossible d\'effectuer le déplacement, merci de réésayer.')