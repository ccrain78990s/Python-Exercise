# 0317
#第一題 :
#請設計一個輸入input數學成績的迴圈,並用list紀錄所輸入的成績
# [50,70,60]
#第二題 :
#延續上題,當輸入q就離開迴圈,並列印出list所有的數學成績
# [50,70,60]
#第三題 :
#延續上題,顯示出 1. 合格60的數學成績 2. 有幾位合格 3. 本次的數學平均成績
# [60,70]   2   60
#第四題 :
#延續上題, 1.找出不及格的成績 2.幫不及格的成績+10分
# [50]  [60,60,70]
#第五題 :
#延續上題,請有最低到最高的分數排列出所有的分數
# [50,60,70]
#第六題 :
#延續上題,請有最低到最高的分數排列出所有的分數,並且印出那個分數是"輸入時第幾個"輸入(也就是學號)
# [50,60,70]  [0,2,1]

print("===1用list紀錄所輸入成績===")
mathList=[]
while True:
    try:
        math= input("請輸入數學成績:")
        if math=="q":
            break
        mathList.append(int(math))
    except:
        print("請輸入整數")

print("===2印出list所有數學成績===")
print(mathList)

print("===3.1合格的數學成績===")
list60up=[x for x in mathList if x>=60]
print(list60up)

print("===3.2有幾位合格===")
print(len(list60up))

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

print("===6列出所有分數(最低分排到最高分)並且印出那個分數是輸入時第幾個輸入(也就是學號)===")
#0318修改 還沒完成
d={}
x=0
while x<len(mathList):
    print(x)
    print(mathList[x])
    d[mathList[x]]=int(x)
    print(d)
    x=x+1

for key in d:
    number=d[key]
    print("分數: %d 學號: %d" % (key,number))
