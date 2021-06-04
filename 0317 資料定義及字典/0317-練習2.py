A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A - B)
#print(A + B)
print(A & B)                # 交 集 and
print(A | B)                # 聯 集 or
print(A.union(B))           # 聯集
print(A.intersection(B))    # 交集
#減少
print(A)
A.discard(2)
print(A)
A.remove(4)
print(A)
#增加
A.add(4)
print(A)
A.update([2,3,4])
print(A)


print("===練習===")
A={"apple","banana"}
B={"banana","watermelon"}
print(A)
print(B)

print("==A 和 B 買的所有品項==")
# A 和 B 買的所有品項
print(A | B)
print("==A 和 B 都有買的品項==")
# A 和 B 都有買的品項
print(A & B)
print("==A 有買的品項,但B沒買的品項==")
# A 有買的品項,但B沒買的品項
print(A - B)
print("==B 有買的品項,但A沒買的品項==")
# B 有買的品項,但A沒買的品項
print(B - A)