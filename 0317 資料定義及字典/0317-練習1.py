#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"

list1 = [1,2,3,4]
print(list1)
print(list1*2)

#### 情況 1.
## 方法 1:
i=0
for x in list1:
	list1[i]=list1[i]*2
	i=i+1
print(list1)

"""
for x in list1
   return x*2
"""
## 方法 2:
list1 = [1,2,3,4]
list1=[x*2 for x in list1]	# <---****難度較高
print(list1)				# [2,4,6,8]
# ↓ ↓ ↓ 解析 1
"""
[x*2 for x in list1]
[
	for x in list1:
		x * 2
]
"""
# ↓ ↓ ↓ 解析 2
"""
# [x*2 for x in list1]
[
  for x in list1
    return  x*2 
]
"""
#### 情況 2.
list1 = [1,2,3,4]
list1=[x*2 for x in list1 if x % 2==0]   #[4, 8] , % = 取餘數
print(list1)

"""
[
	 for x in list1:
        if x % 2==0:
		   x*2
]
"""


"""
# [x*2 for x in list1 if x % 2==0]
[
for x in list1:
  if x % 2==0:
   return x*2
]
"""
#### 情況 3.
list1 = [1,2,3,4]
list1=[x for x in list1 if x>=3]   # [3, 4]
print(list1)

"""
[
	 for x in list1:
       if x>=3:  
        x
]
"""



"""
# [x for x in list1 if x>=3]
 [
  for x in list1:
    if x>=3:
      return x
 ]
"""
#### 情況 4.

list1 = [59,60,70,80]
list1=[x**2 for x in list1 if x<60]    # 3481]
print(list1)
"""
# [x**2 for x in list1 if x<60]
[
   for x in list1:
      if x<60:
        return x**2 
]

"""
### 情況 5.
list1 = [20,30,50,80]
list1=[x for x in list1 if (x>=30 and x<=50)]   # [30, 50]
print(list1)   # 30,50

"""
# [x for x in list1 if (x>=30 and x<=50)]
[
   for x in list1:
    if (x>=30 and x<=50):
       return x 
]
"""

#### 更多參考
list1 = [1,2,3,4]
# [1,3] -> +100   ->    [101,103]
# [x for x in list1 if (x>=30 and x<=50)]
for x in list1:
   if x % 2==1:
	   print(x+100)


list1=[x+100 for x in list1 if x % 2==1]
print(list1)





list1=[1,2,3,4]
list1=[x+10 for x in list1 if x >=3 ]  # >=3   +10
print(list1)

"""
list1=[1,2,3,4]
>=3   +10
"""

#### 練習 0317
list1=[1,2,3,4]
# if x >= 3
# x+100
# list1=[x...for x in list1 if ...]
# print()
# 練習題1: [103,104]
# 練習題2: [2,3]
# 練習題3: [2*10,3*10]
# 練習題4: [1,3]
# 練習題5: [1,2]
print("===練習題1===")
list1=[1,2,3,4]
list1=[x+100 for x in list1 if x >= 3]
print(list1)
print("===練習題2===")
list1=[1,2,3,4]
list1=[x for x in list1 if x==2 or x==3]
print(list1)
print("===練習題3===")
list1=[1,2,3,4]
list1=[x*10 for x in list1 if x==2 or x==3]
print(list1)
print("===練習題4===")
list1=[1,2,3,4]
list1=[x for x in list1 if x==1 or x==3]
print(list1)
print("===練習題5===")
list1=[1,2,3,4]
list1=[x for x in list1 if x==1 or x==2]
print(list1)

print("===練習題6===")
list1=[1,2,3]
# [1,2,3,4]
# [1,2,3,4,5]
# 5
# [1,2,3,4]
# [1,2,4]
# [4,2,1]
# [1,2,4]

list1=[1,2,3]
list1.append(4) # [1,2,3,4]
print(list1)

list1.append(5) # [1,2,3,4,5]
print(list1)

x=list1.pop()	# 5
print(x)

print(list1)  # [1,2,3,4]

list1.remove(3)	# [1,2,4]
print(list1)

list1.reverse()	# [4,2,1]
print(list1)

list1.reverse()	# [1,2,4]
print(list1)