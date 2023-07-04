"""
希尔密码是运用基本矩阵论原理的替换密码，由Lester S. Hill在1929年发明。

每个字母当作26进制数字：A=0, B=1, C=2... 一串字母当成n维向量，跟一个n×n的矩阵相乘，再将得出的结果模26。
（注意用作加密的矩阵（即密匙）在 必须是可逆的，否则就不可能解码。只有矩阵的行列式和26互质，才是可逆的。）
"""
import numpy as np


def string_to_array(string, size, offset):
    """
    根据加解密矩阵维度，把字符串转换为相应的数字矩阵
    :param string: 待处理的字符串
    :param size: 加解密矩阵维度
    :param offset: 偏移量，参看encode和decode的offset
    :return:
    """
    string = string.upper()
    blocks = [string[i:i + size] for i in range(0, len(string), size)]
    if len(blocks[-1]) != size:  # 补齐成矩阵
        blocks[-1] = blocks[-1].ljust(size, chr(ord('A') - offset))
    arr = np.array([list(map(ord, block)) for block in blocks]) - ord(
        'A') + offset
    return arr


def encode(encryptor, string, offset=0):
    """
    希尔加密
    :param encryptor: 加密矩阵
    :param string: 明文
    :param offset: 默认字母A=0
    :return: 密文
    """
    if encryptor.ndim != 2:
        raise ValueError(f'encryptor ndim is illegal. must be 2.')
    if encryptor.shape[0] != encryptor.shape[1]:
        raise ValueError(f'encryptor shape is illegal. must be square matrix.')
    # assert encryptor.ndim == 2 and encryptor.shape[0] == encryptor.shape[1]

    arr = string_to_array(string, encryptor.shape[0], offset)  # 字符串转数字矩阵
    result = (encryptor @ arr.T).T % 26 + ord('A') - offset  # 算法
    result = ''.join(map(chr, result.ravel()))  # 数字矩阵转字符串
    return result


def decode(decryptor, string, offset=0):
    """
    希尔解密，算法和加密一样
    :param decryptor: 解密矩阵
    :param string: 密文
    :param offset: 默认字母A=0
    :return: 明文
    """
    if decryptor.ndim != 2:
        raise ValueError(f'decryptor ndim is illegal. must be 2.')
    if decryptor.shape[0] != decryptor.shape[1]:
        raise ValueError(f'decryptor shape is illegal. must be square matrix.')
    # assert decryptor.ndim == 2 and decryptor.shape[0] == decryptor.shape[1]

    arr = string_to_array(string, decryptor.shape[0], offset)  # 字符串转数字矩阵
    result = (decryptor @ arr.T).T % 26 + ord('A') - offset  # 算法
    result = ''.join(map(chr, map(int, result.ravel())))  # 数字矩阵转字符串
    return result


if __name__ == '__main__':
    # en_matrix = np.array([[1, 1, 2], [-1, 2, 0], [2, 1, 3]])
    # m_msg = 'EastChinaNormalUniversity'
    # c_msg = encode(en_matrix, m_msg)
    # print(f'en_matrix:\n{en_matrix}\n')
    # print(f'm_msg: {m_msg}')
    # print(f'c_msg: {c_msg}')
    #
    # de_matrix = np.array(np.linalg.inv(en_matrix), dtype=int)
    # m_msg2 = decode(de_matrix, c_msg)
    # print(f'de_matrix:\n{de_matrix}\n')
    # print(f'm_msg: {m_msg2}')

    en_matrix = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    de_matrix = np.array(np.linalg.inv(en_matrix), dtype=int)
    c_msg = 'PLGTGBQHM'
    m_msg = decode(de_matrix, c_msg, offset=1)  # Bugku题目说A=1，就是offset=1
    print(m_msg)
