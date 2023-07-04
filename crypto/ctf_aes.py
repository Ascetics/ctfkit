# -*- coding:utf8 -*-

'''
AES encode decode
U2Fs is the feature
'''

from Crypto.Cipher import AES

password = b'1234567812345678'  # 秘钥，b就是表示为bytes类型
iv = b'1234567812345678'  # iv偏移量，bytes类型
text = b'abcdefghijklmnhi'  # 需要加密的内容，bytes类型
aes = AES.new(password, AES.MODE_CBC, iv)  # 创建一个aes对象
# AES.MODE_CBC 表示模式是CBC模式
en_text = aes.encrypt(text)
print("密文：", en_text)  # 加密明文，bytes类型
aes = AES.new(password, AES.MODE_CBC, iv)  # CBC模式下解密需要重新创建一个aes对象
den_text = aes.decrypt(en_text)
print("明文：", den_text)
