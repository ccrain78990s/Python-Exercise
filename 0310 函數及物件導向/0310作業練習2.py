#if
#while
#for

# 練習1. while 印出 2,4,6,8,10
x=2
while x<12:
    print(x)
    x=x+2

# 練習2. while 印出  1 3 6 10 15 21 28 36    <-----
#                   1+2
#                      +3
#                         +4
#
#                           .....

x=1
y=0

while x<=8:
    y=y+x
    print(y)
    x=x+1

# 練習3 while  印出 1,2,3,4,5,6,7,8,9,10
#             並且當 數字為2 4 6 8 10 印出 "偶數"二字
x=1
while x<10:
    y=x%2
    if y == 0 :
        print(x,"偶數")
    else:
        print(x)
    x=x+1

# 練習4 使用 while  印出  九九乘法表
x=1
while x<10:
    y=1
    while y<10:
        print(x,"*",y,"=",x*y)
        y=y+1
    x=x+1

# 練習5 使用 while  印出  九九乘法表
#                 並且當 相乘後的答案為偶數時  印出 "偶數"二字
x=1
while x<10:
    y=1
    while y<10:
        z = x*y % 2
        if z == 0:
            print(x,"*",y,"=",x*y,"偶數")
        else:
            print(x, "*", y, "=", x * y)
        y=y+1
    x=x+1
# 練習6 使用 while  印出  九九九乘法表
#       例如 1*1*1=1
#           1*1*2=2
#           .......
x=1
while x<10:
    y=0
    while y<9:
        y=y+1
        z=0
        while z<9:
            z=z+1
            print(x,"*",y,"*",z,"=",x*y*z)
    x=x+1

# 練習7 使用 while  和 input   做出 x x 乘法表
#       例如  input 為 5 , 那就做出  五五乘法表
#       例如  input 為 9 , 那就做出  九九乘法表
z=input("做出xx乘法表:")
z=int(z)
x=1
while x<(z+1):
    y = 1
    while y < (z+1):
        print(x, "*", y, "=", x * y)
        y = y + 1
    x = x + 1

# 練習8  延續上題,  把它包成def 函數
def fun99(z):
    x = 1
    while x < (z + 1):
        y = 1
        while y < (z + 1):
            print(x, "*", y, "=", x * y)
            y = y + 1
        x = x + 1
c=input("做出XX乘法表")
c=int(c)
fun99(c)


