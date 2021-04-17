# 原理，通过第三方的一个机器去发送请求

import requests

# 218.60.8.83:3129

proxies = {
    "https": "https://120.78.206.20:3128"
    # "https": "47.103.11.129:3128"
}
resp = requests.get("https://www.baidu.com", proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)
