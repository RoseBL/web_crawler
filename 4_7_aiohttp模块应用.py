import aiohttp
import asyncio
import aiofiles
import time

urls = [
    "http://kr.shanghai-jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/a2c58d6d726fb7ef29390becac5d8643.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/d7de3f9faf1e0ecdea27b73139fc8d3a.jpg"
]


async def aiodownload(url):
    # 发送请求
    # 得到图片
    # 保存图片
    # aiohttp.ClientSession.get()
    name = url.rsplit("/", 1)[1]  # 从右边切，切一次，得到[1]位置的内容

    # # 下面代码运行结果没有问题，但是会提示session没有关闭，建议采用后面的写法
    # async with aiohttp.ClientSession().get(url) as resp:
    #     with open("database/" + name, mode="wb") as f:
    #         f.write(await resp.content.read())  # 读取内容是异步的，需要await挂起
    # print(name, "OK!!")

    async with aiohttp.ClientSession() as session:  # 该session 相当于requests
        async with session.get(url) as resp:  # 相当于resp = requests.get()
            # 请求回来了，写入文件
            # resp.content.read() ==> resp.content
            # resp.text() ==> resp.text
            # resp.json() ==> resp.json()
            async with aiofiles.open("database/" + name, mode="wb") as f:  # 创建文件
                await f.write(await resp.content.read())  # 读取内容是异步的，需要await挂起
            # with open("database/" + name, mode="wb") as f:  # 创建文件
            #     f.write(await resp.content.read())  # 读取内容是异步的，需要await挂起
    print(name, "OK!!")


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)
