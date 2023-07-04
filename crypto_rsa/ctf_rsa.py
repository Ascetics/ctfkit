# -*- coding:utf8 -*-
"""
RSA算法的具体描述如下：
（1）任意选取两个不同的大素数p和q，计算n=pq，phi_n=(p-1)(q-1)
（2）任意选取一个大整数e，满足gcd(e, phi_n)=1，整数e用做加密钥（注意：e的选取是很容易的，例如，所有大于p和q的素数都可用）
（3）确定的解密钥d，满足 (de) mod phi_n = 1，即 de = k*phi_n + 1，k是大于等于1的任意整数；所以，若知道e和phi_n，则很容易计算出d
（4）公开整数n和e，秘密保存d
（5）将明文m（m<n是一个整数）加密成密文c，加密算法为 c = m^e mod n
（6）将密文c解密为明文m，解密算法为 m = c^d mod n
"""

import gmpy2
from Crypto.Util.number import long_to_bytes

p = 17
q = 19
e = 23

n = p * q
phi_n = (p - 1) * (q - 1)

d = gmpy2.invert(e, phi_n)
d = int(d)
print('d', d)

m = b'r'
m = int.from_bytes(m, 'big')
c = pow(m, e, n)
m = pow(c, d, n)
# m = m.to_bytes(1, 'big').decode('ascii')
m = long_to_bytes(m).decode('utf-8')
print(m)