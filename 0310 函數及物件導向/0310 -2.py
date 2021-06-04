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