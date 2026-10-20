import zlib, hashlib
from gmssl import sm3, func

"""
计算商品数据的CSV文件校验码（长度+CRC32+SM3）
flag形式：flag{长度~crc32~SM3}
"""

# 读取文件内容（需要把原始 CSV 内容保存）
with open('products.csv', 'rb') as f:
    data = f.read()

length = len(data)
crc = zlib.crc32(data) & 0xffffffff
sm3_hash = sm3.sm3_hash(func.bytes_to_list(data))

print(length)
print(hex(crc))
print(sm3_hash)
