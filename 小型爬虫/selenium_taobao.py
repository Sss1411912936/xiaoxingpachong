# 导入selenium工具
from selenium import webdriver
# 从selenium工具中导入驱动模块
from time import sleep

# 加入chrome浏览器的的无头操作
opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

# 创建一个基于chrome的驱动
driver = webdriver.Chrome(chrome_options=opt)
# driver对象可以自动化的操作chrome浏览器

# 用浏览器发起一个get请求
driver.get("https://www.baidu.com/")
# 点击页面上的某个按钮
btn = driver.find_element_by_link_text("新闻")
print(btn) #[<selenium.webdriver.remote.webelement.WebElement (session="43f7f4191eaa0a0bdd70b6703cb74951", element="0.29015434851673083-1")>]
# btn.click()
# 向输入框中输入内容
driver.find_element_by_id("kw").send_keys("老王")
driver.find_element_by_id("su").click()
sleep(2)

# 对于爬虫，一般是要提取某个操作执行结束以后，加载出来的网页的源码
# 提取浏览器执行完以后的得到的html源码
html = driver.page_source
with open("test.html",'w',encoding="utf-8") as fp:
    fp.write(html)

# 关掉浏览器
driver.quit()