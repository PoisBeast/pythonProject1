import requests
import re

url = "https://u.jss.com.cn/usercenter/userlogin/allow/check.do?m=0.865331691075681"#需要爬取图片的网页地址
a = requests.get(url)#得到网页源码
#print(page)
#print(reg)
f = open("img.jpg", 'wb')#以二进制格式写入img文件夹中
f.write(a.content)
f.close()
print("第%s张图片下载完毕")

