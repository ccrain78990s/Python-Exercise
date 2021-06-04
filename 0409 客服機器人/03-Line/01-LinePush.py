import requests

auth_token='jk36TjswuZE3G0v9aVlsVq1drMzDYlo9p77//1gK/64QjgvnlLMhBpitXiCTen8eKhTaGMef8egr2dUkdnXbUCPt1gpb0cl7eCLeSljRcCSBWf4yyqOn3lmvdml0/93zX7whfqOdL8oDMLUifvSo9AdB04t89/1O/w1cDnyilFU='
hed = {'Authorization': 'Bearer ' + auth_token}
data = {
    "to": "U936a8a4a4f642ad8172501d59d8d766c",
    "messages":[
        {
            "type":"text",
            "text":"Hello, world1"
        },
        {
            "type":"text",
            "text":"Hello, world2"
        }
    ]
}

url = 'https://api.line.me/v2/bot/message/push'
response = requests.post(url, json=data, headers=hed)
print(response)
print(response.json())