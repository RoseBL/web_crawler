import requests

query = input("输入一个你喜欢的明星")

url = f"https://www.sogou.com/web?query={query}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}

resp = requests.get(url, headers=headers)
print(resp)

print(resp.text)
