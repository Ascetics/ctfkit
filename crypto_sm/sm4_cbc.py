from gmssl import sm4


# PKCS7 填充
def pkcs7_pad(data: bytes, block_size: int = 16) -> bytes:
    pad_len = block_size - len(data) % block_size
    return data + bytes([pad_len] * pad_len)


def pkcs7_unpad(data: bytes) -> bytes:
    pad_len = data[-1]
    return data[:-pad_len]


key = bytes.fromhex('0123456789abcdeffedcba9876543210')
iv = bytes.fromhex('000102030405060708090a0b0c0d0e0f')

crypt_sm4 = sm4.CryptSM4()

# 加密
crypt_sm4.set_key(key, sm4.SM4_ENCRYPT)
padded_data = pkcs7_pad(b"Hello SM4 CBC Mode")
enc_data = crypt_sm4.crypt_cbc(iv, padded_data)
print("CBC 加密结果(hex):", enc_data.hex())

# 解密
crypt_sm4.set_key(key, sm4.SM4_DECRYPT)
dec_padded = crypt_sm4.crypt_cbc(iv, enc_data)
dec_data = pkcs7_unpad(dec_padded)
print("CBC 解密结果:", dec_data.decode())
