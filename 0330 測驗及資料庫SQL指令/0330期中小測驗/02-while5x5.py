x=1
while x<=5:
    print(x)
    y = 1
    while y <=5:
         print(y)
         print(x, "*", y, "=", x * y)   # 只要x等於4  y等於4 就不印
         y = y + 1
    x = x + 1