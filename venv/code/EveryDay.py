import requests
from bs4 import BeautifulSoup
import json
from pyecharts import Geo

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
header = {
    'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
raw = json.loads(json.loads(requests.get(url, headers=header).text)['data'])
# raw = json.loads(requests.get(url, headers=header).text)['data']
print(raw)

# LastUpdateTime
updateTime = raw['lastUpdateTime']

# chinaConfirmDay
chinaConfirmDay = []
# chinaSuspectDay
chinaSuspectDay = []
# chinaDeadDay
chinaDeadDay = []
# chinaHealDay
chinaHealDay = []
# chinaAddDay
chinaAddDay = []
# date
date = []

chinaDayList = raw['chinaDayList']
for item in chinaDayList:
    # print(item)
    chinaConfirmDay.append(item['confirm'])
    chinaSuspectDay.append(item['suspect'])
    chinaDeadDay.append(item['dead'])
    chinaHealDay.append(item['heal'])
    date.append(item['date'])

print(updateTime)
print(len(chinaConfirmDay), chinaConfirmDay)
print(len(chinaSuspectDay), chinaSuspectDay)
print(len(chinaDeadDay), chinaDeadDay)
print(len(chinaHealDay), chinaHealDay)
print(len(date), date)
