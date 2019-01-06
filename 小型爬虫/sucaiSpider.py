from urllib import request
from lxml import etree
import os
import time

# 处理url
def handle_request(url,page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    if page==1:
        page_url = url + ".html"
    else:
        page_url = url + "_" + str(page) + ".html"

    return request.Request(url=page_url,headers=headers)

# 请求
def request_data(req):

    return request.urlopen(req).read().decode("utf-8")

# 解析
def anylasis_data(html):
    # 把html字符串转化为etree结构
    html_tree = etree.HTML(html)
    # 提取html中的图片的链接
    imgs = html_tree.xpath("//div[starts-with(@class,'box')]//img/@src2")
    return imgs

# 下载图片
def download_imgs(img_list):
    # 遍历img_list
    for img in img_list:
        # http://pic1.sc.chinaz.com/Files/pic/pic9/201808/zzpic13564_s.jpg
        # 提取后缀
        suffix = os.path.splitext(img)[-1]
        # 提取图片名字
        img_name = os.path.splitext(img)[0].split("/")[-1]
        # 拼接图片存储路径
        filename = "./sucai/" + img_name + suffix
        # 下载
        print("正在下载：",img)
        request.urlretrieve(url=img,filename=filename)
        # 每下载一次，就休眠一下
        time.sleep(0.2)


# 定义一个main函数
def main():
    url = "http://sc.chinaz.com/tag_tupian/yazhou" # _xx.html
    start = input("请输入起始页：")
    end = input("请输入终止页：")
    print("开始下载...")
    for i in range(int(start),int(end)+1):
        # 处理url
        req = handle_request(url=url,page=i)
        # 请求
        res = request_data(req)
        # print(res)
        # 解析
        data = anylasis_data(res)
        # print(data)
        # 处理解析结果（下载图片）
        download_imgs(data)



if __name__ == '__main__':
    main()



