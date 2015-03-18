#!/usr/bin/env python
# encoding: utf-8

import billtcpserver
import sys
import getopt


help_message = '''
A script for running the simple bill tcp server.
-o to specify where to send output
'''


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
        except getopt.error, msg:
            raise Usage(msg)

        # Option processing.
        for option, value in opts:
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("-o", "--output"):
                sys.stdout = open(value, 'w')

        # Start the server.
        server = billtcpserver.BillTCPServer('localhost', 8080)
        print 'Starting server, use <Ctrl-C> to stop'
        server.serve_forever()

    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2


if __name__ == "__main__":
    sys.exit(main())
