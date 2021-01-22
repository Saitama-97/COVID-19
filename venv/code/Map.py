import requests
from bs4 import BeautifulSoup
import json
from pyecharts import Geo

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
header = {
    'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
raw = json.loads(json.loads(requests.get(url, headers=header).text)['data'])
# print(raw)

# LastUpdateTime
updateTime = raw['lastUpdateTime']
# print(updateTime)

keys = ['lastUpdateTime', 'chinaTotal', 'chinaAdd', 'isShowAdd', 'showAddSwitch', 'areaTree']
# for key in keys:
#     print(raw[key])
#     print()


# ChinaTotal
# chinaTotalConfirm = raw['chinaTotal']['confirm']
# chinaTotalSuspect = raw['chinaTotal']['suspect']
# chinaTotalDead = raw['chinaTotal']['dead']
# chinaTotalHeal = raw['chinaTotal']['heal']
# print(chinaTotalConfirm, chinaTotalSuspect, chinaTotalDead, chinaTotalHeal)

# ChinaAdd
chinaAddConfirm = raw['chinaAdd']['confirm']
chinaAddSuspect = raw['chinaAdd']['suspect']
chinaAddDead = raw['chinaAdd']['dead']
chinaAddHeal = raw['chinaAdd']['heal']
print(chinaAddConfirm, chinaAddSuspect, chinaAddDead, chinaAddHeal)
print()

# cityList
cityLst = []

# cityAddList
cityAddLst = []

china = raw['areaTree'][0]['children']
for p in china:
    print(p['name'], '*', p['today']['confirm'])
    cityLst.append(p['name'])
    cityAddLst.append(p['today']['confirm'])
    cities = p['children']
    for c in cities:
        print(c['name'], c['today']['confirm'])
    print()

print(len(cityLst), cityLst)
print(len(cityAddLst), cityAddLst)

dict = {}
for i in range(0, 34):
    dict[cityLst[i]] = [cityAddLst[i], 0]

title = '全国疫情地图'
subtitle = "新增确诊:" + str(chinaAddConfirm) + " 新增疑似:" + str(chinaAddSuspect) + " 新增死亡:" + str(
    chinaAddDead) + " 新增治愈:" + str(chinaAddHeal) + " 更新日期:" + updateTime

geo = Geo(title=title, title_color="#2E2E2E", subtitle=subtitle,
          title_text_size=24, title_top=20, title_pos="center", width=1400, height=700,
          background_color='white')
geo.add("", cityLst, cityAddLst, type="effectScatter", is_random=True, visual_range=[0, 80],
        maptype='china', visual_text_color="#FF0000", geo_normal_color="gray", geo_emphasis_color='blue',
        symbol_size=8, effect_scale=5, is_visualmap=True)

geo.render(path='plague.html')
