import pymysql
from urllib.request import urlretrieve

db = pymysql.connect("47.94.238.129","root","Sun19961206","axf")

cursor = db.cursor()

cursor.execute("select img from products;")

data = cursor.fetchall()

address = '/Users/sunfn/Desktop/tupian99/'


j = 1
print(data)
for i in data:
    address = '/Users/sunfn/Desktop/tupian99/'
    print("正在下载%s"%(address+i[0][:-14]))
    urlretrieve(i[0][:-14],address+str(j)+'.jpg')
    j += 1

db.close()