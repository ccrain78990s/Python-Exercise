#!/usr/bin/python

import tkinter as tk
from tkinter import StringVar


win = tk.Tk()

win.wm_title("Hello, JING  ,輸入框5")
win.minsize(width=400, height=400)
win.maxsize(width=400, height=400)
win.resizable(width=False, height=False)

def event1():
    global entry1       # Entry 輸入框的變數
    global label1Str    # Label1 的文字 變數
    t1=entry1.get()     #取得用戶所輸入的文字
    print(t1)
    label1Str.set(t1)   #設定 Label1 的文字     <------

entry1=tk.Entry(win)
entry1.place(x=20,y=20)

btn1 =tk.Button(win,text="請輸入",command=event1)
btn1.place(x=20,y=50)

label1Str=StringVar()
label1=tk.Label(win,text="XXX",textvariable=label1Str)    #<-----
label1.place(x=20,y=60)


win.mainloop()


