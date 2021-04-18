from multiprocessing import Process


# 第一种：基于函数
# def func():
#     for i in range(1000):
#         print("子进程", i)
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()
#     for i in range(1000):
#         print("主进程", i)

# 第二种：基于对象
class MyProcess(Process):
    def run(self):
        for i in range(1000):
            print("子进程", i)


if __name__ == '__main__':
    p = MyProcess()
    p.start()
    for i in range(1000):
        print("主进程", i)
