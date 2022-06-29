# coding=utf-8
import pymssql

class SQLServer:
    def __init__(self,server,user,password,database):
    # 类的构造函数，初始化DBC连接信息
        self.server = server
        self.user = user
        self.password = password
        self.database = database

    def __GetConnect(self):
    # 得到数据库连接信息，返回conn.cursor()
        if not self.database:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(server=self.server,user=self.user,password=self.password,database=self.database)
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")  # 将DBC信息赋值给cur
        else:
            return cur

    def ExecQuery(self,sql):
        '''
        执行查询语句
        返回一个包含tuple的list，list是元素的记录行，tuple记录每行的字段数值
        '''
        cur = self.__GetConnect()
        cur.execute(sql) # 执行查询语句
        result = cur.fetchall() # fetchall()获取查询结果
        # 查询完毕关闭数据库连接
        self.conn.close()
        return result

    def ExecQuerys(self,sql):
        '''
        执行查询语句
        返回一个包含tuple的list，list是元素的记录行，tuple记录每行的字段数值
        '''
        cur = self.__GetConnect()
        cur.execute(sql) # 执行查询语句
        result = cur.fetchall() # fetchall()获取查询结果
        # 查询完毕关闭数据库连接
        self.conn.close()
        return result

def main(starDate,endDate):
    msg = SQLServer(server="47.98.176.103", user="sa", password="QAZwsx123!@#", database="CnYiu_HDTFBA")
    if len(starDate)>5 and len(endDate)>5:
        result = msg.ExecQuery(
            "SELECT wlhmc,fph,fprq,sjje,fpbz,fpid FROM kpfp WHERE ysyf = '应收'" + " and fprq >= " + starDate + " and fprq <= " + endDate+"")
    else:
        result = msg.ExecQuery("SELECT  column_name  FROM  information_schema.columns  WHERE  table_name = 'kpfp'")
    return result
    # result = msg.ExecQuery("select TOP 2 * from kpyf where fpid='20200924203319330' and ysyf='应收'")
    # for (Value) in result:
    #     print(Value)

def mains(content):
    msg = SQLServer(server="47.98.176.103", user="sa", password="QAZwsx123!@#", database="CnYiu_HDTFBA")
    if len(content)>1:
        result = msg.ExecQuery("SELECT fymc,bz,jg,sl,wlhmc FROM  kpyf WHERE ysyf = '应收' and fpid = "+content+"")
    else:
        result = msg.ExecQuery("SELECT  column_name  FROM  information_schema.columns  WHERE  table_name = 'kpfp'")
    return result
