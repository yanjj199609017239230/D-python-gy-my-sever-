#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json

import pymysql


class mysql_db():

    def __init__(self,host='localhost',user='root',password='123456',database='practise',port=3306,charset='utf8'):
        self.host=host
        self.user = user
        self.password=password
        self.database=database
        self.port=port
        self.charset=charset
    def connect(self):
        try:
            return pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               password=self.password,
                               database=self.database,
                               charset=self.charset)
        except:
            print("连接数据库失败")
            return None


    def select_execute(self,sql):
        rows = []
        conn = self.connect()
        cur = conn.cursor()
        try:
            if conn:
                cur.execute(sql)
                rows = cur.fetchall()
        except:
            print("查询失败")
        finally:
            conn.close()
        return rows


    def update_execute(self,sql):
        sign=False
        conn = self.connect()
        cur = conn.cursor()
        try:
            if conn:
                cur.execute(sql)
                conn.commit()
                sign = True
        except:
            print("插入数据失败")
            conn.rollback()
        finally:
            conn.close()
        return sign





if __name__=='__main__':
    mydb = mysql_db('192.168.60.132','root','root','mall')
    mydb.update_execute("UPDATE `oms_order` SET STATUS = 1;")
