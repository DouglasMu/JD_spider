import jieba.posseg as pseg
import analysis.phone_analysis as ap
txt = ap.get_comments(1552946,1)
print(txt)
words = dict(pseg.cut(txt))
# print(type(words))
# print(words)
for key,value in words.items():
    print(key,value)
with open("E:\\PythonFile\\test.txt",'a') as file:
    file.write(str(words))
fr = open("E:\\PythonFile\\test.txt",'r+')
dic = eval(fr.read())   #  读取的str转换为字典
print(dic)
fr.close()