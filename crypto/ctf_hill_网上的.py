import numpy as np


def encode(string, size):
    # 转换小写字母
    if not string.islower():
        string = string.lower()
    # 分成 size个 字的分段
    blocks = [string[i:i + size] for i in range(0, len(string), size)]
    # 明文字串与密钥矩阵阶数不整除。。字串补a
    if len(blocks[-1]) != size:
        blocks[-1] = blocks[-1].ljust(size, 'a')
    # 将 a-z 编码为 0-25
    temp = np.array([list(map(ord, block)) for block in blocks]) - ord('a')
    #     print(temp)
    return temp


def analysis(crypter, code):
    return ((crypter @ code.T) % 26).T + ord('a')


if __name__ == '__main__':
    # 要加密的信息
    en_msg = 'eastchinanormaluniversity'.lower()
    print('待加密的信息：' + en_msg)

    # 密钥
    en_matrix = np.array([[2, 5], [9, 5]])
    print('密钥：')
    print(en_matrix)

    # 加密代码
    en_code = analysis(en_matrix, encode(en_msg, 2))

    # 密文
    de_msg = ''.join(map(chr, en_code.ravel()))
    print("密文：" + de_msg[:len(en_msg)].upper())

    # arr1 = np.array([[1, 2], [2, 1]])
    # arr2 = np.array([[1, 3], [3, 1]])
    # print(arr1 @ arr2)
