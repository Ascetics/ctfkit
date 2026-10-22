from gmssl import sm2, func

# 1. 准备十六进制格式的公钥和私钥（64 位十六进制字符串）
# 注意：这里使用示例密钥，生产环境请自行生成并安全保存
private_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
public_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'

# 2. 初始化 SM2 加密对象
sm2_crypt = sm2.CryptSM2(
    public_key=public_key,
    private_key=private_key
)

# 3. 待加密数据（bytes 类型）
data = b"Hello SM2 Encryption"

# 4. 公钥加密
enc_data = sm2_crypt.encrypt(data)
print("加密结果（hex）:", enc_data.hex())

# 5. 私钥解密
dec_data = sm2_crypt.decrypt(enc_data)
print("解密结果:", dec_data.decode())
