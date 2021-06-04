###0316複習檔案

"""
# 1. 建立一個people 的類別class
#people("林志玲",18,175,50,"female")
# 2. 在該類別內,建立一個方法method 印出 姓名和身高
# 3. 沿用 people 的類別,建立三個人的基本資料
class people(object):
    def __init__(self,x,y,z,a,b):
        self.name=x
        self.age=y
        self.high=z
        self.weight=a
        self.gender=b
        print("姓名:"+str(x),"年紀:"+str(y),
              "身高:"+str(z),"體重:"+str(a),
              "性別:"+str(b))
    #↓↓↓在該類別內 建立一個方法method 印出姓名和身高↓↓↓↓
    def funNameHigh(self):
        print("姓名:",self.name,"身高:",self.high)

id1=people("林志玲",18,175,50,"female")
id1.funNameHigh()

id2=people("小玲",23,168,48,"female")
id2.funNameHigh()

id3=people("小志",30,180,77,"male")
id3.funNameHigh()

# 4. 請把同學名稱給印出來  <-----
list1=[1,2,3,4]
print(list1[0])
list2=[id1,id2,id3]
print(id1)
print(list2[0])
list2[0].funNameHigh()

x=0
for x in list1:
    list1[x].funNameHigh()
    x=x+1
while x<len(list1):
    list1[x].funNameHigh()
    x=x+1
"""

#0316新增

class office(object):
    name=""
    stockCode=0
    industry=""
    def __init__(self,iName,iStockCode,iIndustry):
        self.name=iName
        self.stockCode=iStockCode
        self.industry=iIndustry
    def funPrintOffInfo(self):
        print("公司名稱:", self.name, " 股票代碼:", self.stockCode,"產業別:",self.industry)
    def funStrPrintOffInfo(self):
        str1="公司名稱:"+self.name+" 股票代碼:"+str(self.stockCode)+"產業別:"+self.industry
        return str1

"""
1. 透過class建立公司基本資料
2. 透過method方法 印出公司基本資料
"""
t1=office("鴻海",2317,"半導體")
t1.funPrintOffInfo()
print(t1.name)

"""
3.使用相同的類別 放入其他2家公司的基本資料
"""

t2=office("台積電",2330,"半導體")
t2.funPrintOffInfo()

t3=office("聯發科",2454,"半導體")
t3.funPrintOffInfo()

"""
4. 類別的Method xxx.回傳公司基本資料
"""
print(t1.funStrPrintOffInfo())

"""
5. tkinter GUI 請你把剛剛的公司
   透過tkinter 顯示到 label 視窗上面
"""
import tkinter as tk

str1=t1.funStrPrintOffInfo()
str2=t2.funStrPrintOffInfo()
str3=t3.funStrPrintOffInfo()

win = tk.Tk()

win.wm_title("Hello,JING,0316複習,公司資料")     #設定視窗標題
win.minsize(width=600, height=600)                      #視窗最小尺寸
win.maxsize(width=600, height=600)                      #視窗最大尺寸
win.resizable(width=False, height=False)                #是否可調整視窗大小

label1 =tk.Label(win,bg="blue",text=str1,fg="yellow",font=20)     #放上啥文字 顏色
label1.place(x=120, y=40)                                   #要放在哪裡?從左上角開始計算

label2 =tk.Label(win,bg="black",text=str2,fg="yellow",font=10)
label2.place(x=115, y=140)

label3 =tk.Label(win,bg="red",text=str3,fg="yellow",font=20)
label3.place(x=120, y=240)

win.mainloop()