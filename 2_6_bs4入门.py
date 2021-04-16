import requests
from bs4 import BeautifulSoup
import csv

# 1.拿到页面源代码
# 2.使用bs4进行解析，拿到数据


url = "http://www.xinfadi.com.cn/marketanalysis/1/list/1.shtml"

resp = requests.get(url)
f = open("菜价.csv", mode='w', encoding="utf-8")
csvwriter = csv.writer(f)
# print(resp.text)
# 解析数据
# 1.把页面源代码交给BeautifulSoup进行处理，生成BeautifulSoup对象
page = BeautifulSoup(resp.text, "html.parser")  # 指定html解析器
# 2.从bs对象中查找数据
# find(标签，属性=值)
# find_all(标签，属性=值)
# table = page.find("table", class_="hq_table")  # class是Python的关键字
table = page.find("table", attrs={"class": "hq_table"})  # 和上一行是一个意思，此时可以避免使用class_
# print(table)
# 拿到所有数据
trs = table.find_all("tr")[1:]
for tr in trs:  # 每一行数据
    tds = tr.find_all("td")  # 拿到每行中所有td
    name = tds[0].text  # .text 表示拿到被标签标记的内容
    low = tds[1].text  # .text 表示拿到被标签标记的内容
    avg = tds[2].text  # .text 表示拿到被标签标记的内容
    high = tds[3].text  # .text 表示拿到被标签标记的内容
    gui = tds[4].text  # .text 表示拿到被标签标记的内容
    kind = tds[5].text  # .text 表示拿到被标签标记的内容
    date = tds[6].text  # .text 表示拿到被标签标记的内容
    print(name, low, avg, high, gui, kind, date)
    csvwriter.writerow([name, low, avg, high, gui, kind, date])
f.close()
print("over!!")
