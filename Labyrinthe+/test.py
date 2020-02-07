#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-

from tkinter import *

class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, bg="green", **kwargs)
        self.place(x=0, y=0, width=800, height=600)
        
        # Création de nos widgets
        self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
        self.message.pack(side=TOP)
        
        self.displayFrame = Frame(self, bg="blue")
        self.displayFrame.place(y=25, width=800, height=550)

        self.bouton_quitter = Button(self.displayFrame, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")
        
        self.toolFrame = Frame(self)
        self.toolFrame.pack(side="bottom", fill=X)

        userText = StringVar()
        userText.set('Entrez la prochaine action ici')
        self.userInput = Entry(self.toolFrame, textvariable=userText, width=75)
        self.userInput.pack(side="left")

        self.bouton_cliquer = Button(self.toolFrame, text="Cliquez ici", fg="red",
                command=self.cliquer)
        self.bouton_cliquer.pack(side="right")
    
    def cliquer(self):
        """Il y a eu un clic sur le bouton.
        
        On change la valeur du label message."""
        
        self.nb_clic += 1
        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)

fenetre = Tk()
fenetre.title('Labyrinthe +')
fenetre.geometry('800x600')
fenetre.resizable(False, False)
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()