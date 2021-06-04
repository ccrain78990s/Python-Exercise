# 0319
"""
xlsx格式 需要把版本倒退 ↓
pip install xlrd==1.2.0
"""
import xlrd
import xlwt


read=xlrd.open_workbook('統一發票開的張數.xlsx')  # xls, xlsx,
sheet=read.sheets()[0]
#sheet=read.sheets("Sheet5")        #選工作集
print(sheet.nrows)           #印出有幾筆資料  直行
print(sheet.ncols)
#張數指標 總和 最大 最小 平均
#哪個市區最大?
list1=[]
total=0
for i in range(1,sheet.nrows):
    total=total+int(sheet.cell(i, 10).value)
    list1.append(int(sheet.cell(i, 10).value))

print("張數指標總和:", total)
print("平均:",total/(sheet.nrows-1))   #扣掉抬頭

list2=list1.copy()
list2.sort()
print("最小",list2[0])
print("最大",list2[sheet.nrows-2])    #扣掉抬頭 從0開始計算再扣1

x=1
while x<len(list2):
    y=list2[x]
    print("張數指標:",y, end="")
    id=list1.index(y)
    print("  學號:",id)
    list1[id]=-1
    # print("list2:",list2)
    x=x+1
"""






print("===3.3本次數學平均分數===")
x=0
total=0
while x<=(len(mathList)-1):
    total=total+mathList[x]
    x=x+1
#total =sum(mathList)
print(total/len(mathList))

print("===4.1找出不及格成績===")
list60down=[x for x in mathList if x<60]
print(list60down)

print("===4.2幫不及格的成績+10分===")
list60down=[x+10 for x in mathList if x<60]
print(list60down)

print("===5列出所有分數(最低分排到最高分)===")
listLowToHight=mathList.copy()
listLowToHight.sort()
print(listLowToHight)

x=0
while x<len(list5):
    y=list5[x]
    print("分數:",y, end="")
    id=list2.index(y)
    print("  學號:",id)
    list2[id]=-1
    # print("list2:",list2)
    x=x+1
"""