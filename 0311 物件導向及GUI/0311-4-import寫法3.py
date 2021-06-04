#0311
def main():
    print("Hello World!")

if __name__ == "__main__":      #<----
    main()
    print(__name__)
    print(__file__)

import MyFun as lib1    #<---把檔案名稱換掉
from sub import MyFun3

#
y=lib1.fun3(1,2)
print(y)

x=lib1.fun3(num1=1,num2=2)
print(x)

#
MyFun3.fun1()
MyFun3.fun2(1,2)
MyFun3.fun3(a=1,b=1)
x=MyFun3.fun4(1,2)
print(x)






