#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"

import matplotlib.pyplot as plt
import csv
list1=[]
listClose=[]   # 收盤價
listDate=[]    # 日期
listOpen=[]    # 開盤價
listVolume=[]  # Volume 成交量
listSM5=[]     # SM5
listDiff=[]    # 漲跌
with open('2330.TW.csv', 'r',encoding="utf-8") as fin:
        read = csv.reader(fin, delimiter=',')
        header = next(read)   # 讀擋頭
        print(header)
        x=0
        for row in read:
            print(row[1])
            #if  (int(row[7])==2021 and   int(row[8])==1):  # 2008 01
            list1.append(int(x))
            listClose.append(float(row[4]))      # close
            listOpen.append(float(row[1]))      # open
            listVolume.append(float(row[6]))      # 開盤價
            listDate.append(row[0])            # 日期

            ### sm5 的計算 start
            total=0
            sm=5
            if x>=sm:
                for day in range(x,x-sm,-1):
                    print(total, listClose[day],day)
                    total=total+float(listClose[day])
                    print(total)
                total=total/(sm)
                print(total)
            else:
                total=float(listClose[x])   # 前五天
            listSM5.append(total)
            ### sm5 的計算 end

            x=x+1
        plt.subplot(3, 1, (1, 2))
        plt.plot(list1,listClose, 'r-',label="close")
        plt.plot(list1,listOpen, 'b-',label="open")
        plt.plot(list1,listSM5, 'g-',label="SM5")
        plt.title('open-close')
        plt.legend()

        plt.subplot(3, 1, (3))
        plt.title('Volume')
        plt.plot(list1, listVolume, 'r-', label="Volume")


        plt.legend()
        plt.show()


# 1. 印出所有資料
# 2. 最大 最小 平均

def findValue(value1):
    global sheet
    global list1
    global list2
    global listDate
    for i in range(1, len(list2)):
        try:
            curr = list2[i]  # close
            if value1 == curr:
                print("日期是:",listDate[i],"價格為:",list2[i])
        except:
            print("error-----------")

print("最大",max(list2))
print(findValue(max(list2)))
print("最小",min(list2))
print(findValue(min(list2)))   # <----

avg_value = 0 if len(list2) == 0 else sum(list2)/len(list2)
print("平均",avg_value)



# 3. 畫出圖表