# 0323 練習 +畫面切割

import matplotlib.pyplot as plt
import csv
from datetime import datetime


date=[]
list1=[]
listDate=[]    # 日期
stockOpen=[]
stockHigh=[]
stockLow=[]
stockClose=[]
stockVolume=[]
stockUpDown=[]
listSM5=[]     # SM5

with open('2330.TW.csv', 'r') as fin:
    read = csv.reader(fin, delimiter=',')
    header = next(read)     # 讀擋頭
    print(header)
    x=0
    for row in read:
        print(row)
        current_date = datetime.strptime(row[0], '%Y-%m-%d')  # 將日期資料轉換為datetime物件
        date.append(current_date)  # 儲存日期
        list1.append(int(x))
        listDate.append(row[0])    # 日期

        stockOpen.append(float(row[1]))

        stockHigh.append(float(row[2]))

        stockLow.append(float(row[3]))

        stockClose.append(float(row[4]))

        stockVolume.append(int(row[6]))

        stockUpDown.append(float(row[4])-float(row[1]))




        x=x+1

        ### sm5 的計算 start
        total = 0
        sm = 5
        if x >= sm:
            for day in range(x, x - sm, -1):
                print(total, stockClose[day], day)
                total = total + float(stockClose[day])
                print(total)
            total = total / (sm)
            print(total)
        else:
            total = float(stockClose[x])  # 前五天
        listSM5.append(total)
        ### sm5 的計算 end


    plt.subplot(7, 1, (1,3))
    plt.plot(list1, stockClose, 'k-')
    plt.plot(list1, listSM5, 'g-', label="SM5")
    plt.title('Close')


    plt.subplot(7, 1, (4,5))
    plt.plot(date, stockVolume, 'y-')
    plt.title('Volume')

    plt.subplot(7, 1, (6,7))
    plt.plot(date, stockUpDown, 'r-')
    plt.title('Ups and downs')

    plt.tight_layout()          #間距調整

    plt.show()

print(stockUpDown)


#. 練習題1:
#       下載2330.TW 一年的資料, 並在Python 讀取
#. 練習題2:
#.       畫出 每天收盤價
#. 練習題3:
#.       用畫面切割的分法 subpolot 在另外一個圖表上 畫出每天的成交量 Volume
#. 練習題4:
#.       用畫面切割的分法 subpolot 在另外一個圖表上 畫出每天的漲跌圖  close-open
#. 練習題5: * * *
#.       在收盤價圖表上 畫出SM5   (五日平均價)  五天的平均價格