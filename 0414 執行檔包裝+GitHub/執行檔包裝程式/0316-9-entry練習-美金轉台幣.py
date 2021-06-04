#0316  台幣轉美金 GUI使用  entry 美化

import tkinter as tk
from tkinter import StringVar
from PIL import ImageTk, Image
#

"""
twd=100
usd=twd/38.8
"""

win = tk.Tk()

def event1():
    global entry1
    global label3Str
    t1=entry1.get()
    print(t1)
    label3Str.set(float(t1)/28.23)   #匯率 美金 1 : 台幣 28.23

win.wm_title("Hello, JING ,台幣轉美金小東西")     #設定視窗標題
win.minsize(width=380, height=400)                      #視窗最小尺寸
win.maxsize(width=380, height=400)                      #視窗最大尺寸
win.resizable(width=False, height=False)                #是否可調整視窗大小

backgroundImg = ImageTk.PhotoImage(Image.open("backgroud.png"))
backgroundLabel =tk.Label(win,image=backgroundImg)
backgroundLabel.place(x=0,y=0)

label1 =tk.Label(win,bg="blue",text="台幣:",fg="yellow",font=20)     #放上啥文字 顏色
label1.place(x=80, y=40)                                            #位置

entry1=tk.Entry(win)
entry1.place(x=140,y=40)

img = ImageTk.PhotoImage(Image.open("button2.png"))
btn1 =tk.Button(win,text="轉換",image=img,command=event1)
btn1.place(x=110,y=120)

label2 =tk.Label(win,bg="red",text="美金:",fg="yellow",font=20)
label2.place(x=80, y=240)


label3Str=StringVar()
label3=tk.Label(win,text="...",textvariable=label3Str)
label3.place(x=140,y=240)



win.mainloop()


# 1. 畫面處理

