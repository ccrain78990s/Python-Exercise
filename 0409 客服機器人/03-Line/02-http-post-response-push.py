from sys import version as python_version
from cgi import parse_header, parse_multipart
import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import parse_qs
import json
import requests
# pip install requests
# ngrok http 8000


auth_token='jk36TjswuZE3G0v9aVlsVq1drMzDYlo9p77//1gK/64QjgvnlLMhBpitXiCTen8eKhTaGMef8egr2dUkdnXbUCPt1gpb0cl7eCLeSljRcCSBWf4yyqOn3lmvdml0/93zX7whfqOdL8oDMLUifvSo9AdB04t89/1O/w1cDnyilFU='

class MyHandler(RequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header('Authorization', 'Bearer ' + auth_token)
        self.end_headers()

    def do_POST(self):
        # Your user ID (Basic settings)
        # U936a8a4a4f642ad8172501d59d8d766c
        userId="U936a8a4a4f642ad8172501d59d8d766c"
        varLen = int(self.headers['Content-Length'])
        if varLen > 0:
            post_data = self.rfile.read(varLen)
            data = json.loads(post_data)
            print(data)
            userId=data['events'][0]['source']['userId']

        self.do_HEAD()
        # print(self.wfile)
        message = {
            "to": str(userId),
            "messages": [
                {
                    "type": "text",
                    "text": "安安，你好"
                },
                {
                    "type": "text",
                    "text": "嘿嘿"
                }
            ]
        }
        # self.wfile.write(bytes(json.dumps(message), 'utf-8'))

        hed = {'Authorization': 'Bearer ' + auth_token}
        url = 'https://api.line.me/v2/bot/message/push'
        response = requests.post(url, json=message, headers=hed)
        print(response)
        print(response.json())


socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', 8000), MyHandler)
httpd.serve_forever()
