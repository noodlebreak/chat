#!/usr/bin/env python

import socket
import select

BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

# Set socket timeout to 1 min
socket.setdefaulttimeout(60)

# Create server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind to host and port
s.bind(('127.0.0.1', 5007))
# Set socket to be non-blocking
s.setblocking(0)
# Queue max 5 connection requests
s.listen(5)

clientsockets = []

messages = []

def handle_read(s):
  msg = s.recv(BUFFER_SIZE)
  if len(msg) == 0:
    print "a client socket has closed"
    # socket has disconnected
    s.close()
    clientsockets.remove(s)
  else:
    print msg
    messages.append(msg)

def handle_write(s):
  pass

def handle_connect(s):
  cs = s.accept()
  print "New client"
  clientsockets.append(cs[0])
  print clientsockets

while 1:
  # Check sockets
  read, write, error = select.select([s]+clientsockets, clientsockets, [], 60)
  for sock in read:
    if sock is s:
      # New connection
      handle_connect(s)
    else:
      # New message
      handle_read(sock)
  # Write queued messages to client sockets
  for sock in write:
    for msg in messages:
      sock.send(msg)


s.close()