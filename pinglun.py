# -*- coding: utf-8 -*-
import urllib.request
import json
import time
import random
import SQL


def crawlProductComment(link, pages):
    contents = urllib.request.urlopen(link)
    html = contents.read().decode('gbk')
    jsondata = html[27:-2]
    print(jsondata)
    data = json.loads(jsondata)
    print(data['productCommentSummary']['commentCount'])
    #遍历商品评论列表
    for comment in data['comments']:
        product_name = comment['referenceName']  # 商品名
        comment_time = comment['creationTime']  # 创建时间
        content = comment['content']    # 评论内容

        #输出商品评论关键信息
        print("商品全名:{}".format(product_name))
        print("用户评论时间:{}".format(comment_time))
        print("用户评论内容:{}".format(content))
        print("-----------------------------")

        # '''
        # 数据库操作
        # '''
        # sql = SQL.save_mysql()
        # sql.save_comment()
        #获取数据库链接
        # connection  = pymysql.connect(host='localhost',
        #                           user='root',
        #                           password = '123456',
        #                           db = 'jd',
        #                           charset = 'utf8mb4')
        # try:
        #     # 获取会话指针
        #     with connection.cursor() as cursor:
        #         # 创建sql语句
        #         sql = "insert into `jd-mi6` (`productName`,`commentTime`,`content`) values (%s,%s,%s)"
        #
        #         # 执行sql语句
        #         cursor.execute(sql, (productName, commentTime, content))
        #
        #         # 提交数据库
        #         connection.commit()
        # finally:
        #     connection.close()
    contents.close()


def comment_execute(goods_id):
    for i in range(0, 100):
        print("正在获取第{}页评论数据!".format(i+1))
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv56668&productId='\
              + str(goods_id) + '&score=0&sortType=5&page=' + str(i) + '&pageSize=10&isShadowSku=0&fold=1'
        crawlProductComment(url, i)
        time.sleep(random.randint(31, 33))


if __name__ == "__main__":
    goods = 1968013
    comment_execute(goods)
