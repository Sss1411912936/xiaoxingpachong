from urllib import request,parse
from time import  sleep
from lxml import  etree
def Request_request(url,page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
    print(url)
    return request.Request(headers=headers,url=url)
def request_data(req):
    res = request.urlopen(req)
    return res.read().decode("utf-8")
def anylsis_html(data):
    html_tree = etree.HTML(data)
    pat = html_tree.xpath("//img/@src2")
    return  pat
def main():
    url = "http://sc.chinaz.com/tupian/hunsha"
    start = input("请输入起始页：")
    end = input("请输入终止页:")
    print("正在下载。。。")
    img_name =1
    for i in range(int(start),int(end)+1):
        if i == 1:
            aurl = url+".html"
            req = Request_request(url=aurl,page=i)
        else:
            burl = url+"_"+str(i)+".html"
            req = Request_request(url=burl,page=i)
        res = request_data(req)
        data = anylsis_html(res)
        print(data)
        for img in data:
            print("当前正在下载："+str(img))
            request.urlretrieve(url=img,filename="./pic/"+str(img_name)+".jpg")
            img_name +=1
            sleep(0.1)
            print("下载完毕")

if __name__ == '__main__':
    main()