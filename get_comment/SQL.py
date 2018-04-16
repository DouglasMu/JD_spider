# coding:utf-8
import pymysql


# 将得到的数据存入数据库中mysql
class save_mysql:
    def __init__(self):
        self.user = 'root'
        self.password = 'admin'
        self.host = 'localhost'
        self.database = 'jd_netbook'

    def save_link(self, i, url):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db=self.database, charset="utf8")
        cursor = conn.cursor()
        sql = "insert into netbook_url(id, url) values(%s ,%s)"
        cursor.execute(sql, (i, url))   #url插入到数据库中
        conn.commit()
        conn.close()

    def save_comment(self, pid, name, price, pinglunnum, phone_id):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db="jd", charset="utf8")
        cursor = conn.cursor()
        cursor.execute("insert into phone_info(id, phone_name, price, comment_num, phone_id) "
                       "values(%s ,%s ,%s ,%s ,%s)"% (pid, name, price, pinglunnum, phone_id))  # 插入到数据库中
        conn.commit()
        conn.close()

    def read_link(self, phoneid):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db="jd", charset="utf8")
        cursor = conn.cursor()
        cursor.execute("select url from phone_url where id = %s" % phoneid)
        link = cursor.fetchall()
        conn.close()
        return link
        # return re.search('//item(.)*\.html', link, flags=0)

    def read_phone_info(self, phoneid):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db="jd", charset="utf8")
        cursor = conn.cursor()
        cursor.execute("select comment_num from phone_info where id = %s" % phoneid)
        nums = cursor.fetchone()
        for num in nums:
            if num > 10000:
                cursor.execute("select phone_id from phone_info where id = %s" % phoneid)
                # print("select phone_id from phone_info where id = %s", phoneid)
                phone_ids = cursor.fetchone()
                # print(phone_ids[0])
                return phone_ids[0]
            else:
                return 0
        conn.close()

    def save_comments1(self, phone_id):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db="jd", charset="utf8")
        cursor = conn.cursor()
        sql = "create table phone_%s" \
              "(id BIGINT  ,phone_id BIGINT,name VARCHAR(255),comment_time VARCHAR(255)," \
              "content text)" % phone_id
        # print(sql)
        cursor.execute(sql)
        conn.close()

    def save_comments2(self, ids, phone_id, product_name, comment_time, content):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db="jd", charset="utf8")
        cursor = conn.cursor()
        sql ="insert into phone_%s(id, phone_id, name,comment_time,content) VALUE(%s, %s, %s, %s, %s)"
        cursor.execute(sql, (phone_id, ids, phone_id, product_name, comment_time, content))
        conn.commit()
        conn.close()

    def save_error(self, error_id, error_type):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db="jd", charset="utf8")
        cursor = conn.cursor()
        sql = "insert into error_table(id,type) VALUE(%s, %s)"
        cursor.execute(sql, (error_id, error_type))
        conn.commit()
        conn.close()

    def read_comment_phone(self, phone_id, i):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db="jd", charset="utf8")
        cursor = conn.cursor()
        sql = "SELECT content FROM phone_%s WHERE id =%s"
        cursor.execute(sql, (phone_id, i))
        comment = cursor.fetchall()
        conn.close()
        return comment

    def select_all_table(self, databast_name):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db="jd", charset="utf8")
        cursor = conn.cursor()
        sql = "select table_name from information_schema.tables " \
              "where table_schema=%s"
        cursor.execute(sql, databast_name)
        table_list = cursor.fetchall()
        conn.close()
        return table_list

    def select_phone_info(self):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db="jd", charset="utf8")
        cursor = conn.cursor()
        sql = "SELECT phone_name,price,phone_id FROM phone_info "
        cursor.execute(sql)
        phone_info = cursor.fetchall()
        conn.close()
        return phone_info
