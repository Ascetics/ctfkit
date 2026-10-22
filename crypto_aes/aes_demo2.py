from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


def encrypt(plain_bytes, key_bytes, iv_bytes):
    cipher = AES.new(key=key_bytes, mode=AES.MODE_CBC, iv=iv_bytes)
    plain_bytes_pad = pad(plain_bytes, AES.block_size)
    crypt_bytes = cipher.encrypt(plain_bytes_pad)
    return crypt_bytes


def decrypt(crypt_bytes, key_bytes, iv_bytes):
    cipher = AES.new(key=key_bytes, mode=AES.MODE_CBC, iv=iv_bytes)
    plain_bytes_pad = cipher.decrypt(crypt_bytes)
    plain_bytes = unpad(plain_bytes_pad, AES.block_size)
    return plain_bytes


if __name__ == '__main__':
    key = '1234567890123456'
    iv = '1234567890123456'
    username = 'admin'
    password = '12345678'
    plain_str = 'username=' + username + '&password=' + password

    key_bytes = key.encode('utf-8')
    iv_bytes = iv.encode('utf-8')
    plain_bytes = plain_str.encode('utf-8')

    # 加密
    crypt_bytes = encrypt(plain_bytes, key_bytes, iv_bytes)
    hex_string = crypt_bytes.hex()
    print(hex_string)

    # 解密
    plain_bytes2 = decrypt(crypt_bytes, key_bytes, iv_bytes)
    plain_str2 = plain_bytes2.decode('utf-8')
    print(plain_str2)
