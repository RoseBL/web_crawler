# import time
#
#
# def func():
#     print("我爱黎明")
#     time.sleep(3)  # 让当前的线程处于阻塞状态，CPU是不为我工作得
#     print("我真的爱黎明")
#
#
# if __name__ == '__main__':
#     func()
# input() 程序也是出去阻塞状态
# requests.get(url) 在网络请求返回数据之前，程序也是出去阻塞状态
# 一般情况下，当程序处于IO操作的时候，线程都会处于阻塞状态

# 协程：当程序遇见了IO操作的时候，可以选择性的切换到其他任务上
# 在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
# 在宏观上，我们看到的其实是多个任务一起在执行
# 多任务异步操作

# 协程代码---模板---start
import asyncio
import time


# async def func1():
#     print("你好啊，我是func1")
#     # time.sleep(3)  # 当程序出现了同步操作的时候，异步就中断了
#     await asyncio.sleep(3)  # 异步操作的代码
#     print("好的，我是func1")
#
#
# async def func2():
#     print("你好啊，我是func2")
#     # time.sleep(2)
#     await asyncio.sleep(2)  # 异步操作的代码
#     print("好的，func2")
#
#
# async def func3():
#     print("你好啊，我是func3")
#     # time.sleep(4)
#     await asyncio.sleep(4)  # 异步操作的代码
#     print("好的，func3")
#
#
# async def main():
#     # 第一种写法
#     # f1 = func1()
#     # await f1#一般await挂起操作放在协程对象前面
#
#     # 第二种写法(推荐)
#     tasks = [
#         asyncio.create_task(func1()),
#         asyncio.create_task(func2()),
#         asyncio.create_task(func3())
#     ]
#     await asyncio.wait(tasks)
#
#
# if __name__ == '__main__':
#     t1 = time.time()
#     asyncio.run(main())
#     t2 = time.time()
#     print(t2 - t1)

# 协程代码---模板---end


# 在爬虫领域的应用---模板---start

async def download(url):
    print("开始下载！")
    await asyncio.sleep(2)  # 网络请求
    print("下载完成")


async def main():
    urls = [
        "httpp://www.baidu.com",
        "http://www.bilibili.com",
        "http://www.163.com"
    ]
    tasks = []
    tasks = [asyncio.create_task(download(url)) for url in urls]  # 这样也可以
    # for url in urls:
    #     d = download(url)
    #     task = asyncio.create_task(d)
    #     tasks.append(task)  # 在py3.8以后用这种方法，加上asyncio.create_task
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())

# 在爬虫领域的应用---模板---end
