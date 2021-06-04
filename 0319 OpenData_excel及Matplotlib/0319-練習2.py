# ERP
# 練習題3:
# 添加幾個 entry , 讓用戶可以直接在程式上 輸入 日期, 時間, 消費人, 品項, 總金額,

import tkinter as tk
import csv
win = tk.Tk()
win.wm_title("Hello")
win.minsize(width=600, height=600)
win.maxsize(width=600, height=600)
win.resizable(width=False, height=False)

Lb1 = tk.Listbox(win)

with open('消費紀錄1.csv', 'r') as fin:
    read = csv.reader(fin, delimiter=',')
    header = next(read)
    print(header)
    x=1
    for row in read:
        print("日期=", row[0], "時間=", row[1], "消費人=", row[2], "品項=", row[3], "總金額=", row[4])
        str=row[0]+row[1]+row[2]+row[3]+row[4]
        Lb1.insert(x, str)
        x=x+1



Lb1.pack()
win.mainloop()
