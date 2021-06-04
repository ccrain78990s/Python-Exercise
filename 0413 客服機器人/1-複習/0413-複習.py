#0413小複習
print("======練習1======")
a="我愛吃滷肉飯嗎?"
print(a)
b="我愛吃高麗菜嗎?"
print(b)
c="我愛吃水煎包嗎?"
print(c)
d="我愛吃鹹酥雞嗎?"
print(d)

print("======練習2======")
list=["滷肉飯","高麗菜","水煎包","鹹酥雞"]
#print(len(list))
print("我愛吃"+""+list[0]+""+"嗎?")
print("我愛吃"+""+list[1]+""+"嗎?")
print("我愛吃"+""+list[2]+""+"嗎?")
print("我愛吃"+""+list[3]+""+"嗎?")

print("======練習3======")
x=0
for x in (range(0,len(list))):
    print("我愛吃"+""+list[x]+""+"嗎?")

print("======練習4======")
def ILikeEat(x):
    print("我愛吃"+""+x+""+"嗎?")
#return
x=0
while x <len(list):
    ILikeEat(""+list[x]+"")
    x=x+1

print("======練習5======")
print("請看其他檔案")

print("======練習6======")
import xlrd
import xlwt

write = xlwt.Workbook()         #新增excel
write2 = write.add_sheet('ILikeEat')
write2.write(0, 0, ""+a+"")
write2.write(1, 0, ""+b+"")
write2.write(2, 0, ""+c+"")
write2.write(3, 0, ""+d+"")

write.save('food.xls')
