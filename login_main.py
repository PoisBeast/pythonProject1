# self.pushButton.setShortcut(_translate("MainWindow", "enter")) #设置快捷键
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap, QKeyEvent

from PyQt5.QtWidgets import QMessageBox
import login_ui
import test_designed
from PyQt5.QtCore import Qt


class login_window(QtWidgets.QMainWindow, login_ui.LoginForm):
    def __init__(self):
        super(login_window, self).__init__()
        self.init()
        self.admin = "帅哥"
        self.Password = "000"

    def init(self):

        self.initUI()  # 创建窗体对象
        self.btn_login.clicked.connect(self.login_button)  # 连接槽

    def login_button(self):
        if self.login_ui.LoginForm.led_workerid.text() == "":
            QMessageBox.warning(self, '警告', '密码不能为空，请输入！')
            return None

        # if  self.password == self.lineEdit.text():
        if (self.login_ui.LoginForm.led_pwd.text() == self.Password) and self.login_ui.LoginForm.led_workerid.text() == self.admin:
            # Ui_Main = Open_Camera()  # 生成主窗口的实例
            # 1打开新窗口

            Ui_Main.setupUi(MainWindow)
            MainWindow.show()
            # 2关闭本窗口
            self.close()
        else:
            QMessageBox.critical(self, '错误', '密码错误！')
            self.lineEdit.clear()
            return None


if __name__ == '__main__':
    from PyQt5 import QtCore

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应分辨率

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    window = login_window()
    Ui_Main = test_designed.Ui_mytest()  # 生成主窗口的实例
    window.show()

    sys.exit(app.exec_())