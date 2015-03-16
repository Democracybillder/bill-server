#!/usr/bin/env python
# encoding: utf-8

import socket
import json

sendData = {'numAdditionalBills' : 12}

# This is so long because we want to test that requests larger
# than a single buffer can make it through.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8080))
toSend = json.dumps(sendData)
lenString = "%010d" % len(toSend)
s.send(lenString + toSend)
myBuffer = ''
data = True
while data:
    data = s.recv(1024)
    myBuffer += data
print myBuffer
result = json.loads(myBuffer)
print result
s.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8080))
sendData['oldBills'] = result
toSend = json.dumps(sendData)
lenString = "%010d" % len(toSend)
s.send(lenString + toSend)
myBuffer = ''
data = True
while data:
    data = s.recv(1024)
    myBuffer += data
print myBuffer
result = json.loads(myBuffer)
print result