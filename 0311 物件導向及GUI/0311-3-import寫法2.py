#0311
def main():
    print("Hello World!")

if __name__ == "__main__":      #<----
    main()
    print(__name__)
    print(__file__)

import MyFun as lib1    #<---把檔案名稱換掉
import MyFun2

#
y=lib1.fun3(1,2)
print(y)

x=lib1.fun3(num1=1,num2=2)
print(x)

#
MyFun2.fun1()
MyFun2.fun2(1,2)
MyFun2.fun3(a=1,b=1)
x=MyFun2.fun4(1,2)
print(x)






