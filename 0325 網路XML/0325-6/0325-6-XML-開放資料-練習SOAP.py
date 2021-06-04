#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"

#0325

import sys 
from xml.etree import ElementTree
import urllib.request as httplib  # 3.x


def print_node(node):
    try:
       print("node.text:%s" % node.text)
    except:
       print("node.text:null")


try:
    url="https://data.taipei/api/getDatasetInfo/downloadResource?id=a9a97996-3a55-46c8-9076-e5ebdefad6dc&rid=2979c431-7a32-4067-9af2-e716cd825c4b"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            #contents=reponse.read().decode(reponse.headers.get_content_charset())
            contents=reponse.read().decode("UTF-8")
        else:
            contents=reponse.read()

        """
        fr = open('workfile.txt', 'w')
        fr.write(contents)
        fr.close()
        """


        print(contents)
        print_node(contents)
        root = ElementTree.fromstring(contents)

        lst_node = root.findall("RPWeekDataResult/Rows/Row/col1")[1].attrib["DISTRICT"]
        print(lst_node)

        #for node in lst_node:
        #    print(node.text)
        #    #print_node(node)
except:
    print("error")
