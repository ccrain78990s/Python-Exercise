# 第六題: 透過 input 輸入 3個數字, 並存放到 List 矩陣之
list = []
for x in range(0,3):
    x=input("請輸入數字:")
    list.append(float(x))
print(list)

y=max(list)
print("最大數字:",y)

import matplotlib.pyplot as plt
label=['num1','num2','num3']
plt.plot(label,list)
plt.show()
