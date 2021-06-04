# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"

import sys
import time

import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import urlparse,unquote
import subprocess
import aiml



class MyHandler(RequestHandler):
    def MyHeader(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

    def do_GET(self):
        global kernel
        html = '我收到資料 '
        print(self.path)                   # /?name=powenko&passsword=abc
        query = urlparse(self.path).query  #  'name=powenko&passsword=abc'
        if query!="":
           dict2 = dict(qc.split("=") for qc in query.split("&"))
           try:
                aiml=""
                action=""
                if "aiml" in dict2:
                    aiml = dict2["aiml"].lower()      #<--
                    print(aiml)
                if "action" in dict2:
                    action = dict2["action"].lower()  #<---
                    print(action)
                if action=="ubikeall":
                    # html ="顯示Ubike 所有資料"
                    print("1111")
                    html = subprocess.check_output(['python', '07HTTP_JSON-openData-Ubike.py'])
                    print("222")
                    self.MyHeader()
                    self.wfile.write(html)
                    return
                if action=="ubike":
                    print(dict2["sarea"])
                    sarea = unquote(dict2["sarea"].lower())   # URL 的資料, 轉成utf-8文字
                    html = subprocess.check_output(['python', '07HTTP_JSON-openData-UbikeBysarea.py',sarea])
                    # python 07HTTP_JSON-openData-UbikeBysarea.py  龜山區
                    self.MyHeader()
                    self.wfile.write(html)
                    return

           except:
                html=html+"沒有資料"
        #html = html.encode("utf-8")
        #self.wfile.write(html)
        super().do_GET()



kernel = aiml.Kernel()
kernel.learn("01-AIML-公司客服系統.xml")
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



