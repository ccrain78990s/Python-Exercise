#!/usr/bin/python
import tkinter as tk
from PIL import ImageTk, Image    #<---要有這個函示庫 才能用圖片



win = tk.Tk()

win.wm_title("Hello, JING  ,輸入框3")
win.minsize(width=600, height=600)
win.maxsize(width=600, height=600)
win.resizable(width=False, height=False)

def event1():
    global entry1    #<----寫這個比較好
    t1=entry1.get()  #取得用戶所輸入的文字
    print(t1)


entry1=tk.Entry(win)
entry1.place(x=130,y=120)

btn1 =tk.Button(win,text="輸入英文名稱印出",command=event1)
btn1.place(x=150,y=150)


win.mainloop()


