"""
Tap Code 敲击码
因该编码对信息通过使用一系列的点击声音来编码而命名，敲击码是基于5×5方格波利比奥斯方阵来实现的。
不同点是是用K字母被整合到C中。
码表如下：
  1  2  3  4  5
1 A  B C/K D  E
2 F  G  H  I  J
3 L  M  N  O  P
4 Q  R  S  T  U
5 V  W  X  Y  Z

/分割坐标，空格分割坐标值，举例
..... ../... ./... ./... ../
(5,2),(3,1),(3,1),(3,2)
w,l,l,m
"""


def enc(string):
    string = string.strip('\n').lower()

    for c in string:
        if not ord('a') <= ord(c) <= ord('z'):
            raise ValueError(string + f' has illegal symbol: {c}')

    result = []
    for c in string:
        if c < 'k':
            offset = ord(c) - ord('a')
            x, y = offset // 5 + 1, offset % 5 + 1
        elif c > 'k':
            offset = ord(c) - ord('a') - 1
            x, y = offset // 5 + 1, offset % 5 + 1
        else:
            x, y = 1, 3
        result.append(x * '.' + ' ' + y * '.')
        result.append('/')
    return ''.join(result)


def dec(string):
    string = string.strip('\n')

    symbol = {'.', ' ', '/'}
    for c in string:
        if c not in symbol:
            raise ValueError(string + f' has illegal symbol: {c}')

    tab = [['a', 'b', 'c/k', 'd', 'e'],
           ['f', 'g', 'h', 'i', 'j'],
           ['l', 'm', 'n', 'o', 'p'],
           ['q', 'r', 's', 't', 'u'],
           ['v', 'w', 'x', 'y', 'z']]

    result = []
    coordinates = string.split('/')
    for i, coordinate in enumerate(coordinates):
        if coordinate != '':
            s = coordinate.split(' ')
            if len(s) != 2 or s[0] == '' or s[1] == '':
                msg = (f'{i} coordinate is illegal. length: {len(s)}'
                       f' x: {s[0]} y: {s[1]}')
                raise ValueError(msg)
            x, y = s[0].count('.') - 1, s[1].count('.') - 1
            result.append(tab[x][y])
    return ''.join(result)


if __name__ == '__main__':
    cipher = '..... ../... ./... ./... ../'
    plain = dec(cipher)
    print(plain)
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = enc(plain)
    print(cipher)
    plain = dec(cipher)
    print(plain)
    pass
