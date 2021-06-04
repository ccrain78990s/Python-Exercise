# -*- coding: UTF-8 -*-
__author__ = "Chen"
# python 10-執行時帶參數.py aaa bbb
import sys

print(len(sys.argv))
if len(sys.argv)>1:
    print(sys.argv[1])
if len(sys.argv)>2:
    print(sys.argv[2])
