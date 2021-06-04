# ERP
# 練習題4:
# 添加一個按鈕, 把 entry 的資料存入 消費紀錄.csv

import tkinter as tk
import csv

win = tk.Tk()
win.wm_title("Hello")
win.minsize(width=600, height=400)
win.maxsize(width=600, height=400)
win.resizable(width=False, height=False)

def event1():
    global entry1
    global entry2
    global entry3
    global entry4
    global entry5
    t1=entry1.get()
    t2 = entry2.get()
    t3 = entry3.get()
    t4 = entry4.get()
    t5 = entry5.get()
    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)

    with open('消費紀錄1.csv', 'a', newline='', encoding='utf-8') as fout:  # a 新增在後面
        write = csv.writer(fout, delimiter=',')
        write.writerow(t1,t2,t3,t4,t5)



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

btn1 =tk.Button(win,text="新增資料",command=event1)
btn1.place(x=5,y=140)


win.mainloop()
