# 拿到页面源代码
# 通过re来提取想要的有效数据

import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}
resp = requests.get(url=url, headers=headers)
page_content = resp.text

# 解析数据

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*? <div class="bd">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span class="rating_num" property="v:average">(?P<average>.*?)</span>.*?<span>(?P<people>.*?)人评价</span>', re.S)

result = obj.finditer(page_content)
f = open("database/"+"豆瓣TOP.csv", mode="w", encoding="utf-8")
csvwrite = csv.writer(f)
for it in result:
    # print(it.group("name"))
    # print(it.group("average"))
    # print(it.group("people"))
    # print(it.group("year").strip())
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwrite.writerow(dic.values())
f.close()
print('over')
