# -*- coding:utf8 -*-
"""
BUUCTF 丢失的MD5
已知一部分明文和一部分MD5密文
暴力破解出明文密文
"""
import hashlib

for i in range(32, 127):
    for j in range(32, 127):
        for k in range(32, 127):
            m = hashlib.md5()
            m.update(('TASC' + chr(i) + 'O3RJMV' + chr(j) + 'WDJKX' + chr(
                k) + 'ZM').encode('utf-8'))
            des = m.hexdigest()
            if 'e9032' in des and 'da' in des and '911513' in des:
                print(des)
