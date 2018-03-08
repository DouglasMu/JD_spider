import time

import requests
from bs4 import BeautifulSoup

from get_comment import SQL

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;'
                         ' Win64; x64) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
i = 121339
phone_urls = "https://list.jd.com/list.html?cat=9987,653,655&page=%s"
netbook_urls = "https://list.jd.com/list.html?cat=670,671,672&page=%s"

for n in range(963, 1104):
    url = (netbook_urls % n)
    print(url)
    res = requests.get(url, headers=headers)
    html = res.text
    #print html
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.findAll('a', target="_blank")
    for div in divs:
        link = div.get('href')
        print(link)
        if "//item.jd.com/" in link:
            sss = SQL.save_mysql()
            sss.save_link(i, link)
            i = i+1

    res.close()
    time.sleep(1)
    print("page%s" % n)
    print("___________________________________________________________")
