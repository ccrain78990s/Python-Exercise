#!/usr/bin/python
"""
pip install Pillow     <----要安裝
pip install --upgrade pip
"""

try:
  import Tkinter as tk    #python2.0
except ImportError:
  import tkinter as tk    #python3.0
from PIL import ImageTk, Image

#加圖 記得在本程式的同一個路徑之中放置一張png 的圖片，請取名為 python.png

win = tk.Tk()

win.wm_title("Hello, JING  ,練習放圖片")
win.minsize(width=600, height=600)
win.maxsize(width=600, height=600)
win.resizable(width=False, height=False)

img = ImageTk.PhotoImage(Image.open("pig.jpg"))

label1 =tk.Label(win, image = img)   # <----指定圖片
label1.place(x=300, y=300)           #place 位置有其他寫法  ex: pack


win.mainloop()


