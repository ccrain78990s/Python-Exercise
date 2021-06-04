# 0317 切割

list1=[0,1,2,3,4]
list2=[10,11,12,13,14]

print(list1)
print(list1[3])  #3
print(list2)
print(list2[3])  #13
# 切割 1***
list1=[0,1,2,3,4]
print(list1[0:2])   #[0,1]      # 2之前的數字不包含2
print(list1[2:4])   #[2,3]
# 切割 2***
list1=[0,1,2,3,4]
print(list1[1:])    #[1,2,3,4]  #1後面的全部數字
print(list1[2:])    #[2,3,4]
print(list1[3:])    #[3,4]
print(list1[3:5])   # ↑ 的另一種寫法  (延伸切割1)
print(list1[4:])    #[4]
# 切割 3***
list1=[0,1,2,3,4]
print(list1[:3])    #[0,1,2]     # 3前面的全部數字
print(list1[:4])    #[0,1,2,3]
print(list1[:2])    #[0,1]
# 切割 4***
list1=[0,1,2,3,4]
print(list1[0:3])   #[0,1,2]
print(list1[0:-1])  #[0,1,2,3]  # 解釋:____
print(list1[-1:3])  #[]
print(list1[-4:3])  #[1,2]
print(list1[0:-2])  #[0,1,2]
print(list1[:-1])   #[0,1,2,3]
print(list1[-2:])   #[3,4]
print("===練習1===")
list2=[0,1,2,3,4,5,6,7,8,9]
#寫法1
len2=len(list2)
train=list2[:8]        #80
print(train)
#寫法2
x=int(len2*0.8)
train=list2[:x]        #80
print(train)

test=list2[x:]         #20
print(test)

print("===練習2===")
list3=[[0,1,2,3,4],
       [10,11,12,13,14],
       [20,21,22,23,24],
       [30,31,32,33,34],
       [40,41,42,43,44]]

print(list3[2][2])  #22
print(list3[3][1])  #31

print(list3[0:2])       #[[0,1,2,3,4],[10,11,12,13,14]]
#list不能這樣用  print(list3[0:2][0:2])  #[[0,1,2,3,4],[10,11,12,13,14]] 請避開