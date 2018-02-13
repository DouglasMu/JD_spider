# coding:utf-8

import requests
from bs4 import BeautifulSoup
import threading
from SQL import save_mysql  # 导入sql存储数据


class spiders:
    def __init__(self, page):
        self.url = 'https://list.jd.com/list.html?cat=9987,653,655&page=' + str(
            page)
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
        self.search_urls = 'https://list.jd.com/list.html?cat=9987,653,655&page=1'
        self.pids = set()
        self.phone_urls = set()  # 得到的所有手机的url
        self.search_page = page + 1  # 翻页的作用
        self.sql = save_mysql()  # 数据库保存

    # 得到每一页的网页源码
    def get_html(self):
        res = requests.get(self.url, headers=self.headers)
        html = res.text
        print (html)
        return html

    def get_src_data(self):
        html = self.get_html()
        soup = BeautifulSoup(html, 'lxml')
        # plist > ul > li:nth-child(1) > div > div.p-img > a
        divs = soup.select(' ul.gl-warp clearfix > li > div > div.p-img > a')
        for div in divs:
            link = div.get('href')
            print (link)
            self.save_mysql.save_link(link)

        print ("--------------------------------------------------")

    def main(self):
        self.get_src_data()
        print( "------------------------------------------------------------------------------------")


if __name__ == '__main__':
    threads = []
    for i in range(1, 10):
        page = i + 1
        t = threading.Thread(target=spiders(page).main, args=[])
        threads.append(t)
    for t in threads:
        t.start()
        t.join()
    print ("end")

