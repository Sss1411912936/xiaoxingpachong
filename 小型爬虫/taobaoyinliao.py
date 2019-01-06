from urllib import request
from lxml import etree
import os
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# 处理url
def handle_request(url,page):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    return request.Request(url=url,headers=headers)#给请求加上请求头，更能方便的不被认别出是爬虫
# 请求
def request_data(req):
    print(request.urlopen(req).read().decode("gbk"))
    return request.urlopen(req).read().decode("gbk")#通过utf-8的格式读出网页的内容，打印这句话应该是整个网页的html

# 解析
def anylasis_data(html):
    # 把html字符串转化为etree结构
    html_tree = etree.HTML(html)#换成etree的结构，适应xpath去介休
    # 提取html中的图片的链接
    #//*[@id="J_Itemlist_Pic_550472066896"]
    # img_list = html_tree.xpath("//div[@id='solist']/dl//img/@src")#通过检查网页找出要爬图片的xpath路径
    # img_list = html_tree.xpath("//div[@class='item J_MouserOnverReq  ']//div[@class='pic']//img/@src")#通过检查网页找出要爬图片的xpath路径
    img_list = html_tree.xpath("//div[@class='item J_MouserOnverReq  ']//div[@class='pic']//img/@src")#通过检查网页找出要爬图片的xpath路径
    print(img_list)
    return img_list

#https://s.taobao.com/search?q=%E9%A5%AE%E6%96%99%E7%93%B6&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190105&ie=utf8&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44
#https://s.taobao.com/search?q=%E9%A5%AE%E6%96%99%E7%93%B6&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190105&ie=utf8&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s=88
#https://s.taobao.com/search?q=%E9%A5%AE%E6%96%99%E7%93%B6&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190105&ie=utf8&bcoffset=-3&ntoffset=-3&p4ppushleft=1%2C48&s=132
# 下载图片
def download_imgs(img_list):
    # 遍历img_list
    for img in img_list:
        suffix = os.path.splitext(img)[-1]#通过os模块分割图片的地址把后缀解析出来
        print(suffix)#看一看后缀名，若不是.jpg可能带有反爬策略
        # 提取图片名字
        img_name = os.path.splitext(img)[0].split("/")[-1]#通过os模块分析出图片的名字
        # 拼接图片存储路径
        filename = "/Users/sunfn/Desktop/小型爬虫/sucai/" + img_name + suffix
        # 下载
        print("正在下载：",img)
        request.urlretrieve(url=img,filename=filename)#通过urlretrieve下载图片，url是图片的路径，filename是图片要存储的路径
        exit()
        # 每下载一次，就休眠一下
        time.sleep(0.2)


# 定义一个main函数
def main():
    firsturl = "https://s.taobao.com/search?q=%E9%A5%AE%E6%96%99%E7%93%B6&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190105&ie=utf8&bs=132&s="
    # url = "http://so.redocn.com/yinliao/d2fbc1cfc6bf.htm"
    a = input("您想从第几页开始呢？")
    b = input("你想爬到第几页呢")
    for i in range(int(a),int(b)):
        urlnum = (i-1)*44
        url = firsturl + str(urlnum)
        print(url)
        print("开始下载...")
        req = handle_request(url=url,page=0)
        res = request_data(req)
        img_list = anylasis_data(res)
        download_imgs(img_list)
        print("over")



if __name__ == '__main__':
    main()



