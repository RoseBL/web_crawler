from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
# 用户包装下拉菜单
from selenium.webdriver.support.select import Select
import time

# 准备好配置的参数
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable--gpu")

web = Chrome(options=opt)  # 把参数配置设置到浏览器中

web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")

# 定位到下拉列表
sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')
# 对元素进行包装，包装成下来菜单
sel = Select(sel_el)
# 让浏览器进行调整选型
for i in range(len(sel.options)):  # i 就是每一个下拉框选择的索引位置
    sel.select_by_index(i)  # 按照索引进行切换
    time.sleep(2)
    table = web.find_element_by_xpath('//*[@id="TableList"]/table')
    print(table.text)
    print("========================================")
print("运行完毕！！！")
web.close()
