import re
import time

import requests
from bs4 import BeautifulSoup

from get_comment import SQL
from get_comment import getprice

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                          ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}

for i in range(1, 21168, 2):
    sss = SQL.save_mysql()
    link = sss.read_link(i)
    try:
        for row in link:
            url1 = row[0]
            print(url1)
            phone_id = url1.split('/')[-1].strip(".html")
            # phone_id = re.findall(r"\d+", url1)
            print(phone_id)
            url = "http:"+url1
            print(url)
            price = getprice.jd_price(url)
            if price == KeyError:
                price = 0
            content = requests.get(url, headers=headers)
            html = content.text
            #print html
            soup = BeautifulSoup(html, 'lxml')
            title = re.findall(r'<title>(.*?)</title>', html)
            name = title[0]
            print(name)
            num = getprice.get_comment_num(phone_id)
            print(num)
            print('id:'+phone_id[0])
            sss.save_comment(i, name, price, num, phone_id)
            content.close()
            time.sleep(0.1)
    except:
        print("Error: 读取失败")
    else:
        print("内容成功写入数据库")
