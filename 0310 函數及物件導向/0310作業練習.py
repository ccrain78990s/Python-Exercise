#0310 下午 練習函數

# a 和 b 在 if 的各種判斷

a=100
b=200
#各種大於小於..的情況
if a > b:
    print("a大於b")
elif a < b:
    print("a小於b")
elif a == b:
    print("a等於b")
elif a != b:
    print("不等於b")
elif a >= b:
    print("a大於或等於b")
elif a <= b:
    print("a小於或等於b")
else:
    print("都不是~")

"""    
練習1 設計函數 fun
funCompare(10,20):  # 印出 a小於b
funCompare(20,10):  # 印出 a大於b
funCompare(20,20):  # 印出 a等於b
"""
def funCompare(a=0,b=0):
    if a > b:
        print("a大於b")
    elif a < b:
        print("a小於b")
    elif a == b:
        print("a等於b")
    elif a != b:
        print("不等於b")
    elif a >= b:
        print("a大於或等於b")
    elif a <= b:
        print("a小於或等於b")
    else:
        print("都不是~")

funCompare(10,20)
funCompare(20,10)
funCompare(20,20)

"""
練習2  設計函數 fun
funCompareBool(True,True)   #  印出 "a==True 並且  b==True"
funCompareBool(True,False)  #  印出 "a==True 或  b==True" 
"""

def funCompareBool(a,b):
    if a==True and b==True:
        print("a==True 並且  b==True")
    elif  a==True or b==True:
        print("a==True 或  b==True")
    else:
        print("a!=True 並且  b!=True")

funCompareBool(True,True)
funCompareBool(True,False)



"""
#### 練習3:  客戶有會員卡打9折 如果要發票 加 5% 的函數
x=funCompareBool(100,memberCard=True,Tax=True)  # 回傳 94.5

memberCard=True # 會員卡
Tax=True # 要發票
price=100
# 客戶有會員卡打9折
if (memberCard==True):
    price = price*0.9

# 如果要發票 加 5%
if Tax==True:
    price = price*1.05

print("計算後的價格",price) # 94.5
"""
def funCompareBool(price,memberCard,Tax):
    if (memberCard == True):
        price = price * 0.9
    if Tax == True:
        price = price * 1.05
    return price

x=funCompareBool(100,memberCard=True,Tax=True)
print(x)
print("計算後的價格", x)  # 94.5

"""
#### 練習4:  如果 商品1>100 並且 商品2>100  所有商品打8折
####        如果 商品1>100 商品1打9折
####        如果 商品2>100 商品2打9.5折


x=funMath2Price(10,10)  # 回傳 94.5



"""

def funMath2Price(price1=0,price2=0):
    total=0
    if price1 > 100 and price2 > 100:
        #  所有商品打8折
        print("所有商品打8折 總價:", (price1 + price2) * 0.8)
        total=(price1 + price2) * 0.8
    elif price1 > 100:  # 如果 商品1>100 商品1打9折
        print("商品1打9折 商品1:", (price1 * 0.9), "商品2:", price2)
        total=(price1 * 0.9)+price2
    elif price2 > 100:  ####        如果 商品2>100 商品2打9.5折
        print("商品2打9.5折 商品1:", price1, "商品2:", price2 * 0.95)
        total=price1+price2 * 0.95
    else:
        print("商品1:", price1, "商品2:", price2, "總價:", (price1 + price2))
        total=price1+price2
    return total

total=funMath2Price(10,10)
print("計算後總價",total)

