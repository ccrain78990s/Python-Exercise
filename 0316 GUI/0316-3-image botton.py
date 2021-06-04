#!/usr/bin/python 
try:
  import Tkinter as tk 
except ImportError:
  import tkinter as tk 
from PIL import ImageTk, Image    #<---要有這個函示庫 才能用圖片

win = tk.Tk()

win.wm_title("Hello, JING  ,圖片按鈕")
win.minsize(width=600, height=600)
win.maxsize(width=600, height=600)
win.resizable(width=False, height=False)

def event1():
   print("btn1 pressed.")

def event2():
   print("Noah.")

img = ImageTk.PhotoImage(Image.open("python.png"))

btn1 =tk.Button(win,text="press me", image=img ,command=event1)
btn1.pack()

img2 = ImageTk.PhotoImage(Image.open("button.png"))

btn1 =tk.Button(win,text="press me", image=img2 ,command=event2)
btn1.place(x=250,y=250)

win.mainloop()


