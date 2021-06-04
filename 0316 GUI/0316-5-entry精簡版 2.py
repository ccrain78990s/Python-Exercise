#!/usr/bin/python
import tkinter as tk
from PIL import ImageTk, Image    #<---要有這個函示庫 才能用圖片



win = tk.Tk()

win.wm_title("Hello, JING  ,輸入框2")
win.minsize(width=600, height=600)
win.maxsize(width=600, height=600)
win.resizable(width=False, height=False)

def event1():
    print("Noah")

entry1=tk.Entry(win)
entry1.place(x=0,y=0)

btn1 =tk.Button(win,text="按一下印出英文名稱",command=event1)
btn1.place(x=150,y=150)


win.mainloop()


