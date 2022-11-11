# -*- coding:utf8 -*-
"""
Base64要求把每三个8Bit的字节转换为四个6Bit的字节（3*8 = 4*6 = 24），
然后把6Bit再添两位高位0，组成四个8Bit的字节，也就是说，转换后的字符串理论上将要比原来的长1/3
"""
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def encode(string):
    old_str = ''
    new_str = []
    result = ''
    # 把原始字符串转换为二进制，ord是ascii位置，用bin转换后是0b开头的，所以把b替换了，首位补0补齐8位
    for i in string:
        old_str += '{:08}'.format(int(str(bin(ord(i))).replace('0b', '')))
    # 把转换好的二进制按照6位一组分好，最后一组不足6位的后面补0
    for j in range(0, len(old_str), 6):
        new_str.append('{:<06}'.format(old_str[j:j + 6]))
    # 在base_list中找到对应的字符，拼接。 int把二进制字符串表示的数转成十进制
    for k in new_str:
        result += alphabet[int(k, 2)]
        # 判断base字符结尾补几个‘=’
    if len(string) % 3 == 1:
        result += '=='
    elif len(string) % 3 == 2:
        result += '='
    return result


def decode(string):
    old_str = string.replace('=', '')
    new_str = ''
    result = ''
    # 把密文转换成二进制，
    for i in old_str:
        s = '{:06}'.format(int(str(bin(alphabet.index(i))).replace('0b', '')))
        new_str += s
    for j in range(0, len(new_str), 8):
        if j + 8 > len(new_str):
            break
        else:
            result += chr(int(new_str[j:j + 8], 2))
    return result


def main():
    m_msg = 'flag{b@5E64_E^c0de}'
    print(encode(m_msg))
    c_msg = 'ZmxhZ3tiQDVFNjRfRV5jMGRlfQ=='
    print(decode(c_msg))
    pass


if __name__ == '__main__':
    main()
