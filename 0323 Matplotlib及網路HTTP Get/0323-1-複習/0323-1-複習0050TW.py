import matplotlib.pyplot as plt
import csv
from datetime import datetime


date=[]
stockOpen=[]
stockHigh=[]
stockLow=[]
stockClose=[]

with open('0050.TW.csv', 'r') as fin:
    read = csv.reader(fin, delimiter=',')
    header = next(read) # 讀擋頭
    print(header)
    x=0
    for row in read:
        print(row)
        current_date = datetime.strptime(row[0], '%Y-%m-%d')  # 將日期資料轉換為datetime物件
        date.append(current_date)  # 儲存日期

        stockOpen.append(float(row[1]))

        stockHigh.append(float(row[2]))

        stockLow.append(float(row[3]))

        stockClose.append(float(row[4]))
        x=x+1

    plt.plot(date,stockOpen, 'b.')
    plt.title('Open')
    plt.show()
    plt.plot(date, stockLow, 'ro')
    plt.title('Low')
    plt.show()
    plt.plot(date, stockClose, 'ys')
    plt.title('Close')
    plt.show()
    plt.plot(date, stockHigh, 'g,')
    plt.title('High')
    plt.show()




# 1. 印出所有資料
# 2. 最大 最小 平均

print("Open最大",max(stockOpen))
print("Open最小",min(stockOpen))
avg_value = 0 if len(stockOpen) == 0 else sum(stockOpen)/len(stockOpen)
print("平均",avg_value)
##問題:1.同時印出日期跟最大資料 2.針對某月份印出資料

# 3. 畫出圖表