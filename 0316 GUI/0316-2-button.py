#!/usr/bin/python 
try:
  import Tkinter as tk 
except ImportError:
  import tkinter as tk

def event1():                   #<---按鈕要寫函數
   print("btn1 pressed.")

def event2():
    print("Noah")

win = tk.Tk()

win.wm_title("Hello, JING  ,按鈕")
win.minsize(width=600, height=600)
win.maxsize(width=600, height=600)
win.resizable(width=False, height=False)

btn1 =tk.Button(win,text="press me",command=event1)     # Button使用,command指令哪個函數
btn1.pack()

btn2 =tk.Button(win,text="按一下印出英文名稱",command=event2)
btn2.place(x=150,y=150)

win.mainloop()






