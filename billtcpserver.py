#!/usr/bin/env python
# encoding: utf-8

import SocketServer
import json
import bill
import random

BUFFSIZE = 1024;

class BillTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True

    def __init__(self, host, port):
        SocketServer.ThreadingTCPServer.__init__(self, (host, port), BillTCPServerHandler)

class BillTCPServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            requestSize = 10
            myBuffer = ''
            while len(myBuffer) < requestSize:
                data = self.request.recv(BUFFSIZE)
                print data
                if (myBuffer == ''):
                    # the first 10 bytes should contain info about how much data is being sent in the request
                    requestSize = int(data[:10])
                    myBuffer += data[10:]
                else:
                    myBuffer += data
            print myBuffer
            data = json.loads(myBuffer.strip())
            # send some 'ok' back
            if 'numAdditionalBills' in data and isinstance(data['numAdditionalBills'], (int, long)):
                newBills = []
                for i in range(0, data['numAdditionalBills']):
                    newBill = bill.Bill(random.randint(0, 10000000), 1)
                    newBills.append(newBill.getDictionary())
                    jsonBills = json.dumps({'additionalBills' : newBills})
                print jsonBills
                self.request.sendall(jsonBills)
        except Exception, e:
            print "Exception wile receiving message: ", e
        
        
