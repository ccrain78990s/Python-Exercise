#0310 下午
def fun1():
    global y    #<--------
    x=1         #local variable
    print(x)
    y=3
    print(y)    #成功 因為y 是全域變數

def fun2():
    #local variable
    # print(x) 會有錯誤 因為x是區域變數
    print("")
    z=4        #區域變數
    print(z)   #輸出 4

y=2         #global variable
fun1()
#print(x)   #會有錯誤 因為x是區域變數
print(y)    #y 輸出為 3


z=2
fun2()
print(z)    #輸出為 2

#補充  漂亮寫法
def fun3(t):
    print(t)
    t=t+1
    return t
t=10
fun3(t)
t=fun3(t)
fun3(t)



