# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-01 15:54
@Auth ： 小胡
@File ：con_db.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''封装数据库操作'''
import pymysql
class Con_DB:
    def __init__(self,host,user,password,database,port=3306,charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            #连接数据库
            self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,\
                                        password=self.password,database=self.database,charset=self.charset)
        except Exception as err:
            print('数据库连接失败，请检查参数是否正确。',str(err))
        else:
            #如果连接成功，创建游标
            self.cursor = self.conn.cursor()

    def dml(self,*sql):
        "执行mysql增删改的操作"
        try:
            for i in sql:
                self.cursor.execute(i)
            print('影响行数：',self.conn.affected_rows())
        except Exception as err:
            print('SQL语句执行失败，请检查！',str(err))
            self.conn.rollback()
        else:
            self.conn.commit()
    def select_one(self,sql):
        "查询一条结果"
        try:
            self.cursor.execute(sql)
            print('影响行数：',self.conn.affected_rows())
            return self.cursor.fetchone()
        except Exception as err:
            print('查询失败，请检查语句是否错误！',str(err))
    def select_many(self,sql,rownumber_num,number):
        "查询多条结果"
        try:
            self.cursor.execute(sql)
            # 设置游标的位置
            self.cursor.rownumber = rownumber_num
            return self.cursor.fetchmany(number)
        except Exception as err:
            print('查询失败，请检查语句是否错误！', str(err))
    def select_all(self,sql):
        "查询所有结果"
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as err:
            print('查询失败，请检查语句是否错误！', str(err))
    def exist_data(self,sql):
        '''
        查询后，是否存在数据
        :return:
        '''
        self.cursor.execute(sql)
        if self.cursor.fetchone():
            return True
        else:
            return False
    def __del__(self):
        self.conn.close()
        # print('数据库连接被关闭')
        # print(self.conn.close)
if __name__ == '__main__':
    db = Con_DB('127.0.0.1','root','123456','test')
    print(db.select_one('select * from class_room where class_id=1;'))
    print(db.select_all('select * from class_room;'))
    print(db.select_many('select * from class_room;',1,2))
    # db.dml('insert into class_room values(4,"c语言","c语言班",4000),(5,"c++语言","c++语言班",4000);')
    # db.dml("update class_room set price = price+1000 where class_id=4;")
    # db.dml("delete from class_room where class_id=4;")
