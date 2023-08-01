# -*- coding:utf8 -*-
"""
BUUCTF Crypto Quoted-printable题目
Quote-Printable 编码解析
"""
import quopri

c = '=E9=82=A3=E4=BD=A0=E4=B9=9F=E5=BE=88=E6=A3=92=E5=93=A6'
m = quopri.decodestring(c.encode('utf-8')).decode('utf-8')
print(m)

c2 = quopri.encodestring(m.encode('utf-8')).decode('utf-8')
print(c2)
