#!/usr/bin/env python
# encoding: utf-8

from socket import *
import thread

class BillTCPServer():
    
    def __init__(self, host, port, buffSize):
        self.host = host
        self.port = port
        self.buffSize = buffSize
    
    def start():
        address = (host, port)
        serversock = socket(AF_INET, SOCK_STREAM)
        serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        serversock.bind(address)
        serversock.listen(5)
        while 1:
            print 'waiting for connection...'
            clientsock, addr = serversock.accept()
            print '...connected from:', addr
            thread.start_new_thread(handler, (clientsock, addr))

    def gen_response():
        return 'this_is_the_return_from_the_server'

    def handler(clientsock,addr):
        while 1:
            data = clientsock.recv(buffSize)
            print 'data:' + repr(data)
            if not data: break
            clientsock.send(gen_response())
            print 'sent:' + repr(gen_response())
            clientsock.close()
        
        
