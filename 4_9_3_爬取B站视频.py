import requests
from lxml import etree
import re
import os

if __name__ == '__main__':
    url = input("请输入网址栏的url：")
    # url = "https://www.bilibili.com/video/BV1X64y1m7jW"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
        "Referer": "https://www.bilibili.com/video/"
    }
    # 对视频主页发送请求，获取响应
    resp = requests.get(url, headers=headers)
    page = resp.text
    # 转换类型
    html_obj = etree.HTML(page)
    title_name = html_obj.xpath('//title/text()')[0]
    # 提取视频名称
    title_name = re.findall(r'(.*?)_哔哩哔哩', title_name)[0]
    print(title_name)
    # 提取纯视频url，纯音频url
    url_str = html_obj.xpath('//script[contains(text(),"window.__playinfo__")]/text()')[0]
    # print(url_str)
    video_url = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)",', url_str)[0]
    # print(video_url)
    audio_url = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)",', url_str)[0]
    # print(audio_url)

    # 构造请求头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
        "Referer": url
    }
    # 发送请求
    resp_video = requests.get(video_url, headers=headers)
    resp_audio = requests.get(audio_url, headers=headers)
    data_video = resp_video.content
    data_audio = resp_audio.content
    title_new = title_name + '_temp'
    with open(f"database/videos/{title_new}.mp4", mode='wb') as f:
        f.write(data_video)
    with open(f"database/videos/{title_new}.mp3", mode='wb') as f:
        f.write(data_audio)
    # 拼接视频
    os.system(
        f'ffmpeg -i "database/videos/{title_new}.mp4" -i "database/videos/{title_new}.mp3" -c copy "database/videos/{title_name}.mp4"')
    # 删除临时视频
    os.remove(f"database/videos/{title_new}.mp4")
    os.remove(f"database/videos/{title_new}.mp3")
