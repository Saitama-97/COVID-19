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

# ChinaTotal
chinaTotalConfirm = raw['chinaTotal']['confirm']
chinaTotalSuspect = raw['chinaTotal']['suspect']
chinaTotalDead = raw['chinaTotal']['dead']
chinaTotalHeal = raw['chinaTotal']['heal']
print(chinaTotalConfirm, chinaTotalSuspect, chinaTotalDead, chinaTotalHeal)

# ChinaAdd
chinaAddConfirm = raw['chinaAdd']['confirm']
chinaAddSuspect = raw['chinaAdd']['suspect']
chinaAddDead = raw['chinaAdd']['dead']
chinaAddHeal = raw['chinaAdd']['heal']
print(chinaAddConfirm, chinaAddSuspect, chinaAddDead, chinaAddHeal)

# cityList
cityLst = []
# TotalList
cityTotalLst = []

china = raw['areaTree'][0]['children']
for p in china:
    print(p['name'], '*', p['total']['confirm'])
    cityLst.append(p['name'])
    cityTotalLst.append(p['total']['confirm'])
    cities = p['children']
    for c in cities:
        print(c['name'], c['total']['confirm'])
    print()

print(cityLst)
print(cityTotalLst)

dict = {}
for i in range(0, 34):
    dict[cityLst[i]] = [cityTotalLst[i], 0]

title = '全国疫情地图'
subtitle = "确诊:" + str(chinaTotalConfirm) + " 疑似:" + str(chinaTotalSuspect) + " 死亡:" + str(
    chinaTotalDead) + " 治愈:" + str(chinaTotalHeal) + " 更新日期:" + updateTime

geo = Geo(title=title, title_color="#2E2E2E", subtitle=subtitle,
          title_text_size=24, title_top=20, title_pos="center", width=1400, height=700,
          background_color='white')
geo.add("", cityLst, cityTotalLst, type="effectScatter", is_random=True, visual_range=[0, 800],
        maptype='china', visual_text_color="#FF0000", geo_normal_color="gray", geo_emphasis_color='blue',
        symbol_size=8, effect_scale=5, is_visualmap=True)

geo.render(path='plague.html')
