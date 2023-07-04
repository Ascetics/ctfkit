"""
ROT5 是 rotate by 5 places 的简写，意思是旋转5个位置，其它皆同。

ROT5：只对数字进行编码，用当前数字往前数的第5个数字替换当前数字。
例如当前为0，编码后变成5，当前为1，编码后变成6，以此类推顺序循环。

ROT13：只对字母进行编码，用当前字母往前数的第13个字母替换当前字母。
例如当前为A，编码后变成N，当前为B，编码后变成O，以此类推顺序循环。

ROT18：这是一个异类，本来没有，它是将ROT5和ROT13组合在一起，为了好称呼，将其命名为ROT18。

ROT47：对数字、字母、常用符号进行编码，按照它们的ASCII值进行位置替换。
用当前字符ASCII值往前数的第47位对应字符替换当前字符。
例如当前为小写字母z，编码后变成大写字母K，当前为数字0，编码后变成符号_。
用于ROT47编码的字符其ASCII值范围是33－126，具体可参考ASCII编码。
"""


def rot5enc(string):
    result = ''
    for c in string:
        if ord('0') <= ord(c) <= ord('9'):
            result += chr(ord('0') + (ord(c) - ord('0') + 5) % 10)
        else:
            result += c
    return result


def rot5dec(string):
    return rot5enc(string)


def rot13enc(string):
    result = ''
    for c in string:
        if ord('A') <= ord(c) <= ord('Z'):
            result += chr(ord('A') + (ord(c) - ord('A') + 13) % 26)
        elif ord('a') <= ord(c) <= ord('z'):
            result += chr(ord('a') + (ord(c) - ord('a') + 13) % 26)
        else:
            result += c
    return result


def rot13dec(string):
    return rot13enc(string)


def rot18enc(string):
    result = ''
    for c in string:
        if ord('0') <= ord(c) <= ord('9'):
            result += rot5enc(c)
        elif ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z'):
            result += rot13enc(c)
        else:
            result += c
    return result


def rot18dec(string):
    return rot18enc(string)


def rot47enc(string):
    result = ''
    for c in string:
        if 33 <= ord(c) <= 126:
            result += chr(33 + (ord(c) - 33 + 47) % 94)
        else:
            result += c
    return result


def rot47dec(string):
    return rot47enc(string)


if __name__ == '__main__':
    # msg = 'ROT5/13/18/47 is the easiest and yet powerful cipher!'
    msg = 'AecvWpF9YinwVc7tvKfCGWt28oYiucpd5MEWhghGaaLWKfgTEywz5hmRREEi'
    msg = rot47enc(msg)
    print(msg)
    msg = rot47dec(msg)
    print(msg)
