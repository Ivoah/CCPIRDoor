#!/usr/bin/env python

# This program goes on the Raspberry Pi

from RPi.GPIO import *
from time import sleep
from BaseHTTPServer import BaseHTTPRequestHandler

setmode(BCM)

SIG = 17

setup(SIG, IN)

class PIRRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(input(SIG))

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('', 3141), PIRRequestHandler)
    print 'Serving on port 3141'
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    cleanup()
    print('\nBye!')
