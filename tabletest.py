import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *


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
        self.web_browser.page().profile().cookieStore().deleteAllCookies()
        self.web_browser.load(QUrl('https://fp.jss.com.cn/#/platform/make?clientopenned=true'))
        btn.clicked.connect(self.add_script)
        # self.web_browser.loadFinished.connect(self.add_script)

    def add_script(self):
        print('按钮已被点击')
        runJs = '''
                    function getCookie(){return document.cookie}
                    getCookie();
                    '''
        self.web_browser.page().runJavaScript(runJs, self.getCookieByJs)

        # self.web_browser.page().toPlainText(lambda x: print(x))
        # self.web_browser.page().toHtml(lambda x: print(x))
        # self.web_browser.page().runJavaScript('''function getname(){
        # document.getElementById("buyername").value="张三";
        # document.getElementById("taxnum").value="张三";
        # document.getElementById("address").value="张三";};
        # getname();''')

    def getCookieRunJs(self):
        runJs = '''
            function getCookie(){return document.cookie}
            getCookie();
            '''
        self.web_browser.page().runJavaScript(runJs, self.getCookieByJs)

    def getCookieByJs(self, result):
        print(result)  # 打印这个的这个result就是cookie了


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
