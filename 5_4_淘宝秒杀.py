# 让selenium启动谷歌浏览器
from selenium.webdriver import Chrome
# 用于模拟键盘输入
from selenium.webdriver.common.keys import Keys
import time
import datetime


def login():
    # 等待页面完全加载
    time.sleep(1)
    # 找到某个元素，点击它  找到  元素  通过 局部  链接  文本
    if web.find_element_by_partial_link_text('亲，请登录'):
        web.find_element_by_partial_link_text('亲，请登录').click()
        # 跳转到登录页面以后，提示用户扫码登录
        print('请在10秒内扫码登录')
        # //*[@id="fm-login-id"]  账户
        # //*[@id="fm-login-password"] 密码
        # //*[@id="login-form"]/div[4]/button 登录
        time.sleep(15)
        # 防止操作过快
        time.sleep(2)
        # 跳转到购物车
        # https://cart.taobao.com/cart.htm
        web.get('https://cart.taobao.com/cart.htm')
        time.sleep(2)
        if web.find_element_by_xpath('//*[@id="J_SelectAll2"]/div/label'):
            web.find_element_by_xpath('//*[@id="J_SelectAll2"]/div/label').click()
    # 打印当前时间
    now_time = datetime.datetime.now()
    print('选择商品时间为：%s' % now_time)


# 设置秒杀时间  对比系统时间  时间一到  就执行结算
def buy(buy_time):  # buy_time 设定秒杀的时间  比如  2021-5-12 21:00:00
    # 循环对比时间
    while True:
        # 获取当前时间
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(now)
        # d对比是否达到抢购时间
        if now >= buy_time:
            try:
                # 时间一到，点击结算
                web.find_element_by_partial_link_text('结 算').click()
            except:
                pass
        # 打印当前时间
        print(now)
        # 睡眠0.1秒，循环对比是否达到抢购时间
        time.sleep(0.1)


if __name__ == '__main__':
    times = input("请输入抢购的时间：2021-05-27 01:33:00")
    # 1.创建浏览器对象
    web = Chrome()
    # 2.打开一个网站
    web.get("https://www.taobao.com/")
    print(web.title)
    # 3.调用登录函数
    login()
    # 4.调用结算函数进行购买
    buy(times)
