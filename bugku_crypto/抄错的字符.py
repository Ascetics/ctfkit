# -*- coding : utf-8 -*-
import base64


def resolve(s):
    # 可能抄错的数字和对应字母
    d = {'O': 0, 'I': 1, 'L': 1, 'Z': 2, 'S': 5, 'B': 6, 'G': 9, 'Q': 9}
    sdict = []

    # 每个字符都可能是大小写和原本的数字
    for c in s:
        sdict.append(c + c.lower() + (str(d.get(c)) if d.get(c) else ''))

    # 把可能的原来字符串都列出来
    result = ['']
    for sd in sdict:
        temp = []
        for sr in result:
            for c in sd:
                temp.append(sr + c)
        result = temp

    # 把可能的base64编码都搞出来
    b64result = []
    err = []
    for i, sr in enumerate(result):
        try:
            #
            s1 = base64.b64decode(sr.encode('utf-8'))
            s1 = s1.decode('utf-8')
            b64result.append(s1)
        except:
            try:
                sr = sr + '='
                s1 = base64.b64decode(sr.encode('utf-8'))
                s1 = s1.decode('utf-8')
                b64result.append(s1)
            except:
                try:
                    sr = sr + '=='
                    s1 = base64.b64decode(sr.encode('utf-8'))
                    s1 = s1.decode('utf-8')
                    b64result.append(s1)
                except:
                    err.append(sr)
    return b64result


def main():
    # base64 因此将密文分成4个一组
    m = 'QWIHBLGZZXJSXZNVBZW'
    mseg = []
    for i in range(0, len(m), 4):
        mseg.append(m[i:i + 4])
    print(mseg)

    # 遍历所有的字符串片段，拼接到一起
    flines = ['']
    for s in mseg:
        b64seg = resolve(s)
        temp = []
        for sf in flines:
            for sg in b64seg:
                temp.append(sf + sg)
        flines = temp

    # 每行都加上换行符
    for i, s in enumerate(flines):
        flines[i] = s + '\n'

    # 输出到文件
    f = open('抄错的字符.txt', 'w', encoding='utf-8')
    f.writelines(flines)
    f.close()


if __name__ == '__main__':
    main()
