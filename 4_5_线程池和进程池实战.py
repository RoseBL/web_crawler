# 1.如何提取单个页面的数据
# 2.上线程池，多个页面同时抓取

import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("database/"+"价格.csv", mode="w", encoding="utf-8")
csvWriter = csv.writer(f)


# 要爬取数据的url
# url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
def download_one_page(url):
    resp = requests.get(url)
    resp.encoding = "utf-8"
    html = etree.HTML(resp.text)
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    print(table)
    trs = table.xpath("./tr")[1:]
    # trs = table.xpath("./tr[position()>1]")
    # print(len(trs))
    for tr in trs:
        txt = tr.xpath("./td/text()")
        # 对数据做简单的处理:\\ /去掉
        txt = (item.replace("\\", "").replace("/", "") for item in txt)
        # print(list(txt))
        # 把数据存放在文件中
        csvWriter.writerow(txt)
    print(url, "提取完毕！，进行下一个")


if __name__ == '__main__':
    # 该方式效率极其低下
    # for i in range(1, 12000):
    #     download_one_page(f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            # 把下载任务提交给线程池
            t.submit(download_one_page, f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")
    print("全部下载完毕！！")
