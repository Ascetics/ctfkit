import base64

"""
[ACTF新生赛2020]base64隐写
附件2次base64解码得到类似C++代码，但是有乱码。但flag不在这里。

base64编码，6bit一组查base64 alphabet得到编码。这决定了当字符串长度不是3的倍数时，余有bit。
剩余bit，用0补充到6位再查base64 alphabet得到最后一个编码表字符。
编码最后用=补充，补充 (3 - len(string) % 3) % 3 个=。

以字母a为例，ascii编码为01100001
一般base64编码会补0: 011000 010000 -> YQ -> YQ==
但是如果补其他内容，只要位数不变，就不会影响解码的效果。
比如a可以补位为是 010001 or 010010 ... or 011111 -> YR== YS== ... Yf==
运行下面的代码，就看到解码都是字母a
b1 = [b'YQ==', b'YR==', b'YS==', b'YT==', b'YU==', b'YV==', b'YW==', b'YX==',
      b'YY==', b'YZ==', b'Ya==', b'Yb==', b'Yc==', b'Yd==', b'Ye==', b'Yf==', ]
b2 = list(map(lambda x: base64.b64decode(x), b1))
print(b2)

这为隐写创造了空间。
=，余2个字符，有4bit偏移
==，余1个字符，有4bit偏移
"""
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

with open('ACTF2022_base64_steg.txt', 'r') as fin:
    steg_lines = fin.readlines()
    steg_lines = list(map(lambda line: line.strip('\n'),
                          steg_lines))  # steg_lines要迭代多遍，所以转成list

    # 先解码再编码得到一般的base64编码
    normal_lines = map(lambda line: base64.b64decode(line.encode('utf-8')),
                       steg_lines)
    normal_lines = map(lambda line: base64.b64encode(line).decode('utf-8'),
                       normal_lines)

    # 计数每行编码的=个数eq_counts
    eq_counts = map(lambda line: line.count('='), steg_lines)

    # 去掉=，看最后一个字符的差别得到offsets
    steg_lines = map(lambda line: line.replace('=', ''), steg_lines)
    normal_lines = map(lambda line: line.replace('=', ''), normal_lines)
    offsets = map(lambda steg_line, normal_line: abs(
        alphabet.index(steg_line[-1]) - alphabet.index(normal_line[-1])),
                  steg_lines, normal_lines)

    # 按照=个数*2，左边补0，形成二进制字符串
    bin_strs = map(lambda eq_count, offset: bin(offset)[2:].zfill(
        eq_count * 2) if eq_count else '', eq_counts, offsets)
    bin_str = ''.join(bin_strs)

    chs = []
    for i in range(0, len(bin_str), 8):
        chs.append(chr(int(bin_str[i:i + 8], 2)))
    print(''.join(chs))
