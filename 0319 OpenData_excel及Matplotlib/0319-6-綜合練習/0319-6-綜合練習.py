import csv
import matplotlib.pyplot as plt
from datetime import datetime

date=[]
stockOpen=[]
stockHigh=[]
stockLow=[]
stockClose=[]

with open('0050.TW.csv', 'r',encoding="utf-8") as fin:
    read = csv.reader(fin, delimiter=',')
    header = next(read)
    print(header)
    if ="null":
    for row in read:
        print(row)

        current_date = datetime.strptime(row[0], '%Y-%m-%d')  # 將日期資料轉換為datetime物件
        date.append(current_date)  # 儲存日期
        stockOpen=int(row[1])
        stockOpen.append(stockOpen)
        stockHigh = row[2]
        stockHigh.append(stockHigh)
        stockLow = row[3]
        stockLow.append(stockLow)
        stockClose = row[4]
        stockClose.append(stockClose)



# 1. 印出所有資料
# 2. 最大 最小 平均
# 3. 畫出圖表


#根據資料繪製圖形
plt.title('0050.TW',fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel('dollar($NT.)',fontsize=16)

plt.plot(date,row[1],c='red',label='Open')
plt.plot(row[2],c='blue',label='Hight')
plt.plot(row[3],c='yellow',label='Low')
plt.plot(row[4],c='blue',label='Close')


plt.legend()
plt.axis([0,100,0,100])


plt.show()