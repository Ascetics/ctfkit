# -*- coding:utf8 -*-
import base64

# 读取base64密文
f1 = open('把猪困在猪圈里.txt', 'r', encoding='utf-8')
c = f1.read()
f1.close()

# base64解码，查看16个字节有没有magic，发现是JPG图片
m = base64.b64decode(c)
print(m[0:16])

# 输出到二进制文件
f = open('把猪困在猪圈里.jpg', 'wb')
f.write(m)
f.close()
