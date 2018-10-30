#!/usr/bin/env python

import socket
con_adres = ('0.0.0.0', 6500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(con_adres)
sock.listen(1)
conn, ca = sock.accept()
data = conn.recv(1024)
conn.send("DUPA")
conn.close()
