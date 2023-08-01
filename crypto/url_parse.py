# -*- coding:utf-8 -*-
"""
BUUCTF Crypto Url编码题目
Url parse
"""
from urllib.parse import quote, unquote

c = r'%66%6c%61%67%7b%61%6e%64%20%31%3d%31%7d'
m = unquote(c, encoding='utf-8')
print(m)

c2 = quote(m, encoding='utf-8')
print(c2)
