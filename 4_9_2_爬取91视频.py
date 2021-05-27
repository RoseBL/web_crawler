import requests
import re
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
}

# https://ccn.91p52.com//m3u8/428819/42881921.ts
# https://cdn.91p07.com//m3u8/471132/471132.m3u8?st=iPV3TsTS5GZ-5AJD7JXX9Q&e=1621760628
# # https://ccn.91p52.com//m3u8/428819/428819.m3u8?st=ZaEqMsgq8KU7sfk9C9bnUw&e=1619122060
# https://cdn.91p07.com//m3u8/471132/471132.m3u8?st=mzw7dkPG-M9IQRAUwY9vHA&e=1621761266
url = "https://cdn.91p07.com//m3u8/470292/470292.m3u8?st=e85YPIrWtf_m9M785PxPMQ&e=1621762430"
requests.packages.urllib3.disable_warnings()
resp = requests.get(url, headers=headers, verify=False)
url_Domain = url.split("470292.m3u8")[0]
# print(resp.text)
# with open("database/movie/" + "470292.m3u8", mode="wb") as f:
#     f.write(resp.content)
# resp.close()

# 如何解析m3u8文件

with open("database/movie/470292.m3u8", mode="r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # 先去掉空格，空白，换行符
        if line.startswith("#"):  # startswith() 方法用于检查字符串是否是以指定子字符串开头,如果是则返回 True，否则返回 False
            continue
        # print(line)
        # 拼接下载url
        # url_down = url_Domain + line
        url_down = "https://cdn.91p07.com//m3u8/470292/4702920.ts"
        print(url_down)
        # https://cdn.91p07.com//m3u8/470292/4702920.ts
        # 下载视频片段
        resp1 = requests.get(url_down)
        f = open(f"database/movie/11.ts", mode="wb")
        f.write(resp1.content)
        f.close()
        resp1.close()
# mac: cat 1.ts 2.ts 3.ts > xxx.mp4
# windows: copy /b 1.ts+2.ts+3.ts xxx.mp4


# lst = []
# with open("database/movie/470292.m3u8", mode="r", encoding="utf-8") as f:
#     for line in f:
#         if line.startswith("#"):
#             continue
#         line = line.strip()
#         lst.append(f"database/movie/{line}")
#
# s = "|".join(lst)  # 1.ts 2.ts 3.ts
# os.system(f'ffmpeg -i "concat:{s}" -c copy -absf aac_adtstoasc database/movie/movie.mp4')
# print("搞定!")
