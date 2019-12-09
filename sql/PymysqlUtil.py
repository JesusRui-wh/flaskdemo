# encoding = utf8
import pymysql


# mysql工具类
class PymysqlUtil():
    # 初始化方法
    def __init__(self, host, port, user, passwd, dbName, charsets):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.dbName = dbName
        self.charsets = charsets

    # 链接数据库
    def getCon(self):
        self.db = pymysql.Connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.dbName,
            charset=self.charsets
        )
        self.cursor = self.db.cursor()

    # 关闭链接
    def close(self):
        self.cursor.close()
        self.db.close()

    # 查询单行记录
    def get_one(self, sql):
        res = None
        try:
            self.getCon()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
        except:
            print("查询失败!")
        return res

    # 查询列表数据
    def get_all(self, sql):
        res = None
        try:
            self.getCon()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except:
            print("查询失败！")
        return res

    # 插入, 更新或修改数据
    def oper(self, sql):
        count = 0
        try:
            self.getCon()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print("操作失败！" + sql)
            self.db.rollback()
        return count
