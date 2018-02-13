#coding:utf-8
import pymysql
import re

#将得到的数据存入数据库中mysql
class save_mysql:
    def __init__(self):
        self.user = 'root'
        self.password = 'admin'
        self.host = 'localhost'
        self.database = 'jd'

    def save_link(self, i, url):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db="jd", charset="utf8")
        cursor = conn.cursor()
        cursor.execute("insert into phone_url(id, url) values(%s ,%s)", (i, url))   #url插入到数据库中
        conn.commit()
        conn.close()

    def save_comment(self, pid, name, price, pinglunnum, phone_id):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db="jd", charset="utf8")
        cursor = conn.cursor()
        cursor.execute("insert into phone_info(id, phone_name, price, comment_num, phone_id) "
                       "values(%s ,%s ,%s ,%s ,%s)", (pid, name, price, pinglunnum, phone_id))  # 插入到数据库中
        conn.commit()
        conn.close()

    def read_link(self, phoneid):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db="jd", charset="utf8")
        cursor = conn.cursor()
        cursor.execute("select url from phone_url where id = %s", phoneid)
        link = cursor.fetchall()
        conn.close()
        return link
        #return re.search('//item(.)*\.html', link, flags=0)

