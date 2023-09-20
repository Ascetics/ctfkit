import base64
from Crypto.Cipher import AES
from Crypto import Random
import os
import base64
import json

"""
1、密钥处理

直接处理密钥会报错：‘AES key must be either 16, 24, or 32 bytes long’
因为AES接收的key&vi都必须是有固定长度。
对Key 进行填充至符合规格。
"""


def add_to_16(text):
    while len(text) % 16 != 0:
        text += '\0'
    return (text)


key = 'Fcniggersm'
key = add_to_16(key)

"""
2、密文处理

有可能处理密文时候会报错：'Error: Incorrect padding'
这是因为密文长度不符合规格，对base64解码的string补齐等号就可以了
"""


def decode_base64(data):
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    return (data)


message = 'gYknrv3zMWYXEpRLDL0n8q+6s68DKapAfRpBDhN1XGM='
encrypt_data = message
encrypt_data = decode_base64(encrypt_data)

"""
3、解密处理

解密成功获取到a，再对a进行解码处理获取数据。
"""


# encoding:utf-8

def encrypt(data, password):
    bs = AES.block_size
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    cipher = AES.new(password.encode('utf-8'), AES.MODE_ECB)
    data = cipher.encrypt(pad(data).encode('utf-8'))
    return (data)


if __name__ == '__main__':
    data = 'ni hao'
    password = 'aesrsasec'  # 16,24,32位长的密码
    password = add_to_16(password)
    encrypt_data = encrypt(data, password)
    encrypt_data = base64.b64encode(encrypt_data)
    print('encrypt_data:', encrypt_data)


"""
CBC & ECB相比多出了一个vi（偏移量）。
cipher = AES.new(self.__key, AES.MODE_CBC, iv)
"""

def encrypt(data, password):
    bs = AES.block_size
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    iv = Random.new().read(bs)
    cipher = AES.new(password.encode('utf-8'), AES.MODE_CBC, iv)
    data = cipher.encrypt(pad(data).encode('utf-8'))
    data = iv + data
    return (data)


def decrypt(data, password):
    bs = AES.block_size
    if len(data) <= bs:
        return (data)
    unpad = lambda s: s[0:-ord(s[-1])]
    iv = data[:bs]
    cipher = AES.new(password.encode('utf-8'), AES.MODE_CBC, iv)
    data = unpad(cipher.decrypt(data[bs:]))
    return (data)


if __name__ == '__main__':
    data = 'd437814d9185a290af20514d9341b710'
    password = '78f40f2c57eee727a4be179049cecf89'  # 16,24,32位长的密码
    encrypt_data = encrypt(data, password)
    encrypt_data = base64.b64encode(encrypt_data)
    print('encrypt_data:', encrypt_data)

    encrypt_data = base64.b64decode(encrypt_data)
    decrypt_data = decrypt(encrypt_data, password)
    print('decrypt_data:', decrypt_data)