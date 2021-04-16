import re

# # findall: 匹配字符串中所有的符合正则的内容
# lst = re.findall(r"\d+", "我的电话：10086，她的电话：12345")
# print(lst)
#
# # finditer: 匹配字符串中所有的符合正则的内容[返回的是迭代器],从迭代器中拿内容需要.group()
# it = re.finditer(r"\d+", "我的电话：10086，她的电话：12345")
# for i in it:
#     print(i.group())
# # search: 找到一个结果就返回，[返回的是match对象],拿内容需要.group()
# s = re.search(r"\d+", "我的电话：10086，她的电话：12345")
# print(s.group())

# # match: 从头开始匹配 找到一个结果就返回，[返回的是match对象],拿内容需要.group()
# ma = re.match(r"\d+", "10086，她的电话：12345")
# print(ma.group())

# # 预加载正则表达式
#
# obj = re.compile(r"\d+")
#
# ret = obj.finditer("我的电话：10086，她的电话：12345")
# for it in ret:
#     print(it.group())
#
# ret = obj.finditer("呵呵呵，你阿达100123000")
# for it in ret:
#     print(it.group())

s = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='1'>宋蝶</span></div>
<div class='jolin'><span id='1'>大枞木</span></div>
<div class='sylar'><span id='1'>范思哲</span></div>
<div class='tory'><span id='1'>胡受不起</span></div>
"""
# (?P<分组名字>正则)  可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='.*?'><span id='\d'>(?P<WAWA>.*?)</span></div>", re.S)#re.S:让.匹配换行符

resu = obj.finditer(s)
for it in resu:
    print(it.group("WAWA"))