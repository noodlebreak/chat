#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5007
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while 1:
  msg = raw_input()
  s.send(msg)

s.close()