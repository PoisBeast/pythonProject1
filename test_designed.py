# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_designed.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from datetime import date

import shujjuku2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QDate
from PyQt5.QtWebEngineWidgets import *


class Ui_mytest(object):
    def setupUi(self, mytest):
        mytest.setObjectName("mytest")
        mytest.resize(1187, 870)
        self.groupBox = QtWidgets.QGroupBox(mytest)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 471, 52))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout.addWidget(self.dateEdit_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(mytest)
        self.groupBox_2.setGeometry(QtCore.QRect(480, 10, 485, 52))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_2.addWidget(self.checkBox_4)
        self.pushButton = QtWidgets.QPushButton(mytest)
        self.pushButton.setGeometry(QtCore.QRect(980, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(mytest)
        self.pushButton_2.setGeometry(QtCore.QRect(1070, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_3 = QtWidgets.QGroupBox(mytest)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 360, 1131, 471))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.browser = QWebEngineView(mytest)
        self.browser.setGeometry(QtCore.QRect(10, 360, 1131, 471))
        self.browser.load(QUrl(
            'https://u.jss.com.cn/Contents/usercenter/allow/login/login.jsp?redirecturl=dzfp&jumpurl=tHp1Fp52u91VCWLiYG_MV_yLhBgZbSkTYxFazTnEglTdwzw2TRHzFAUHNYJt_Id8VV8UGVa98upNVH524V9YOg..'))
        self.groupBox_4 = QtWidgets.QGroupBox(mytest)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 70, 1131, 61))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_3.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_3.addWidget(self.lineEdit_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.groupBox_5 = QtWidgets.QGroupBox(mytest)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 140, 1131, 212))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.tableView = QtWidgets.QTableView(self.groupBox_5)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout_4.addWidget(self.tableView)
        self.dateEdit.setEnabled(False)
        self.dateEdit_2.setEnabled(False)
        self.retranslateUi(mytest)
        self.checkBox.toggled['bool'].connect(self.dateEdit.setEnabled)
        self.checkBox_2.toggled['bool'].connect(self.dateEdit_2.setEnabled)
        # self.clicked_button=shujjuku2.main()
        self.pushButton.clicked.connect(self.clickButton)
        self.tableWidget.clicked.connect(self.xxx)
        QtCore.QMetaObject.connectSlotsByName(mytest)
    def xxx(self):
        print("你是煞笔")

    def retranslateUi(self, mytest):
        _translate = QtCore.QCoreApplication.translate
        mytest.setWindowTitle(_translate("mytest", "Dialog"))
        self.groupBox.setTitle(_translate("mytest", "查询"))
        self.label.setText(_translate("mytest", "发票日期"))
        self.label_2.setText(_translate("mytest", "-"))
        self.label_3.setText(_translate("mytest", "往来户"))
        self.checkBox_3.setText(_translate("mytest", "已打印"))
        self.groupBox_2.setTitle(_translate("mytest", "设置"))
        self.label_4.setText(_translate("mytest", "汇率"))
        self.label_5.setText(_translate("mytest", "税率"))
        self.comboBox.setItemText(0, _translate("mytest", "电子发票"))
        self.comboBox.setItemText(1, _translate("mytest", "纸质发票"))
        self.checkBox_4.setText(_translate("mytest", "明细"))
        self.pushButton.setText(_translate("mytest", "查询"))
        self.pushButton_2.setText(_translate("mytest", "开始"))
        self.groupBox_4.setTitle(_translate("mytest", "备注"))
        self.pushButton_3.setText(_translate("mytest", "重置"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mytest", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mytest", "往来户"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mytest", "开票日期"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mytest", "发票金额"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("mytest", "币种"))

    # .year() + "-" + self.dateEdit.date().month() + "-" + self.dateEdit.date().day()
    def clickButton(self):
        if self.checkBox.isChecked():
            self.staryear = self.dateEdit.date().year()
            self.starmonth = self.dateEdit.date().month()
            self.starday = self.dateEdit.date().day()
            starDate = "'"+str(self.staryear) + "-" + str(self.starmonth) + "-" + str(self.starday)+"'"
            #print(self.starDate)
        if self.checkBox_2.isChecked():
            self.endyear = self.dateEdit_2.date().year()
            self.endmonth = self.dateEdit_2.date().month()
            self.endday = self.dateEdit_2.date().day()
            endDate = "'"+str(self.endyear) + "-" + str(self.endmonth) + "-" + str(self.endday)+"'"
            #print(self.endDate)
        shujjuku2.main(starDate, endDate)
