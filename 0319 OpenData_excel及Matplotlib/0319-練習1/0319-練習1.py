# 練習題1:
# 透過excel 設計一個 消費紀錄的csv
# 例如: 日期, 時間, 消費人, 品項, 總金額
# 並寫上2筆資料
import csv

with open('消費紀錄1.csv', 'w', newline='', encoding='utf-8') as fout:
        write = csv.writer(fout, delimiter=',')
        header=["日期","時間","消費人","品項","總金額"]
        write.writerow(header)
        write.writerow(['03/18','9:22;','王亡亡','日用品',999])
        write.writerow(['03/19','12:25','李里里','食物',888])
        write.writerow(['03/19','14:46','黃惶惶','飲料',777])
# 練習題2:
# 打開 01-tkinter-list.py 修改,
# 讀取"消費紀錄.csv"把裡面的資料 ,顯示在list