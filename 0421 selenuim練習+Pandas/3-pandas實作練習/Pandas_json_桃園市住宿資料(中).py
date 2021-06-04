#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
import pandas as pd
import json
from pandas import json_normalize

df = pd.read_json('桃園市住宿資料(中).json')
#print(df.to_string())
df = json_normalize(df['infos']) #Results contain the required data
print(df)


df=pd.DataFrame(df)
df.to_json(orient='index')
print(df)
#df.to_csv("test.csv")

#print(df.info())


"""
import pandas as pd
import json
from pandas import json_normalize

data = '''
{
"Results":
         [
         { "id": "1", "Name": "Jay" },
         { "id": "2", "Name": "Mark" },
         { "id": "3", "Name": "Jack" }
         ],
"status": ["ok"]
}
    '''

info = json.loads(data)

df = json_normalize(info['Results']) #Results contain the required data
print(df)
"""