# -*- coding:utf8 -*-
"""
社会主义核心价值观(core socialist values)的主要内容是

富强、民主、文明、和谐
自由、平等、公正、法治
爱国、敬业、诚信、友善

是社会主义核心价值体系的高度凝练和集中表达
是当代中国精神的集中体现
凝结着全体人民共同的价值追求。
"""
from typing import List
from urllib import parse
import random
import re


def step3(inp: List[int]) -> str:
    value = '富强民主文明和谐自由平等公正法治爱国敬业诚信友善'
    return ''.join(list(map(lambda v: value[v << 1] + value[v << 1 | 1], inp)))


def step2(inp: str) -> List[int]:
    ans = []
    for c in inp:
        v = int(c, 16)
        if v < 10:
            ans.append(v)
        elif random.random() < 0.5:
            ans.append(11)
            ans.append(v - 6)
        else:
            ans.append(10)
            ans.append(v - 10)
    return ans


def step1(inp: str) -> str:
    reg = re.compile(r'[A-Za-z0-9\-\_\.\!\~\*\'\(\)]')
    tmp = reg.sub(lambda g: hex(ord(g.group(0)))[2:], inp)
    return parse.quote(tmp).replace('%', '').upper()


def enc(inp: str) -> str:
    return step3(step2(step1(inp)))


if __name__ == '__main__':
    m = 'flag{c5V_1S_v3Ry_imp0rt@nt}'
    c = enc(m)
    print(c)
