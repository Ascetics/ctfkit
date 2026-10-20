from gmssl import sm4, func

# 1. 密钥必须是 16 字节（128 位），这里是十六进制字符串（32 个 hex 字符）
key = '0123456789abcdeffedcba9876543210'  # 32 hex chars = 16 bytes
key_bytes = bytes.fromhex(key)

# 2. 初始化 SM4 对象
crypt_sm4 = sm4.CryptSM4()
crypt_sm4.set_key(key_bytes, sm4.SM4_ENCRYPT)  # 加密模式

# 3. 待加密数据（必须按 16 字节分组，不足需填充）
data = b"Hello SM4 Encryption!!!"  # 正好 24 字节，不是 16 的倍数，需要填充
print("原始数据长度:", len(data))


# 4. PKCS7 填充
def pkcs7_pad(data: bytes, block_size: int = 16) -> bytes:
    pad_len = block_size - len(data) % block_size
    return data + bytes([pad_len] * pad_len)


def pkcs7_unpad(data: bytes) -> bytes:
    pad_len = data[-1]
    return data[:-pad_len]


padded_data = pkcs7_pad(data)
print("填充后长度:", len(padded_data))

# 5. 加密
enc_data = crypt_sm4.crypt_ecb(padded_data)
print("加密结果(hex):", enc_data.hex())

# 6. 解密
crypt_sm4.set_key(key_bytes, sm4.SM4_DECRYPT)
dec_padded = crypt_sm4.crypt_ecb(enc_data)
dec_data = pkcs7_unpad(dec_padded)
print("解密结果:", dec_data.decode())

assert dec_data == data
