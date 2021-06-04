
# -*- coding: UTF-8 -*-
__author__ = "Chen"
# AIML
import sys

print(len(sys.argv))
if len(sys.argv)>1:
    print(sys.argv[1])
if len(sys.argv)>2:
    print(sys.argv[2])

import aiml
"""
kernel = aiml.Kernel()
kernel.learn("01-AIML-公司客服系統.xml")
while True:   # Press CTRL-C to break this loop
    t1=input("請輸入 >> ")
    contents=kernel.respond(t1)
    print(contents)
"""

import sys
import time

"""


# 點選 link ,  顯示該區域的ubike 資料
http://127.0.0.1:8888/?action=Ubike&sarea=龜山區
http://127.0.0.1:8888/?action=Ubike&sarea=中壢區
http://127.0.0.1:8888/?action=Ubike&sarea=桃園區


# HTML + Javascript + PHP/ASP + Python

"""
# HTTP

import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import urlparse,unquote
import subprocess

class MyHandler(RequestHandler):
    def do_GET(self):
        global kernel  ####
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        html = '我收到資料 '
        print(self.path)                   # /?name=powenko&passsword=abc
        query = urlparse(self.path).query  #  'name=powenko&passsword=abc'
        if query!="":
           dict2 = dict(qc.split("=") for qc in query.split("&"))
           try:
                aiml = dict2["aiml"].lower()
                print(aiml)
                if aiml!="":
                    #t1 = input("請輸入 >> ")
                    contents = kernel.respond(t1)
                    print(contents)
                if aiml=="公司電話":
                    # html ="顯示Ubike 所有資料"
                    print("1111")
                    html = subprocess.check_output(['python', '07HTTP_JSON-openData-Ubike.py'])
                    print("222")

                    self.wfile.write(html)
                    return
                if action=="ubike":
                    print(dict2["sarea"])
                    sarea = unquote(dict2["sarea"].lower())   # URL 的資料, 轉成utf-8文字
                    html = subprocess.check_output(['python', '07HTTP_JSON-openData-UbikeBysarea.py',sarea])
                    # python 07HTTP_JSON-openData-UbikeBysarea.py  龜山區
                    self.wfile.write(html)
                    return

           except:
                html=html+"沒有資料"
        html = html.encode("utf-8")
        self.wfile.write(html)



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
