# ERP
# 練習題2:
# 打開 01-tkinter-list.py  修改,
# 讀取  "消費紀錄.csv" 把裡面的資料, 顯示在 list

import tkinter as tk
import csv
win = tk.Tk()
win.wm_title("Hello")
win.minsize(width=600, height=400)
win.maxsize(width=600, height=400)
win.resizable(width=False, height=False)


Lb1 = tk.Listbox(win, width=120, height=20)
with open('消費紀錄1.csv', 'r') as fin:
    read = csv.reader(fin, delimiter=',')
    header = next(read)
    print(header)
    x=1
    for row in read:
        print("日期=", row[0], "時間=", row[1], "消費人=", row[2], "品項=", row[3], "總金額=", row[4])
        str=row[0]+"  "+row[1]+"  "+row[2]+"  "+row[3]+"  "+row[4]
        Lb1.insert(x, str)
        x=x+1
Lb1.place(x=0,y=160)

label1 =tk.Label(win,text="日期:",font=20)
label1.place(x=5, y=5)
entry1=tk.Entry(win)
entry1.place(x=80,y=5)

label2 =tk.Label(win,text="時間:",font=20)
label2.place(x=5, y=35)
entry2=tk.Entry(win)
entry2.place(x=80,y=35)

label3 =tk.Label(win,text="消費人:",font=20)
label3.place(x=5, y=65)
entry3=tk.Entry(win)
entry3.place(x=80,y=65)

label4 =tk.Label(win,text="品項:",font=20)
label4.place(x=5, y=95)
entry4=tk.Entry(win)
entry4.place(x=80,y=95)

label5 =tk.Label(win,text="總金額:",font=20)
label5.place(x=5, y=125)
entry5=tk.Entry(win)
entry5.place(x=80,y=125)



win.mainloop()
