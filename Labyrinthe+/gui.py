
#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.font as tkFont
import socket
import os
from pathlib import Path

class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, master, **kwargs):
        master.title('Labyrinthe +')
        self.bgColor="light grey"
        master.geometry('800x600')
        master.resizable(False, False)
        Frame.__init__(self, master, bg=self.bgColor,**kwargs)
        self.place(x=0, y=0, height=600, width=800)
        self.labFont = tkFont.Font(family="Courier New")

        self.message = Label(self, text="Bienvenue sur mon jeu du labyrinthe", fg="black",bg=self.bgColor )
        self.message.pack(side=TOP)

        self.displayFrame = Frame(self, bg="white",highlightbackground="black", highlightthickness=1, width=790)
        self.displayFrame.pack(side=TOP, fill=Y, expand=1)
        self.displayFrame.pack_propagate(0)

        self.labyrintheDisplay = Frame(self.displayFrame, width=540, height=576)
        self.labyrintheDisplay.pack(fill=X, side=LEFT, expand=1)
        self.labyrintheDisplay.pack_propagate(0)

        self.infoDisplay = Frame(self.displayFrame, width=250, height=576, bg="AntiqueWhite1")
        self.infoDisplay.pack(fill=X, side=RIGHT, expand=1)
        self.infoDisplay.pack_propagate(0)

        self.toolFrame = Frame(self, height=25, bg=self.bgColor)
        self.toolFrame.pack(side=BOTTOM, fill=X)

        userText = StringVar()
        userText.set('Entrez la prochaine action ici')
        self.userInput = Entry(self.toolFrame, textvariable=userText, width=80, highlightbackground=self.bgColor)
        self.userInput.pack(side="left")

        self.sendBtn = Button(self.toolFrame, text="Envoyer", highlightbackground=self.bgColor, bg="white", command=self.clearLabyrintheView)
        self.sendBtn.pack(side="left")

        self.padding1 = Label(self.labyrintheDisplay)
        self.padding1.pack()

        self.connect('localhost', 12345)
        print(self.__repr__())

#TODO : Deplacer la connexion dans un fichier à part (client.py ou dans une classe à part) et créer des getter setters pour les elements amenés à changer dans la fenetre. 
    def connect(self, host, port):
        connectionStatus = Label(self.infoDisplay, text="Connexion en cours...", bg="AntiqueWhite1")
        connectionStatus.pack()
        try:
            self.serverConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serverConnection.connect((host, port))
            update = {"msg" : "Connecté au serveur", "color": "green4"}
            self.connected = True
            self.serverConnection.send(b'Coucou')
        except:
            update = {"msg" : "Echec de connexion", "color": "red"}
            self.connected = False
        connectionStatus.configure(text=update["msg"], fg=update['color'])


    def menu(self):
        basePath = os.getcwd()
        cartesPath = Path(basePath+"/cartes")
        os.chdir(basePath)
        cartes = []
        for nomFichier in os.listdir("cartes"):
            if nomFichier.endswith(".txt"):
                chemin = os.path.join(basePath+"/cartes/", nomFichier)
                nomCarte = nomFichier[:-4].lower()
                with open(chemin, "r") as fichier:
                    contenu = fichier.read()
                cartes.append([nomCarte, contenu])
        i=0
        menuData = ["Voici les cartes disponibles: \n"]
        while i < len(cartes):
            menuData.append(str((i+1))+" - "+cartes[i][0]+"\n")
            i += 1
        menuStr = ""
        for part in menuData:
            menuStr += part
        menu = Label(self.labyrintheDisplay, text=menuStr)
        menu.pack(fill=X)

    def lab(self):
        basePath = os.getcwd()
        cartesPath = Path(basePath+"/cartes")
        os.chdir(basePath)
        print(cartesPath)
        cartes = []
        for nomFichier in os.listdir("cartes"):
            if nomFichier.endswith(".txt"):
                chemin = os.path.join(basePath+"/cartes/", nomFichier)
                nomCarte = nomFichier[:-4].lower()
                with open(chemin, "r") as fichier:
                    contenu = fichier.read()
                cartes.append([nomCarte, contenu])
        laby = Label(self.labyrintheDisplay, text=cartes[0][1], font=self.labFont, bg="black", fg="white")
        laby.pack()
        

    def clearLabyrintheView(self):
        self.labyrintheDisplay.destroy()
        self.labyrintheDisplay = Frame(self.displayFrame, width=490, height=576)
        self.labyrintheDisplay.pack(fill=X, side=LEFT, expand=1)
        self.labyrintheDisplay.pack_propagate(0)
        self.padding1 = Label(self.labyrintheDisplay)
        self.padding1.pack()

    def handleServerMessage(self, incMsg):
        if hasattr(self, "serverMsg"):
            print("j'ai")
            self.serverMsg.configure(text=incMsg.decode())
        else:
            print("j'ai pas")
            self.serverMsg = Label(self.infoDisplay, text=incMsg.decode())
            self.serverMsg.pack()

    def __repr__(self):
        return "<Interface client connexion:{}>".format(self.serverConnection)

fenetre = Tk()
interface = Interface(fenetre)
interface.mainloop()