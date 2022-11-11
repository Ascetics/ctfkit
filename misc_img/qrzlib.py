# -*- coding:utf8 -*-
"""
png格式 IDAT块写满65524 byte才会写下一个IDAT
发现没写满65524 byte就写下一个块的肯定有问题

IDAT块以0x789C开头，那么是zlib压缩的，可以解压缩获取信息
"""

import zlib
import binascii

# 字符串转二进制字节流
# 再用zlib解压得到ascii字符编码的字节流

IDAT = ('789C5D91011280400802BF04FFFF5C75294B5537738A21A27D1E49CFD17DB3937A92E7'
        'E603880A6D485100901FB0410153350DE83112EA2D51C54CE2E585B15A2FC78E8872F5'
        '1C6FC1881882F93D372DEF78E665B0C36C529622A0A45588138833A170A2071DDCD182'
        '19DB8C0D465D8B6989719645ED9C11C36AE3ABDAEFCFC0ACF023E77C17C7897667')
IDAT = bytes.fromhex(IDAT)
result = binascii.hexlify(zlib.decompress(IDAT))

# 再转成字符串,字符串以hex方式出现，在转成ascii字符
# 得到625个01编码，形成二维码

s = result.decode('utf-8')
print(s)
print(len(s))
r = ''
for i in range(len(s) // 2):
    r += chr(int(s[2 * i:2 * i + 2], base=16))
print(r)


