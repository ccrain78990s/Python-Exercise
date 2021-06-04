#0310複習1

#練習1: a 和 b 在 if 的各種判斷

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

#練習2: 用if 寫出 if a和b , a或b的判斷式
a=True
b=True
if a==True and b==True:
    print("a == True 並且 b == True")
elif a==100 or b==200:
    print("a == True 或者 b == True")
else:
    print("都不是唷~")

#練習3: 客戶有會員卡打 9 折 如果要發票 加5%
price=input("購買金額:")
price1=float(price)
memberCard=True #打 9 折
invoice=True    #加 5 %
if memberCard == True:
    print("有會員卡，打九折 價格為:",price1*0.9)
    if invoice == True:
        print("有會員卡 且需要 發票 價格為:",price1*0.9*1.05)
    else:
        print("有會員卡 但不需要 發票 價格為:",price1*0.9)
else:
    print("無會員卡，無打折 價格為:",price1)
    if invoice == True:
        print("無會員卡 且需要 發票 價格為:",price1*1.05)
    else:
        print("無會員卡 但不需要 發票 價格為:",price1)
print("謝謝光臨~~~請慢走")

#練習4: 如果 商品 1>100 並且 商品 2>100 所有商品打 8折
#      如果 商品 1>100 商品1 打 9折
#      如果 商品 1>100 商品2 打 9.5折
commodity1=input("商品1購買金額:")
commodity1=float(commodity1)
commodity2=input("商品2購買金額:")
commodity2=float(commodity2)
if commodity1 > 100:
    if commodity2 > 100:
        print("所有商品 打 8 折")
        print("商品1價格:", commodity1*0.8, "商品2價格:", commodity2 * 0.8)
        print("結算金額:",commodity1*0.8+commodity2*0.8)
    else:
        print("商品1打9折 ， 商品2打 9.5 折")
        print("商品1價格:", commodity1*0.9, "商品2價格:", commodity2 )
        print("結算金額:",commodity1*0.9+commodity2)
else:
    if commodity2 > 100:
        print("商品2 打 9.5 折")
        print("商品1價格:",commodity1,"商品2價格:",commodity2*0.95)
        print("結算金額:", commodity1 + commodity2 * 0.95)
    else:
        print("商品無打折")
        print("商品1價格:", commodity1, "商品2價格:", commodity2 )
        print("結算金額:", commodity1 + commodity2)
print("end")
