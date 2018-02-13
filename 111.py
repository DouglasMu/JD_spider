import requests
from bs4 import BeautifulSoup
import SQL
import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
i = 1
for n in range(1, 169):
    url = ("https://list.jd.com/list.html?cat=9987,653,655&page=%s" % n)
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
            time.sleep(0.1)
    res.close()
    print("page%s" % n)
    print("___________________________________________________________")
