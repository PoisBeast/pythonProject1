#!/usr/bin/python3


import pymssql  # 引入pymssql模块


def conn():
    connect = pymssql.connect('47.98.176.103', 'sa', 'QAZwsx123!@#', 'CnYiu_HDTFBA')  # 服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
    return connect


if __name__ == '__main__':
    conn = conn()