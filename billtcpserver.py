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
            myBuffer = ''
            # The first 10 bytes should contain info about how much other data is being
            # sent in the request, so we need to get at least 10 bytes before we
            # parse anything.
            while len(myBuffer) < 10:
                data = self.request.recv(BUFFSIZE)
                myBuffer += data
                if data != '':
                    print "Received: " + data

            # Determine how much data is being sent.
            requestSize = int(myBuffer[:10])
            myBuffer = myBuffer[10:]

            # Wait for the rest of the data
            while len(myBuffer) < requestSize:
                data = self.request.recv(BUFFSIZE)
                if data != '':
                    print "Received2: " + data
                myBuffer += data
            request = json.loads(myBuffer.strip())

            # Send the appropriate number of additional Bills.
            if 'numAdditionalBills' in request and isinstance(request['numAdditionalBills'], (int, long)):
                newBills = []

                # Currently we randomize the bills, but we should eventually populate this using
                # presorted lists of bills.
                for i in range(0, request['numAdditionalBills']):
                    newBill = bill.Bill(random.randint(0, 10000000), 1)
                    newBills.append(newBill.getDictionary())
                    jsonBills = json.dumps({'additionalBills' : newBills})
                print jsonBills

                # Add the length of the response (not including the first 10 bytes) in the
                # first 10 bytes.
                lenString = "%010d" % len(jsonBills)
                self.request.sendall(lenString + jsonBills)
        except Exception, e:
            print "Exception wile receiving message: ", e
