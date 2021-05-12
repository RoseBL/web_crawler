from selenium.webdriver import Chrome

web = Chrome()

web.get("http://www.chaojiying.com/user/login/")
img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png

