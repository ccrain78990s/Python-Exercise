#0317 CH7 資料定義

print("===append===")
list1=[3,1,2]
print(list1)
list1.append(100)   #<----添加資料到陣列最後面
print(list1)
list1.append(2197)
print(list1)

print("===extend===")
list2=[2,1,3]
print(list2)
list2.extend([10])  #<----添加 " 矩陣 " 資料到陣列最後面
print(list2)
list2.extend([21,97])
print(list2)

print("===insert===")
list3=[3,1,2]
print(list3)
list3.insert(2,3)   #<----添加資料到指定位置 insert(指定位置,資料)
print(list3)
list3.insert(1,5)   #try 寫出 [3,5,1,3,2]
print(list3)
#[3,1,2,5,1,3,2] 同時加入1,2
# 方法1:
list3.insert(1,1)
list3.insert(2,2)
print(list3)
# 方法2:
# for x in [2,1]:
#     list3.insert(1,2)
# or
# y=[1,2]
# for x in y.reverse():
#    list3.insert(1,x)

print("===remove===")
list4=[3,1,2]
print(list4)
list4.remove(2)     #<----移除指定資料
print(list4)
list4.remove(1)
print(list4)
# 延伸: 移除所有的1
list5=[3,1,2,1]
len(list5)
x=0
while x<len(list5):
    list5.remove(1)
    x=x+1
print(list5)

print("===pop===")
list6=[3,1,2,1]
print(list6)
x=list6.pop()       #<----取得和刪除最後的資料
print(x)
print(list6)
list6.pop()         #<----再做一次會怎樣呢????思考看看
print(list6)

print("===clear===")
list7=[3,1,2,1]
print(list7)
list7.clear()       #<----刪除所有的資料
print(list7)

print("===index===")
list8=[3,1,2,1]
print(list8)
print(list8.index(1))       #<----找第一個符合資料的位置
print(list8.index(2))
print(list8.index(3))

print("===count===")
list9=[3,1,2,1]
print(list9)
x=list9.count(1)              #<----查詢某項資料出現的次數
print(x)

print("===sort===")
list10=[3,1,2,1]
print(list10)
list10.sort()              #<----順序排列資料
print(list10)


print("===reverse===")
list11=[1,2,3,4]
print(list11)
list11.reverse()              #<----反轉資料
print(list11)


print("===copy===")
list12=[1,2,3]
print(list12)
list13=list12.copy()        # copy 複製 *注意
print(list13)
