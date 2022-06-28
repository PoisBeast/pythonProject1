import requests
url = 'https://fp.jss.com.cn/api/invoice/corpInvoice/qurryBuyerInfo.do?_=1656314570903&paramName=%E5%AE%81%E6%B3%A2%E7%9F%A5%E9%A9%AC%E5%9B%BD%E9%99%85%E7%89%A9%E6%B5%81%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8'
headers = {
'Cookie': 'Hm_lvt_09d3edd3a5752419698c3749f739a285=1656384198,1656385212,1656385561,1656385747; makeMenuClick=true; Hm_lpvt_09d3edd3a5752419698c3749f739a285=1656385747'
}
html = requests.get(url,headers=headers,timeout=5).text
print(html)