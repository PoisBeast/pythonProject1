import requests
url = 'https://fp.jss.com.cn/api/invoice/corpInvoice/qurryBuyerInfo.do?_=1656314570903&paramName=%E5%AE%81%E6%B3%A2%E7%9F%A5%E9%A9%AC%E5%9B%BD%E9%99%85%E7%89%A9%E6%B5%81%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8'
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Cookie': 'Hm_lvt_09d3edd3a5752419698c3749f739a285=1656053414,1656309613; SCSESSIONID=2EB78A019C5042229DFD3D93BEB8A869; nuonuo_gray_key=e8474737afd74b8a9dde052811075336; makeMenuClick=true; Hm_lpvt_09d3edd3a5752419698c3749f739a285=1656314562',
#     'Host': 'fp.jss.com.cn',
#     'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
#
# }
headers = {
'Cookie': 'Hm_lvt_09d3edd3a5752419698c3749f739a285=1656053414,1656309613; SCSESSIONID=2EB78A019C5042229DFD3D93BEB8A869; nuonuo_gray_key=e8474737afd74b8a9dde052811075336; makeMenuClick=true; Hm_lpvt_09d3edd3a5752419698c3749f739a285=1656314562'
}
# 网上找的免费代理ip
# proxies = {
#     'http':'http://191.231.62.142:8000',
#     'https':'https://191.231.62.142:8000'
# }
html = requests.get(url,headers=headers,timeout=5).text
print(html)