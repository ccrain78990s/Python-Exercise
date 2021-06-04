#0310 CH5函數 物件導向
def fun1():
    print("fun1")
    print("fun1")
    print("fun1")

fun1()
print("end")


def fun1a():
    print("fun1a")
    print("try")
fun1a()
print("end")

def fun1b():
    print("Yo")
    print("fun1b")
fun1b()
print("end")

#####比較漂亮寫法
def fun1():
    print("fun1")
    print("fun1")
    print("fun1")

def fun1a():
    print("fun1a")
    print("try")

def fun1b():
    print("Yo")
    print("fun1b")

fun1()
fun1a()
fun1b()
fun1a()
fun1()
print("end")
#####

#1
def priceCount():
    price = input("購買金額:")
    price1 = float(price)
    memberCard = True  # 打 9 折
    invoice = True  # 加 5 %
    if memberCard == True:
        print("有會員卡，打九折 價格為:", price1 * 0.9)
        if invoice == True:
            print("有會員卡 且需要 發票 價格為:", price1 * 0.9 * 1.05)
        else:
            print("有會員卡 但不需要 發票 價格為:", price1 * 0.9)
    else:
        print("無會員卡，無打折 價格為:", price1)
        if invoice == True:
            print("無會員卡 且需要 發票 價格為:", price1 * 1.05)
        else:
            print("無會員卡 但不需要 發票 價格為:", price1)
    print("謝謝光臨~~~請慢走")

priceCount()
priceCount()
print("結算完成")
#2
def commodityPriceCount():
    commodity1 = input("商品1購買金額:")
    commodity1 = float(commodity1)
    commodity2 = input("商品2購買金額:")
    commodity2 = float(commodity2)
    if commodity1 > 100:
        if commodity2 > 100:
            print("所有商品 打 8 折")
            print("商品1價格:", commodity1 * 0.8, "商品2價格:", commodity2 * 0.8)
            print("結算金額:", commodity1 * 0.8 + commodity2 * 0.8)
        else:
            print("商品1打9折 ， 商品2打 9.5 折")
            print("商品1價格:", commodity1 * 0.9, "商品2價格:", commodity2)
            print("結算金額:", commodity1 * 0.9 + commodity2)
    else:
        if commodity2 > 100:
            print("商品2 打 9.5 折")
            print("商品1價格:", commodity1, "商品2價格:", commodity2 * 0.95)
            print("結算金額:", commodity1 + commodity2 * 0.95)
        else:
            print("商品無打折")
            print("商品1價格:", commodity1, "商品2價格:", commodity2)
            print("結算金額:", commodity1 + commodity2)

commodityPriceCount()
commodityPriceCount()
commodityPriceCount()
commodityPriceCount()
print("完成~~~")
