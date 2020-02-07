#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-

import socket
import threading
import select
import time
host = ""
port = 12345

serverConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverConn.bind((host, port))
serverConn.listen(5)
print('Server launched on port {}'.format(port))

serverLaunched = True
connectedClients = []

while serverLaunched:
    incConns, outCons, xlist = select.select([serverConn],
        [], [], 0.05)
    for conns in incConns:
        clientConn, infosClient = conns.accept()
        time.sleep(5)
        clientConn.send(b'test')
        time.sleep(10)
        clientConn.send(b'test bitch')
        connectedClients.append(clientConn)
    clients2read = []
    try:
        clients2read, wlist, xlist = select.select(connectedClients, [], [], 0.05)
    except:
        pass
    else:
        for client in clients2read:
            msg = client.recv(1024)
            msg = msg.decode()
            print("Reçu {}".format(msg))
            client.send(b"5 / 5")
            if msg == "fin":
                serverLaunched = False
print('Fermeture des connexions')
for client in connectedClients:
    client.close()
serverConn.close()
        