#0310-2 CH5函數 物件導向
def funInt():
    print("Int")
    return  666    #回傳

def funFloat():
    print("Float")
    return 66.6

def funStr():
    print("Str")
    return "aaa"

def funList():
    print("list")
    return [11,22,33]

def funInt2():
    return 4,5    #python比較特別的地方 用逗號回傳兩個資料

def funA():
    return 11,2.2,"AAA",[99,100]

def funB():
    x=100
    x=x+1
    return x

x=funInt()
print(x)
x=funFloat()
print(x)
x=funStr()
print(x)
x=funList()
print(x)

x1,x2=funInt2() ##
print(x1,x2)

x1,x2,x3,x4=funA() ##
print(x1,x2,x3,x4)

y=funB()
print(y)


def fun4():
    commodity1 = input("商品1購買金額:")
    commodity1 = float(commodity1)
    commodity2 = input("商品2購買金額:")
    commodity2 = float(commodity2)
    total=0
    if commodity1 > 100:
        if commodity2 > 100:
            print("所有商品 打 8 折")
            print("商品1價格:", commodity1 * 0.8, "商品2價格:", commodity2 * 0.8)
            print("結算金額:", commodity1 * 0.8 + commodity2 * 0.8)
            total=commodity1 * 0.8 + commodity2 * 0.8
        else:
            print("商品1打9折 ， 商品2打 9.5 折")
            print("商品1價格:", commodity1 * 0.9, "商品2價格:", commodity2)
            print("結算金額:", commodity1 * 0.9 + commodity2)
            total=commodity1 * 0.9 + commodity2
    else:
        if commodity2 > 100:
            print("商品2 打 9.5 折")
            print("商品1價格:", commodity1, "商品2價格:", commodity2 * 0.95)
            print("結算金額:", commodity1 + commodity2 * 0.95)
            total=commodity1 + commodity2 * 0.95
        else:
            print("商品無打折")
            print("商品1價格:", commodity1, "商品2價格:", commodity2)
            print("結算金額:", commodity1 + commodity2)
            total=commodity1 + commodity2
    return total

fun4()

def fun5():
    price=input("購買金額:")
    price1=float(price)
    memberCard=True #打 9 折
    invoice=True    #加 5 %
    total=0
    if memberCard == True:
        if invoice == True:
            print("有會員卡 且需要 發票 價格為:",price1*0.9*1.05)
            total=price1*0.9*1.05
        else:
            print("有會員卡 但不需要 發票 價格為:",price1*0.9)
            total=price1*0.9
    else:
        if invoice == True:
            print("無會員卡 且需要 發票 價格為:",price1*1.05)
            total= price1*1.05
        else:
            print("無會員卡 但不需要 發票 價格為:",price1)
            total=price1
    return total

fun5()