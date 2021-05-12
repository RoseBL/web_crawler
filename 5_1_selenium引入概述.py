"""
selenium:自动化测试工具
可以打开浏览器，然后像人一样去操作浏览器
可以从selenium中直接提取网页上的各种信息
环境搭建：
    1.pip install selenium -i 清华源
    2.下载浏览器驱动https://npm.taobao.org/mirrors/chromedriver，根据自己浏览器的版本选择
    3.把解压的浏览器驱动，chromedriver放在python解释权所在的文件夹下
"""

# 让selenium启动谷歌浏览器
from selenium.webdriver import Chrome
# 用于模拟键盘输入
from selenium.webdriver.common.keys import Keys
import time

# 1.创建浏览器对象
web = Chrome()
# 2.打开一个网站
web.get("http://lagou.com")
print(web.title)
# 找到某个元素，点击它
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[1]/a')
# 点击操作
el.click()
# 防止操作过快
time.sleep(1)
# 找到输入框，输入python，---->输入回车/点击搜索按钮
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python", Keys.ENTER)
# 防止操作过快
time.sleep(1)
# 点击搜索按钮
# ss = web.find_element_by_xpath('//*[@id="search_button"]')
# ss.click()
# 查找存放页面数据的位置，进行数据提取
# 找到页面存放数据的所有li
# //*[@id="s_position_list"]/ul/li[1]
# //*[@id="s_position_list"]/ul/li[2]
li_list = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
for li in li_list:
    job_name = li.find_element_by_tag_name("h3").text
    job_price = li.find_element_by_xpath("./div/div/div[2]/div/span").text
    job_company = li.find_element_by_xpath('./div/div[2]/div/a').text
    print(job_company, job_name, job_price)
web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()
# 如何进入新窗口进行提取
# 注意，在selenium的眼中，新窗口默认是不切换过来的
web.switch_to.window(web.window_handles[-1])
# 在新窗口提取内容
job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)
# 关掉子窗口
web.close()
# 变更selenium的窗口视角，回到原来的窗口中
web.switch_to.window(web.window_handles[0])
"""
处理iframe的话，必须先拿到iframe，然后切换视角到iframe,再然后才可以拿到数据
切换到iframe
    web.switch_to.frame(iframe)
切换回去,切换回原页面
    web.switch_to.default_content()
"""