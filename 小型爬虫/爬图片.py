from urllib import request
from lxml import etree
import os
import time


# 处理url
def Request_request(url, page):
    ​headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
​    if page == 1:
        page_url = url + ".html"
​   else:
        page_url = url + "_" + str(page) + ".html"
​    print(page_url)
​    return request.Request(url=page_url, headers=headers)


# 请求
def request_data(req):
    ​    return request.urlopen(req).read().decode("utf-8")


# 解析
def anylasis_data(html):
    ​  # 把html转换成
    ​    html_tree = etree.HTML(html)
    ​    imgs = html_tree.xpath("//div[starts-with(@class,'box')]//img/@src2")
    ​    return imgs

    def download_img(img_list):
        ​  # 遍历img_list
        ​    for img in img_list:
            ​  # 提取后缀
            ​        suffix = os.path.splitext(img)[-1]
            ​  # 提取图片名字
            ​        img_name = os.path.splitext(img)[0].split("/")[-1]
            ​  # 拼接图片路径
            ​        filename = "./sucai/" + img_name + suffix
            ​  # 下载
            ​        print("正在下载")
            ​        request.urlretrieve(url=img, filename=filename)
            ​        time.sleep(0.1)

            # 定义一个main函数
            def main():

                ​    url = "http://sc.chinaz.com/tag_tupian/YaZhou"

            ​    start = input("请输入起始页:")
            ​    end = input("请输入终止页:")
            ​    print("开始下载")
            ​    for i in range(int(start), int(end) + 1):
                ​  # 处理url
                ​        req = Request_request(url=url, page=i)
                ​  # 请求
                ​        res = request_data(req)
                ​  # print(res)
                ​  # 解析
                ​        data = anylasis_data(res)
                ​  # 处理解析结果（下载图片）
                ​        download_img(data)
                if __name__ == '__main__':
                    ​    main()
