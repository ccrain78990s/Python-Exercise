# main.py
# 資料來源:
#
# 記得建立一個  templates/post_submit.html 的檔案

"""
在dos 執行以下指令, 來執行
$ set FLASK_APP=main.py
$ flask run

在Mac /linux  執行以下指令, 來執行
$ export  FLASK_APP=main.py
$ flask run


Flask run 參數還可以加上以下指令
$ export FLASK_APP=main.py
$ flask run --reload --debugger --host 0.0.0.0 --port 80
"""
from flask import Flask, request
from flask import render_template
import sys
import time

import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import urlparse,unquote
import subprocess
import aiml


app = Flask(__name__)



# http://127.0.0.1:5000/restaurantall
@app.route("/restaurantall", methods=['GET'])
def ubikeall():
    html = subprocess.check_output(['python', '2-restaurant.py'])
    return html

# http://127.0.0.1:5000/restaurant?level=優
# http://127.0.0.1:5000/restaurant?level=良
@app.route("/restaurant", methods=['GET'])
def ubike():
    level = request.args.get('level')
    level=str(level)
    html = subprocess.check_output(['python', '3-level.py', level])
    return html

# http://127.0.0.1:5000/?name=xxxx
@app.route("/post_submit", methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        return 'Hello ' + request.form.get('username')

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('post_submit.html')   # 記得建立一個  templates/post_submit.html 的檔案

if __name__ == '__main__':
    app.debug = True
    app.run()
