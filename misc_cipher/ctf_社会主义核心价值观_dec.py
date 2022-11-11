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


def step3(enc: str) -> List[int]:
    assert len(enc) % 2 == 0
    value = '富强民主文明和谐自由平等公正法治爱国敬业诚信友善'
    ans = []
    for i in range(0, len(enc), 2):
        ans.append(value.index(enc[i:i + 2]) >> 1)
    return ans


def step2(enc: List[int]) -> str:
    ans = ''
    i = 0
    while i < len(enc):
        if enc[i] < 10:
            ans += str(enc[i])
            i += 1
        elif enc[i] == 10:
            ans += hex(enc[i + 1] + 10)[2:]
            i += 2
        elif enc[i] == 11:
            ans += hex(enc[i + 1] + 6)[2:]
            i += 2
        else:
            raise ValueError('step2 failed. 不合法数据')
    return ans


def step1(enc: str) -> str:
    tmp = ''
    for i in range(len(enc)):
        if not i % 2:
            tmp += '%'
        tmp += enc[i]
    return parse.unquote(tmp)


def dec(enc: str) -> str:
    return step1(step2(step3(enc)))


if __name__ == '__main__':
    c = ('公正公正公正友善公正公正民主公正法治法治友善平等公正和谐和谐平等平等公正平等诚信平等'
         '和谐民主平等和谐平等友善敬业法治公正和谐和谐平等文明法治敬业平等友善敬业公正敬业公正'
         '友善法治法治富强和谐富强法治文明法治自由自由富强公正友善爱国法治自由法治诚信和谐')
    # flag{c5V_1S_v3Ry_imp0rt@nt}
    m = dec(c)
    print(m)

    c = ('公正爱国法治自由法治自由法治富强法治和谐和谐诚信富强文明友善敬业文明友善敬业公正民主'
         '法治自由公正诚信平等公正诚信平等公正诚信文明文明友善爱国法治公正公正敬业法治富强文明'
         '友善敬业')
    # https://atool.vip/
    m = dec(c)
    print(m)
