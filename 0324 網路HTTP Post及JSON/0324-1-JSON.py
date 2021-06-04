#!/usr/bin/env python
# 0324 練習JSON
import json

data = {
    'name' : 'Powen Ko',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data)        #字典轉字串
print(json_str)
data = json.loads(json_str)        #反向操作 轉成字典
print(data)
print(data['name'])
#印出價格
print(data['price'])

data2= {
'people' : { "name":"www" ,"age":18}
}

print("===data2===")
# data 2 印出 name
print(data2['people']['name'])

data3= {
'person' : [ { "name":"xxx" ,"age":18},
             {"name": "Lee", "age": 17},
             ]
}

print("===data3===")
#  data 3 印出 name
#  方法1
t1=data3['person']
t1=t1[0]
t1=t1['name']
print(t1)
# 方法2
print(data3['person'][0]['name'])
#印出17
print(data3['person'][1]['age'])


data4= {
'person' :{ "group":
             [ { "name":"powen","age":18},
               {"name": "Lee", "age": 17},
             ]
          }
}
#印出powen
print("===data4===")
print(data4['person']['group'][0]['name'])
print("===data5===")


#data5=???
#print(data5['person']['class']['A'][0]['name']) #寫出JSON dic
data5={'person':
        {'class':
            {'A':
                [{ "name":"d5","age":18},
                 {"name": "Lee", "age": 17}]
                                             }
                                               }
                                                 }

print(data5['person']['class']['A'][0]['name'])