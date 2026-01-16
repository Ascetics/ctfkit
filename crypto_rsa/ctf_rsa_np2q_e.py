import binascii

# 已知参数
N = 4382400036133367223779
e = 23
c = 0x5f6ea1f38716c33d60

# 分解
p = 13574881
q = 23781539

# 计算 φ(N)
phi = p * (p-1) * (q-1)

# 计算 d
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

d = modinv(e, phi)

# 解密
m = pow(c, d, N)
print("解密得到的整数 m =", m)

# 将整数转换为字节串
# 首先将m转换为十六进制字符串，去掉'0x'，然后按每两个字符一组转换为字节
hex_str = hex(m)[2:]  # 去掉'0x'
# 确保长度为偶数
if len(hex_str) % 2 == 1:
    hex_str = '0' + hex_str
bytes_data = bytes.fromhex(hex_str)
print("字节表示:", bytes_data)
print("ASCII 字符串:", bytes_data.decode('ascii'))