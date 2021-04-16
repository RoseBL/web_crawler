from lxml import etree
# /表示层级关系，第一个/是根节点
# text()拿文本
# //后代
# * 任意的节点，通配符
# xpath的顺序是从1开始数的，[]表示索引
# [@xxx=xxx]属性的筛选
# 拿到属性值：@属性

# 拿到页面源代码
# 提取和解析数据
import requests
from lxml import etree

url = "https://beijing.zbj.com/search/f/?type=new&kw=saas"
resp = requests.get(url)
# print(resp.text)
# 解析
html = etree.HTML(resp.text)
# 拿到每一个服务商的div
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[6]/div[1]/div")

for div in divs:  # 每一个服务商信息
    price = div.xpath("./div/div/a[1]/div[2]/div[1]/span[1]/text()")[0].strip("¥")
    title = "saas".join(div.xpath("./div/div/a[1]/div[2]/div[2]/p/text()"))
    com_name = div.xpath("./div/div/a[2]/div[1]/p/text()")[0]
    location = div.xpath("./div/div/a[2]/div[1]/div/span/text()")[0]
    print(price)
    print(title)
    print(com_name)
    print(location)
