d={"cat":"cute","dog":"love"}
print(d)
print(d["cat"])
print(d["dog"])

d={"cat":"cute","dog":"love","bird":"tiny"}
print(d["bird"])

d["pig"]="juice"    #增加新的
print(d)

print(len(d))

for key in d:
    print(key)
    print(d[key])

