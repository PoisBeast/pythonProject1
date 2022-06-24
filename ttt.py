from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
client = webdriver.Chrome(chrome_options=chrome_options)  # 驱动路径
client.implicitly_wait(10)
client.get("https://u.jss.com.cn/Contents/usercenter/allow/login/login.jsp?redirecturl=dzfp&jumpurl=tHp1Fp52u91VCWLiYG_MV_yLhBgZbSkTYxFazTnEglTdwzw2TRHzFAUHNYJt_Id8VV8UGVa98upNVH524V9YOg..")  # 要测试网站的地址
content = client.page_source
print(content)
