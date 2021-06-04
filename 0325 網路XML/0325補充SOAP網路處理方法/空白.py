import requests
from xml.etree import ElementTree

response = requests.get('http://www.labs.skanetrafiken.se/v2.2/querystation.asp?inpPointfr=yst')

# define namespace mappings to use as shorthand below
namespaces = {
    'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    'a': 'http://www.etis.fskab.se/v1.0/ETISws',
}
dom = ElementTree.fromstring(response.content)

# reference the namespace mappings here by `<name>:`
names = dom.findall(
    './soap:Body'
    '/a:GetStartEndPointResponse'
    '/a:GetStartEndPointResult'
    '/a:StartPoints'
    '/a:Point'
    '/a:Name',
    namespaces,
)
print(names)
for name in names:
    print(name.text)