
"""
def fun99(z):
    x = 1
    while x < (z + 1):
        y = 1
        while y < (z + 1):
            print(x, "*", y, "=", x * y)
            y = y + 1
        x = x + 1
c=input("做出XX乘法表:")
c=int(c)
fun99(c)
"""

class My99Count(object):
    maxX=1
    maxY=1
    def __init__(self,x,y):
        self.maxX=x
        self.maxY=y

    def fun99(self):
        x = 1
        while x <= self.maxX:
            y = 1
            while y <= self.maxX:
                print(x, "*", y, "=", x * y)
                y = y + 1
            x = x + 1

g=My99Count(4,4)
g.fun99()
print(g.maxX)
