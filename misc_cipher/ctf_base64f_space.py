# -*- coding:utf8 -*-
"""
从文件读取字符
base64解码
输出为二进制文件

以2022·福清·比赛 题目为例
"""
import base64

# 读取base64密文
f1 = open('what_is_it.txt', 'r')
c_barr = f1.readline()
# print(c[0:64])
f1.close()

# 解码得到明文，输出文本文件
f2 = open('what_is_it-1.txt', 'w')
m_str = base64.b64decode(c_barr).decode('utf-8')
# print(m[0:64])
f2.writelines(m_str)
f2.close()

# 转为二进制，输出二进制文件

ms = m_str.split(' ')
m_barr = bytearray()
for b in ms:
    i = int(b, base=16)
    m_barr.append(i)
f3 = open('what_is_it.bin', 'wb')
f3.write(m_barr)
f3.close()
