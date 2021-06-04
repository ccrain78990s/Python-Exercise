"""
===第一題===
在Python中執行"dir c:\" 的指令
"""
import os
os.system("dir c:\\")
os.system("dir c:/")
"""
===第二題===
# 透過 argv[1]  argv[2] 取得輸入的資料
#  例如: python  xxx.py aaa  bbb
取得並印出 aaa  bbb
## python main.py aaaa bbb
"""
import sys

print(len(sys.argv))
if len(sys.argv)>1:
    print(sys.argv[1])
if len(sys.argv)>2:
    print(sys.argv[2])
"""
===第三題===
透過 AIML 請設計一個 簡單的公司服務簡介系統
可以回答以下問題
公司地址
公司電話
公司網址
服務時間
服務項目
"""
import aiml
kernel = aiml.Kernel()
kernel.learn("01-AIML-公司客服系統.xml")
while True:   # Press CTRL-C to break this loop
    t1=input("請輸入 >> ")
    contents=kernel.respond(t1)
    print(contents)
"""
===第四題===
接個上一題目 AIML
記住客戶資料, 並在離開時 說出 客戶姓名
請輸入 >> 我是 柯博文
你好柯博文
請輸入 >> 再見
再見柯博文
"""
