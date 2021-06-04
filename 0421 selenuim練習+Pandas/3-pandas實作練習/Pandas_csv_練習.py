#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
import pandas as pd
df = pd.read_csv('110年3月桃園捷運月運量統計.csv',encoding="big5",sep=",")
#df = pd.read_csv('https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=201be83f-f8ae-4435-8fdd-c0eb28fd1691&rid=549d4adb-95e9-4e05-b51a-b10fd549964c',encoding="big5",sep=",")
print(df.head())
df.to_csv("test.csv")
