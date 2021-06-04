#0311 下午 台幣轉美金 GUI使用
import tkinter as tk
#

twd=100
usd=twd/38.8

#
win = tk.Tk()

win.wm_title("Hello, JING ,台幣轉美金小東西")     #設定視窗標題
win.minsize(width=275, height=400)                      #視窗最小尺寸
win.maxsize(width=275, height=400)                      #視窗最大尺寸
win.resizable(width=False, height=False)                #是否可調整視窗大小

label1 =tk.Label(win,bg="blue",text="台幣:"+str(twd),fg="yellow",font=20)     #放上啥文字 顏色
label1.place(x=120, y=40)                                   #要放在哪裡?從左上角開始計算

label2 =tk.Label(win,bg="black",text="轉換後",fg="yellow",font=10)
label2.place(x=115, y=140)

label3 =tk.Label(win,bg="red",text="美金:"+str(usd),fg="yellow",font=20)
label3.place(x=120, y=240)

win.mainloop()


# 1. 畫面處理

