#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

import os
import os.path
import shutil               #用在複製檔案
FileName1='workfile.txt'
FileName2='workfileCopy.txt'
FileName3='workfileRename.txt'
"""
path="" 
exName=".py"
allFiles=OS.lisrdir(path)
print(allFiles)
for x in allFiles:
print(x)
index=x.find()exName


"""
def FunListAllFiles(iMeg):
	allFiles = os.listdir('.')
	print(iMeg)
	print(allFiles)

try:
    FunListAllFiles("1.")
    if os.path.isfile(FileName1) and os.access(FileName1, os.R_OK):
        shutil.copy(FileName1, FileName2)       #複製檔案


    FunListAllFiles("2.")
    if os.path.isfile(FileName2) and os.access(FileName2, os.R_OK):
        os.rename(FileName2, FileName3)         #修改檔名


    FunListAllFiles("3.")
    if os.path.isfile(FileName3) and os.access(FileName3, os.R_OK):
        os.remove(FileName3)                    #刪除檔案
        print('%s deleted' %(FileName3))

    if os.path.isdir("新增資料夾")==True:
        print("發現文件夾")
except:
    print("error")

FunListAllFiles("4.")

#請印出本目錄中的所有.py的程式