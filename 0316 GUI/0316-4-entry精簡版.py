#!/usr/bin/python
import tkinter as tk
from PIL import ImageTk, Image    #<---要有這個函示庫 才能用圖片

win = tk.Tk()

win.wm_title("Hello, JING  ,輸入框1")
win.minsize(width=600, height=600)
win.maxsize(width=600, height=600)
win.resizable(width=False, height=False)


entry1=tk.Entry(win)
entry1.place(x=0,y=0)


win.mainloop()


