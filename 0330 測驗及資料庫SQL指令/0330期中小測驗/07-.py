list = []
while True:
    x=input("請輸入數字(q離開):")
    if x=="q":
        break
    list.append(float(x))

print(list)

list1=[]
""" 
total=0
while True:
    try:
        x=input("輸入成績(q離開):")
        if x=="q":
            break
        list1.append(int(x))
        total=total+int(x)
    except:
        print("請輸入整數")
print("輸入的所有成績",list1)
"""