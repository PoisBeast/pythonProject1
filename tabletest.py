import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
import requests


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()
        self.web_browser = QWebEngineView()
        # self.web_browser.load(QUrl('https://pan.baidu.com/s/17XlMuMzfQhwJ5R1Bn7yuiA#list/path=%2F'))
        btn = QPushButton('加载脚本')
        layout.addWidget(btn)
        layout.addWidget(self.web_browser)
        self.setLayout(layout)
        # self.web_browser.page().profile().cookieStore().deleteAllCookies()
        self.web_browser.load(QUrl('https://fp.jss.com.cn/#/platform/make?clientopenned=true'))
        btn.clicked.connect(self.add_script)
        # self.web_browser.loadFinished.connect(self.add_script)

    def add_script(self):
        print('按钮已被点击')
        # runJs = '''
        #             function getCookie(){return document.cookie}
        #             getCookie();
        #             '''
        # runjss = '''
        #             document.
        #         '''
        # self.web_browser.page().runJavaScript(runjss, self.getHeadersByJs)
        # self.web_browser.page().runJavaScript(runJs, self.getCookieByJs)
 #宁波知马国际物流有限公司
        self.web_browser.page().toPlainText(lambda x: print(x))
        self.web_browser.page().toHtml(lambda x: print(x))
        self.web_browser.page().runJavaScript('''function getname(){
        document.querySelector("#invoice-make-inner > tbody > tr > td:nth-child(2) > div:nth-child(1) > span > i").click();
        setTimeout(() => {document.querySelector("#searchName").value="宁波知马国际物流有限公司"}, 100);
        setTimeout(() => {document.querySelector("#standard-table > div > div > div > div > div > div > div.ant-table-body > table > tbody > tr:nth-child(1) > td:nth-child(3) > a").click()}, 200);
        setTimeout(() => {document.querySelector("#invoice-body > div.invoice-inner_1Z0ha > div.ant-table-wrapper.content_16ZIR > div > div > div > div > div.ant-table-body > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > div > div > div > ul > li > div > input").click()}, 350);
        setTimeout(() => {document.querySelector("#invoice-body > div.invoice-inner_1Z0ha > div.ant-table-wrapper.content_16ZIR > div > div > div > div > div.ant-table-body > table > tbody > tr.ant-table-row.s-crt.ant-table-row-level-0 > td:nth-child(2) > div > i").click()}, 400);
        setTimeout(() => {document.querySelector("#standard-table > div > div > div > div > div > div > div.ant-table-body > table > tbody > tr:nth-child(1) > td:nth-child(8) > a").click()}, 550);
        };
        getname();''')

    def getCookieRunJs(self):
        runJs = '''
            function getCookie(){return document.cookie}
            getCookie();
            '''
        self.web_browser.page().runJavaScript(runJs, self.getCookieByJs)
        runjss='''
            function getHeaders(){var req = new XMLHttpRequest();
            req.open('GET', document.location.href, false);
            req.send(null);
            var headerArr = req.getAllResponseHeaders().split('\n');
            var headers = {};
            headerArr.forEach(item=>{
            if(item!==''){
            var index = item.indexOf(':');
            var key = item.slice(0,index);
            var value = item.slice(index+1).trim();
            headers[key] = value
            }})return headers}
            getHeaders();
        '''
        self.web_browser.page().runJavaScript(runjss, self.getHeadersByJs)

    def getHeadersByJs(self, result):
        print(result)

    def getCookieByJs(self, result):
        print(result)
        # url = 'https://fp.jss.com.cn/api/invoice/corpInvoice/qurryBuyerInfo.do?_=1656314570903&paramName=%E5%AE%81%E6%B3%A2%E7%9F%A5%E9%A9%AC%E5%9B%BD%E9%99%85%E7%89%A9%E6%B5%81%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8'
        # headers = {
        #     'Cookie': result
        # }
        # print(headers)
        # html = requests.get(url, headers=headers, timeout=5).text
        # print(html)
        # 打印这个的这个result就是cookie了


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
