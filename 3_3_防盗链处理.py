# 1.拿到contId
# 2.拿到videoStatus返回的json.-> srcURL
# 3.srcURL里面的内容进行修整
# 4.下载视频

import requests

# 拉取视频的地址
# url = "https://www.pearvideo.com/video_1726830"
# contId = url.split("_")[1]
# videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.717029754217541"

url = "https://www.pearvideo.com/video_1726833"
contId = url.split("_")[1]
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.5090221386848517"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    # 防盗链:溯源，当前本次请求的上一级是谁
    "Referer": url
}
resp = requests.get(videoStatusUrl, headers=headers)
# print(resp.text)
dic = resp.json()
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
print(srcUrl)

with open("database/videos/"+"a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)
