#!/usr/bin/env python

import socket

class server():

  def __init__(self, key_data):
    self.adres = ('127.0.0.1', 6500)
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.key_data = key_data

  def start(self):
    self.sock.bind(self.adres)
    self.sock.listen(1)
    self.connection()

  def connection(self):
    conn, ca = self.sock.accept()
    data = conn.recv(1024)
    data = data.split('{')
    if data[0].count('get') == 1:
      key = data[1].split('}')
      if self.key_data.count(key[0].strip()) > 0:
        message = "key_out - { %s : yes }" % key[0].strip()
      else:
        message = 'error'
    elif data[0].count('set') == 1:
      password = data[1].strip().split(':')
      if password[0].strip() == 'apud':
        if self.key_data.count(password) == 0:
          self.key_data.extend(password)
          message = 'dziala'#dodac odpowiedz do set
        else:
          message = 'error1'
      else:
        message = 'error2'
    else:
      message = 'error3'
    conn.sendall(message)
    conn.close()

key_data =['123']
while True:
  x = server(key_data)
  x.start()