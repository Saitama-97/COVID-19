import requests
from bs4 import BeautifulSoup
import json
from pyecharts import Geo

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
header = {
    'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
raw = json.loads(json.loads(requests.get(url, headers=header).text)['data'])
print(raw)

# LastUpdateTime
# updateTime = raw['lastUpdateTime']
#
# # chinaConfirmAdd
# chinaConfirmAdd = []
# # chinaSuspectAdd
# chinaSuspectAdd = []
# # chinaDeadAdd
# chinaDeadAdd = []
# # chinaHealAdd
# chinaHealAdd = []
# # date
# date = []
#
#
# chinaDayList = raw['chinaAdd']
# for item in chinaDayList:
#     # print(item)
#     chinaConfirmAdd.append(item['confirm'])
#     chinaSuspectAdd.append(item['suspect'])
#     chinaDeadAdd.append(item['dead'])
#     chinaHealAdd.append(item['heal'])
#     date.append(item['date'])
#
#
# print(updateTime)
# print(chinaConfirmAdd)
# print(chinaSuspectAdd)
# print(chinaDeadAdd)
# print(chinaHealAdd)
# print(date)
