# -*- coding:utf8 -*-
"""
Vigenere cipher is an advanced Caesar cipher.
"""


def check_key(key):
    for k in key:
        if not k.islower() and not k.isupper():
            print('The key must consist only of letters')


def encode(string, key):
    check_key(key)
    si, ki, c_text = 0, 0, ''
    while si < len(string):
        s, k = string[si], key[ki % len(key)]
        if not s.islower() and not s.isupper():
            c_text += s
            si += 1
            continue

        c, offset = ord(s), ord(k.upper()) - ord('A')
        if s.isupper():
            c = (c - ord('A') + offset) % 26 + ord('A')
        elif s.islower():
            c = (c - ord('a') + offset) % 26 + ord('a')
        c_text += chr(c)
        si += 1
        ki += 1

    return c_text


def decode(string, key):
    check_key(key)
    si, ki, m_text = 0, 0, ''
    while si < len(string):
        s, k = string[si], key[ki % len(key)]
        if not s.islower() and not s.isupper():
            m_text += s
            si += 1
            continue

        c, offset = ord(s), ord(k.upper()) - ord('A')
        if s.isupper():
            c = (c - ord('A') + 26 - offset) % 26 + ord('A')
        elif s.islower():
            c = (c - ord('a') + 26 - offset) % 26 + ord('a')
        m_text += chr(c)
        si += 1
        ki += 1

    return m_text


if __name__ == '__main__':
    m = 'W3lcome_to_Mi5C_Wryyy'
    k = 'high'
    print(encode(m, k))

    c = 'D3tivtm_zv_Tq5I_Dygef'
    print(decode(c, k))
