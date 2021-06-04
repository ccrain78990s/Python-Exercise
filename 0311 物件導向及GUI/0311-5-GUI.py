#!/usr/bin/python 
try:
  import Tkinter as tk  # Python 2.x name
except ImportError:
  import tkinter as tk  # Python 3.x name
win = tk.Tk()
win.wm_title("Hello, JING JING JING")      #設定視窗標題
win.minsize(width=777, height=888)         #視窗最小尺寸
win.maxsize(width=1024, height=1024)       #視窗最大尺寸
win.resizable(width=True, height=False)    #是否可調整視窗大小
win.mainloop()
