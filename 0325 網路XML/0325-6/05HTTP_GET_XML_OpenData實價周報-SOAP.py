import sys
from xml.etree import ElementTree

try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x


def print_node(node):
    try:
       print("node.text:%s" % node.text)
    except:
       print("node.text:null")


try:
    url="http://data.taipei/opendata/datalist/datasetMeta/download?id=ece023db-a5f8-4399-97da-f04d7f4009e3&rid=1a2d417e-c121-4a12-835f-97ee6852c4b8"
    url="https://data.taipei/api/getDatasetInfo/downloadResource?id=ece023db-a5f8-4399-97da-f04d7f4009e3&rid=1a2d417e-c121-4a12-835f-97ee6852c4b8"
    url="https://data.taipei/api/getDatasetInfo/downloadResource?id=ece023db-a5f8-4399-97da-f04d7f4009e3&rid=1a2d417e-c121-4a12-835f-97ee6852c4b8"
    url="https://data.taipei/api/getDatasetInfo/downloadResource?id=ece023db-a5f8-4399-97da-f04d7f4009e3&rid=1a2d417e-c121-4a12-835f-97ee6852c4b8"
    url="https://data.taipei/api/getDatasetInfo/downloadResource?id=a9a97996-3a55-46c8-9076-e5ebdefad6dc&rid=2979c431-7a32-4067-9af2-e716cd825c4b"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents=reponse.read().decode("UTF-8")
        else:
            contents=reponse.read()
        fr = open('workfile.txt', 'w')
        fr.write(contents)
        fr.close()

        print(contents)
        # print_node(contents)
        # define namespace mappings to use as shorthand below
        namespaces = {
            'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
            'a': 'http://tempuri.org/',   #<--- 需要修改
        }
        root = ElementTree.fromstring(contents)
        t1 = root.findall('soap:Body/a:RPWeekDataResponse',namespaces)
        print(t1)
        t2=t1[0].findall("a:RPWeekDataResult",namespaces)
        print(t2)
        t3=t2[0].findall("a:Rows",namespaces)
        print(t3)
        t4=t3[0].findall("a:Row",namespaces)
        print(t4)
        print(len(t4))
        for node in t4:
            t5=node.findall("a:Col4",namespaces)
            print(t5[0].attrib["LOCATION"])

        #<Col4> "行善路286-290號(單號)"  <Col4/>
        #<Col4 LOCATION="行善路286-290號(單號)"/>

except:
    print("error")
