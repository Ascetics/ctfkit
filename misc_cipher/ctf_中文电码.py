# -*- coding:utf8 -*-
import pandas as pd

"""
1983年邮电部编写的《标准电码本（修订本）》，包含7293个中文字符（汉字、字母和符号）。

5831和7016两个汉字现已废止，不予实现；
9992至9995的标点因计算机兼容性这里没有实现；

9992	起始着重号
9993	末尾着重号
9994	起始专名号
9995	末尾专名号

9998是中文空格（即全角空格）。
"""


def _create_csv():
    """
    生成中文电码csv文件
    :return:
    """
    f = open('ctf_中文电码.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()

    codes, words = [], []
    for i, line in enumerate(lines):
        line = line.strip('\n')
        code_word = line.split('\t')
        if len(code_word) != 2:
            msg = f'{i} line has illegal value. {code_word}'
            raise ValueError(msg)
        else:
            codes.append(code_word[0])
            words.append(code_word[1])

    dic = {'code': codes, 'word': words}
    df = pd.DataFrame(dic)
    df.to_csv('ctf_中文电码.csv')


def enc(string):
    df = pd.read_csv('ctf_中文电码.csv', dtype={'code': str, 'word': str})
    words = df.get('word').values
    df.set_index('word', inplace=True)  # 设置汉字列为索引

    result = []
    for i, c in enumerate(string):
        if c not in words:
            raise ValueError(f'illegal character {c}.')
        else:
            result.append(df.loc[c]['code'])
    return ''.join(result)


def dec(string):
    string = string.strip()
    if len(string) % 4 != 0:
        raise ValueError(f'string length must be multiple of 4.')
    if not string.isdecimal():
        raise ValueError(f'string must be decimal.')

    df = pd.read_csv('ctf_中文电码.csv', dtype={'code': str, 'word': str})
    df.set_index('code', inplace=True)  # 设置编码列为索引

    result = []
    for i in range(0, len(string), 4):
        code = string[i:i + 4]
        result.append(df.loc[code]['word'])
    return ''.join(result)


if __name__ == '__main__':
    # _create_csv()
    plain = dec('049117955478')
    print(plain)
    cipher = enc('中文查询电码')
    print(cipher)
