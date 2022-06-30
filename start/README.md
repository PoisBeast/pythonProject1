# MY VERSION GREGORIO HONORATO
# Splash Screen Python PySide2/PyQt5 - MODERN GUI

# pyside安装命令 
pip install pyside6
# 编译qrc文件的命令 
pyside6-rcc src.qrc -o dst.py
# 编译ui文件的命令 
pyside6-uic src.ui -o dst.py
----
# pyqt 安装命令
pip install pyqt5 pyqt5-tools
# 编译qrc文件的命令 
pyrcc5 resource.qrc -o resource.py
# 编译ui文件的命令 
pyuic5 main_window.ui -o main_window.py