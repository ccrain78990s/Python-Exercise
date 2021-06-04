#0316  貨幣轉美金 GUI使用  entry 美化 >>>>>0317 messagebox

import tkinter as tk
from tkinter import StringVar
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import  messagebox




#



win = tk.Tk()

messagebox.showinfo("Basic Example", "歡迎來到此程式")

def event1():
    global entry1
    global label3Str
    t1=entry1.get()
    print(t1)
    comStr=comboExample.get()
    if comStr=="台幣":
        dollar=float(t1)/28.8
    elif  comStr=="日幣":
        dollar=float(t1)/0.0092
    elif  comStr=="韓元":
        dollar=float(t1)/0.00088
    label3Str.set(str(dollar))   #匯率 美金 1 : 台幣 28.23
#視窗調整
win.wm_title("Hello, JING,金錢轉換")     #設定視窗標題
win.minsize(width=380, height=400)                      #視窗最小尺寸
win.maxsize(width=380, height=400)                      #視窗最大尺寸
win.resizable(width=False, height=False)                #是否可調整視窗大小

#背景
backgroundImg = ImageTk.PhotoImage(Image.open("backgroud.png"))
backgroundLabel =tk.Label(win,image=backgroundImg)
backgroundLabel.place(x=0,y=0)
#下拉式選單
labelTop = tk.Label(win,text = "↓↓↓ 請選擇 幣別 ↓↓↓")
labelTop.place(x=120, y=15)

comboExample = ttk.Combobox(win,            #ttk 要安裝函式庫
                            values=[
                                    "台幣",
                                    "韓元",
                                    "日幣"])
print(dict(comboExample))                   #<----dict?
comboExample.place(x=110, y=50)
comboExample.current(0)
print(comboExample.current(), comboExample.get())


label1 =tk.Label(win,bg="blue",text="請輸入金額:",fg="yellow",font=20)     #放上啥文字 顏色
label1.place(x=30, y=90)                                            #位置

entry1=tk.Entry(win)
entry1.place(x=140,y=90)

img = ImageTk.PhotoImage(Image.open("button2.png"))
btn1 =tk.Button(win,text="轉換",image=img,command=event1)
btn1.place(x=110,y=160)

label2 =tk.Label(win,bg="red",text="美金:",fg="yellow",font=20)
label2.place(x=80, y=290)


label3Str=StringVar()
label3=tk.Label(win,text="...",textvariable=label3Str)
label3.place(x=140,y=290)



win.mainloop()




