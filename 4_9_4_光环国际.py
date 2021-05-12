# # "https://mv.aura-el.com/eaa719f235af4fda8ce63871930c2338/804bbdfe44d94160a298a74624c4a90c-c6bd8ef011abe26c234ddaa74bb7b086-fd-encrypt-stream.m3u8"
# 让selenium启动谷歌浏览器
from selenium.webdriver import Chrome
# 用于模拟键盘输入
from selenium.webdriver.common.keys import Keys
import time
from Crypto.Cipher import AES
import requests

#
# 1.创建浏览器对象
# web = Chrome()
# # 2.打开一个网站
# web.get("https://yun.aura.cn/Login/login.html")
#
# # web.get("https://yun.aura.cn")
# print(web.title)
# web.find_element_by_xpath('//*[@id="xieyi_box"]/div/button').click()
# time.sleep(1)
# web.find_element_by_xpath('//*[@id="phone"]').send_keys("18180472136")
# web.find_element_by_xpath('//*[@id="passwd"]').send_keys("hhxxttxs1")
# time.sleep(5)
# web.find_element_by_xpath('//*[@id="safe_login"]').click()

url = "http://ebt192.doc88.com/getebt-0rUXzqMV2qMU1rUQ2KUS0LMT0q3R2KUS0LMT0q3X2qPU0T0X1V9IskVWrQNlrP==.ebt"
resp = requests.get(url)
with open("dkbb", "wb") as f:
    f.write(resp.content)

# "https://mv.aura-el.com/eaa719f235af4fda8ce63871930c2338/804bbdfe44d94160a298a74624c4a90c-c6bd8ef011abe26c234ddaa74bb7b086-fd-encrypt-stream.m3u8"
# "https://mv.aura-el.com/eaa719f235af4fda8ce63871930c2338/804bbdfe44d94160a298a74624c4a90c-493ca596e158004f712cc7c9362a63a1-fd-encrypt-stream-00003.ts"

# 下载m3u8文件
# url = "https://mv.aura-el.com/eaa719f235af4fda8ce63871930c2338/804bbdfe44d94160a298a74624c4a90c-c6bd8ef011abe26c234ddaa74bb7b086-fd-encrypt-stream.m3u8"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
# }
# resp = requests.get(url, headers=headers)
# print(resp.text)
# with open("database/movie/" + "光环国际.m3u8", mode="wb") as f:
#     f.write(resp.content)
# resp.close()
# 解析m3u8文件
# url_Domain = url.split("/804")[0]
# url_Domain = url_Domain + "/"
# print(url_Domain)
# with open("database/movie/光环国际.m3u8", mode="r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()  # 先去掉空格，空白，换行符
#         if line.startswith("#"):  # startswith() 方法用于检查字符串是否是以指定子字符串开头,如果是则返回 True，否则返回 False
#             continue
#         # print(line)
#         # 拼接下载url
#         url_down = url_Domain + line
#         print(url_down)
#         # 下载视频片段
#         resp1 = requests.get(url_down)
#         f = open(f"database/movie/{line}", mode="wb")
#         f.write(resp1.content)
#         f.close()
#         resp1.close()

# resp = requests.get(
#     "NTdiMThhZWEtMmQ0OS00YmNmLThhYzktMjUwOWYwYzRhN2U1MU4yMHh0MmxwZUZCalNCQXdlemxsem1USk9mUW5CSkdBQUFBQUFBQUFBQUkyTWhGamlzbWVrTkFwTy84VEhsS3lBQ0hDbk1hdkpEalUxUS9oRUU2NXNPQ0hPRnFXYkky"
#     "NTdiMThhZWEtMmQ0OS00YmNmLThhYzktMjUwOWYwYzRhN2U1Y3FTbEF0eU4vM2JvczZVQkFoOFJDUEI2cXozRTViRjZBQUFBQUFBQUFBQndOS3RWaUVobEVXTHZHaWsrcjNCanFFS2lpbGRDdnhndmxZdUJuMEZJejVmblo2UmhwUEV5"
# print(resp.text)
"""
IEEhxZ3R3EL8QsUFvljJzFb4rMcxk2OoLMTmt7m4vWQ=
wmvLvETyYHrReWR1Znt36i76rOTt1zJzMm8+8za6U/w=

U7yf1moi/q/Ya2+8xdl9KdYyU+dUXDP3zPNx2lxf9yc=
IE+kRNtlwM9Ol/0J0B/sLl4naCa/JRSAuDaYeIXQhr4=
wFdWOWdghaSnuv1T3eL0+d/NOG/Gt89uWaqwsakujyQ=
eTYB8/lLVK1hodjMrDYV9/6My2YBfjq2FBpeuYx4jnc=
"NTdiMThhZWEtMmQ0OS00YmNmLThhYzktMjUwOWYwYzRhN2U1Y3FTbEF0eU4vM2JvczZVQkFoOFJDUEI2cXozRTViRjZBQUFBQUFBQUFBQndOS3RWaUVobEVXTHZHaWsrcjNCanFFS2lpbGRDdnhndmxZdUJuMEZJejVmblo2UmhwUEV5"
8043
12176
2144
 var y = (" " + o[n + 1]).slice(1)
CAIShwN1q6Ft5B2yfSjIr5aHPMOFgpFO9pidZ2XLgUwYS+gUloL/kzz2IHpKeXduAeAXs/o0mmhZ7/YYlrMqEMAYHRWfMpsrssgOrV36JpLFst2J6r8JjsUAjvAr81mpsvXJasDVEfl2E5XEMiIR/00e6L/+cirYpTXHVbSClZ9gaPkOQwC8dkAoLdxKJwxk2t14UmXWOaSCPwLShmPBLUxmvWgGl2Rzu4uy3vOd5hfZp1r8xO4axeL0PoP2V81lLZplesqp3I4Sc7baghZU4glr8qlx7spB5SyVktyWGUhJ/zaLIoit7NpjfiB0eoQAPopFp/X6jvAawPLUm9bYxgphB8R+Xj7DZYaux7GzeoWTO80+aKzwNlnUz9mLLeOViQ4/Zm8BPw44ELhIaF0IUExzEW+FevL/pgmQPl/+FJLoiv9mjcBHqHzz5sePKlS1RLGU7D0VIJdUbTlzbUBLgzK5Iv5bLVcSKwI+V+yPMax3bQFDr53vsTbbXzZb0mptuPnzdwJ4TWbrgkeUGoABm9kni2IoRjD3kYP2LWVNICsnoOIUv04qvVhYURzdH2C0/8e0RZEpiaB3T+gEG4/Ramq3V3FIng14FsrlDTBo/OWDlnJTke4B6pV+xDuIjJSAi0WJPA8HnJed9a5YrKRiAcHX3Brs8Eo8fes3mBEDHjGJNFG5SC/RfoalIg6P+7U=
"""
