# coding:utf8
import matplotlib.pyplot as plt
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh.sorting import FieldFacet

from analysis import phone_analysis1

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def create_index(tup, ix):
    writer = ix.writer()
    print(tup[0], tup[1], tup[2])
    # print(type(tup[0]))
    writer.add_document(phone_name=str(tup[0]), price=int(tup[1]), phoneid=str(tup[2]))
    print("建立完成一个索引")
    writer.commit()


def search1(name):
    new_list = []
    index = open_dir("F:\\PythonFile\\JD_spider\\search\\index", indexname='comment')
    with index.searcher() as searcher:
        parser = QueryParser("phone_name", index.schema)
        myquery = parser.parse(name)
        facet = FieldFacet("price", reverse=True)
        results = searcher.search(myquery, limit=None, sortedby=facet)
        # print(list(results))
        for result1 in results:
            # print(dict(result1))
            new_list.append(dict(result1))
        return new_list


def search():
    print("请输入查询的名称：")
    # name = str(input())
    name = str(input())
    newlist = search1(name)
    return newlist


if __name__ == "__main__":
    # mysql = SQL.save_mysql()
    # tup = mysql.select_phone_info()
    # analyser = ChineseAnalyzer()
    # schema = Schema(phone_name=TEXT(stored=True, analyzer=analyser), price=NUMERIC(stored=True),
    #                 phoneid=ID(stored=True))
    # ix = create_in("E:\\PythonFile\\JD_spider\\search\\index", schema=schema, indexname='comment')
    # for i in range(0,len(tup)):
    #     create_index(tup[i],ix)
    # print("建立索引完毕！")
    dic1 = phone_analysis1.get_result()
    while 1:
        new_list = search()
        # print(new_list)
        for dic in new_list:
            # print(dic['phoneid'])
            if dic['phoneid'] in dic1:
                print(dic['phone_name'])
                print(dic1[dic['phoneid']])
