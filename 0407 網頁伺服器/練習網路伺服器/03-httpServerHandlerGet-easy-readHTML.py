# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"

import sys
import time

"""
http://127.0.0.1:8888/?name=powenko&password=abc
"""
import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import urlparse

class MyHandler(RequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        file=open("03-html.html",'r',encoding='utf-8')
        html =file.read()
        file.close()


        html = html.encode("utf-8")
        self.wfile.write(html)


port = 8888

print('Server listening on port %s' % port)
socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', port), MyHandler)
try:
    httpd.serve_forever()
except:
    print("Closing the server.")
    httpd.server_close()
    raise
