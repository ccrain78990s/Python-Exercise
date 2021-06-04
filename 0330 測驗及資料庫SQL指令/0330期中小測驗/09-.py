# 第九題: 使用tkinter, 設計一個 計算消費稅後的總價的視窗程式,
#        使用1個 entry, 1 個button, 1 個 label,
#        當按下按鈕時, 把 輸入的數字, 加上消費稅後 (*1.05) , 顯示在label上
#        請參考: 台幣轉美金的程式

import tkinter as tk
from tkinter import StringVar
from PIL import ImageTk, Image

win = tk.Tk()

def event1():
    global entry1
    global label3Str
    t1=entry1.get()
    print(t1)
    label3Str.set(float(t1)*1.05)

win.wm_title("Hello,第9題")     #設定視窗標題
win.minsize(width=380, height=400)                      #視窗最小尺寸
win.maxsize(width=380, height=400)                      #視窗最大尺寸
win.resizable(width=False, height=False)                #是否可調整視窗大小


label1 =tk.Label(win,bg="blue",text="消費稅前:",fg="yellow",font=20)     #放上啥文字 顏色
label1.place(x=80, y=40)                                            #位置

entry1=tk.Entry(win)                    #輸入框
entry1.place(x=200,y=40)


btn1 =tk.Button(win,text="計算",command=event1)
btn1.place(x=110,y=120)

label2 =tk.Label(win,bg="red",text="消費稅後總價:",fg="yellow",font=20)
label2.place(x=30, y=240)


label3Str=StringVar()
label3=tk.Label(win,text="...",textvariable=label3Str)
label3.place(x=140,y=240)



win.mainloop()