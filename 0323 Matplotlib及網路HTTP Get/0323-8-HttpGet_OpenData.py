
# https://data.taipei/#/dataset/detail?id=6d15899a-ff77-4a39-8203-a3addfe1fa28

import sys 
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x

try:
    #臺北捷運路線發車班距頻率資料服務
    #url="https://ptx.transportdata.tw/MOTC/v2/Rail/Metro/Frequency/TRTC?$format=xml"
    # 桃園公共自行車即時服務資料
    url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
    # 車輛偵測器動態資料
    url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f65920c8-0ba2-467c-8f26-0a3b7f543c51&rid=9dd1a96d-fd75-4208-b688-e85bde24c4bf"
    #路外停車資訊
    url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f4cc0b12-86ac-40f9-8745-885bddc18f79&rid=0daad6e6-0632-44f5-bd25-5e1de1e9146f"
    #臺中市消費者物價指數－商品性質分類
    url="https://datacenter.taichung.gov.tw/swagger/OpenData/37a56800-7363-45a5-bf59-2acebb3192da"
    #
    url="https://www.dgbas.gov.tw/public/data/open/localstat/088-%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E8%80%85%E8%81%B7%E6%A5%AD%E5%88%A5%E5%B9%B3%E5%9D%87%E6%AF%8F%E4%BA%BA%E9%9D%9E%E6%B6%88%E8%B2%BB%E6%94%AF%E5%87%BA.xml"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            #contents=reponse.read().decode(reponse.headers.get_content_charset())
            contents=reponse.read().decode("utf-8")
            #contents = reponse.read().decode("utf-8")
        else:
            contents=reponse.read()
        print(contents)
except:
    print("error")   