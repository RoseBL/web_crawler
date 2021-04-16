# 登录->得到cookie
# 带着cookie去请求到书架URL->书架上的内容
#
# 必须的把上面的两个操作连起来
# 我们可以使用session进行请求->session你可以认为是一连串的请求，在这个过程中cookie不会丢失

import requests

# 会话
session = requests.session()
url = "https://passport.17k.com/ck/user/login"

data = {
    "loginName": "17364943563",
    "password": "lb18180472136"
}

resp = session.post(url, data=data)
print(resp.text)
print(resp.cookies)
