# <video src = "不能播的视频.mp4"></video>
# 一般的视频网站是怎么做的
# 用户上传 --> 转码(把视频做处理,2k,1080,标清) --> 切片处理(把单个的文件进行拆分)
# 用户在进行拉动进度条的时候

# 需要一个文件记录：1.视频播放顺序；2.视频存放的路径
# MCU8
# 想要抓取一个视频：
# 1.找到M3U8(各种手段)
# 2.通过M3U8下载到ts文件
# 3.可以通过各种手段(不仅是编程手段)，把ts文件合并为一个mp4文件
"""
流程：
    1.拿到548121-1-1.html的页面源代码
    2.从源代码中提取到m3u8的url
    3.下载m3u8
    4.读取m3u8文件，下载视频
    5.合并视频
"""

import requests
import re

#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
# }
# obj = re.compile(r"url: '(?P<url>.*?)',", re.S)  # 用来提取m3u8的地址
# # obj = re.compile(r"url: '(?P<url>.*?)',", re.S)  # 用来提取m3u8的url地址
# url = "https://www.91kanju.com/vod-play/54812-1-1.html"
#
# resp = requests.get(url, headers=headers)
# m3u8_url = obj.search(resp.text).group("url")  # 拿到m3u8的地址
#
# print(m3u8_url)
# resp.close()
# # 下载m3u8文件
# resp2 = requests.get(m3u8_url, headers=headers)
#
# with open("database/movie/" + "哲任王后.m3u8", mode="wb") as f:
#     f.write(resp2.content)
# resp2.close()
# print("下载完毕！！！")


# 如何解析m3u8文件
# n = 1
# with open("database/movie/哲任王后.m3u8", mode="r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()  # 先去掉空格，空白，换行符
#         if line.startswith("#"):  # startswith() 方法用于检查字符串是否是以指定子字符串开头,如果是则返回 True，否则返回 False
#             continue
#         print(line)
#         # 下载视频片段
#         resp3 = requests.get(line)
#         f = open(f"database/movie/{n}", mode="wb")
#         f.write(resp3.content)
#         f.close()
#         resp3.close()
#         n += 1



