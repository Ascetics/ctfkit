# -*- coding:utf8 -*-
"""
png格式 IDAT块写满65524 byte才会写下一个IDAT
发现没写满65524 byte就写下一个块的肯定有问题

IDAT块以0x789C开头，那么是zlib压缩的，可以解压缩获取信息

binwalk -e zlib_decompress_221B.png 可以看到如下内容
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 2856 x 4284, 8-bit/color RGB, non-interlaced
62            0x3E            Zlib compressed data, compressed
7693403       0x75645B        Zlib compressed data, default compression
--------------------------------------------------------------------------------
正常来说，不会出现 7693403       0x75645B        Zlib compressed data, default compression
说明0x75645B字节开始有zlib压缩内容
"""

import zlib

with open('zlib_decompress_221B.png', 'rb') as f:
    fdata = f.read()
    data = fdata[0x75645B:]
    s = zlib.decompress(data)
    print(s)
