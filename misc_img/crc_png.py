# -*- coding:utf8 -*-
"""
根据crc32值，爆破png图片宽高
"""
import binascii
import struct

crcbp = open("img.png", "rb").read()  # 打开图片
crc32frombp = int(crcbp[29:33].hex(), 16)  # 读取图片中的CRC校验值
print(crc32frombp)

for i in range(4000):  # 宽度1-4000进行枚举
    for j in range(4000):  # 高度1-4000进行枚举
        data = crcbp[12:16] + \
               struct.pack('>i', i) + struct.pack('>i', j) + crcbp[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        # print(crc32)
        if crc32 == crc32frombp:  # 计算当图片大小为i:j时的CRC校验值，与图片中的CRC比较，当相同，则图片大小已经确定
            print(i, j)
            print('hex:', hex(i), hex(j))
            exit(0)
