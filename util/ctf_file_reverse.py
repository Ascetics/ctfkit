"""
文件内容倒置
"""
f1name = '中华人民共和国网络安全法_百度百科.pdf'
f2name = f1name + '.txt'

f1 = open(f1name, 'rb')
f2 = open(f2name, 'wb')

b1 = f1.read()
# print(type(b1))
b2 = b1[::-1]
f2.write(b2)

f1.close()
f2.close()
