import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
}

# https://ccn.91p52.com//m3u8/428819/42881921.ts
url = "https://ccn.91p52.com//m3u8/428819/428819.m3u8?st=ZaEqMsgq8KU7sfk9C9bnUw&e=1619122060"
requests.packages.urllib3.disable_warnings()
resp = requests.get(url, headers=headers, verify=False)
url_Domain = url.split("428819.m3u8")[0]
# print(resp.text)
with open("database/movie/" + "428819.m3u8", mode="wb") as f:
    f.write(resp.content)
resp.close()

# 如何解析m3u8文件

with open("database/movie/428819.m3u8", mode="r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # 先去掉空格，空白，换行符
        if line.startswith("#"):  # startswith() 方法用于检查字符串是否是以指定子字符串开头,如果是则返回 True，否则返回 False
            continue
        # print(line)
        # 拼接下载url
        url_down = url_Domain + line
        print(url_down)
        # 下载视频片段
        resp1 = requests.get(url_down)
        f = open(f"database/movie/{line}", mode="wb")
        f.write(resp1.content)
        f.close()
        resp1.close()

