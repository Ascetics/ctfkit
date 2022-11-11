# -*- coding:utf8 -*-
"""
读取txt文件，base64转码，输出到二进制文件
"""
import base64

# 读取base64密文
f_src = open('把猪困在猪圈里.txt', 'r', encoding='utf-8')
c_barr = f_src.readline()
f_src.close()

# base64解码，查看16个字节有没有magic
m_barr = base64.b64decode(c_barr)
print(m_barr[0:16])

# 输出到二进制文件
f_dst = open('把猪困在猪圈里.bin', 'wb')
f_dst.write(m_barr)
f_dst.close()
