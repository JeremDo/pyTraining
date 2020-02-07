#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-

import socket
import threading

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour {} {}".format(self.ip, self.port, ))

    def run(self):
        print("Connexion de %s %s" % (self.ip, self.port, ))
        print(threadList)
        r = self.clientsocket.recv(2048)
        print(r.decode())
        self.clientsocket.send(b'info des labs ici')
        #print("Ouverture du fichier: ", r, "...")
        #fp = open(r, 'rb')
        #self.clientsocket.send(fp.read())
        #print("Client déconnecté...")

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",12345))
threadList = []
while True:
    tcpsock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    threadList.append(newthread)
    newthread.start()