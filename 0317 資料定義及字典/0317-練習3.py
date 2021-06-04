d = {'cat': 'cute',
     'dog': 'love'}

print(d['cat'])        
print('cat' in d)

d['fish'] = 'wet'
print(d['fish'])

print(d.get('monkey', 'N/A'))   
print(d.get('fish', 'N/A')) 
del(d['fish'])        
print(d.get('fish', 'N/A'))  



d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))
####

#"王先生" 去 "中壢"
#"李先生" 去 "台中"
#"林小姐" 去 "新竹"
#透過迴圈印出來
print("===練習===")
d={"王先生":"中壢","李先生":"台中","林小姐":"新竹"}
for who in d:
    where=d[who]
    print("%s 去 %s" % (who,where))

d=[{"姓名":"王喵喵","地址:":"台中"},
   {"姓名":"江汪汪","地址:":"高雄"}]
print(d)
print(d[0])
print(d[1])
print(d[0]["姓名"])
for x in d:
    print(x["地址"])
    x=x+1