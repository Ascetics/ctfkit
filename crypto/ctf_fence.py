# -*- coding:utf8 -*-
"""
栅栏密码，加密过程
m=
s{aufadtunfuynuvvfhudxrvnaabvn}abhtnt

s           y           n           t
 {         u n         v a         n
  a       f   u       r   a       t
   u     n     v     x     b     h
    f   u       v   d       v   b
     a t         f u         n a
      d           h           }

c=
synt{unvanafuratunvxbhfuvdvbatfunadh}
"""


def encode(string, n_fence):
    c_str = ''
    f_text = [[] for i in range(n_fence)]

    flag = True
    for i, c in enumerate(string):
        if i > 0 and i % (n_fence - 1) == 0:
            flag = not flag

        if flag:
            f_text[i % (n_fence - 1)].append(c)
        else:
            f_text[(n_fence - 1) - i % (n_fence - 1)].append(c)

    for line in f_text:
        c_str += ''.join(line)

    return c_str


def decode(string, n_fence):
    pass


def main():
    m_str = 's{aufadtunfuynuvvfhudxrvnaabvn}abhtnt'
    # m_str = 'D3tivtm_zv_Tq5I_Dygef'
    print(encode(m_str, 7))


if __name__ == '__main__':
    main()
