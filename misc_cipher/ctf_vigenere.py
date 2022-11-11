# -*- coding:utf8 -*-
"""
Vigenere cipher is an advanced Caesar cipher.
"""

TAB = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ',
       'BCDEFGHIJKLMNOPQRSTUVWXYZA',
       'CDEFGHIJKLMNOPQRSTUVWXYZAB',
       'DEFGHIJKLMNOPQRSTUVWXYZABC',
       'EFGHIJKLMNOPQRSTUVWXYZABCD',
       'FGHIJKLMNOPQRSTUVWXYZABCDE',
       'GHIJKLMNOPQRSTUVWXYZABCDEF',
       'HIJKLMNOPQRSTUVWXYZABCDEFG',
       'IJKLMNOPQRSTUVWXYZABCDEFGH',
       'JKLMNOPQRSTUVWXYZABCDEFGHI',
       'KLMNOPQRSTUVWXYZABCDEFGHIJ',
       'LMNOPQRSTUVWXYZABCDEFGHIJK',
       'MNOPQRSTUVWXYZABCDEFGHIJKL',
       'NOPQRSTUVWXYZABCDEFGHIJKLM',
       'OPQRSTUVWXYZABCDEFGHIJKLMN',
       'PQRSTUVWXYZABCDEFGHIJKLMNO',
       'QRSTUVWXYZABCDEFGHIJKLMNOP',
       'RSTUVWXYZABCDEFGHIJKLMNOPQ',
       'STUVWXYZABCDEFGHIJKLMNOPQR',
       'TUVWXYZABCDEFGHIJKLMNOPQRS',
       'UVWXYZABCDEFGHIJKLMNOPQRST',
       'VWXYZABCDEFGHIJKLMNOPQRSTU',
       'WXYZABCDEFGHIJKLMNOPQRSTUV',
       'XYZABCDEFGHIJKLMNOPQRSTUVW',
       'YZABCDEFGHIJKLMNOPQRSTUVWX',
       'ZABCDEFGHIJKLMNOPQRSTUVWXY', ]


def encode(string, key):
    ki = 0
    c_text = ''

    for i in string:
        if i.islower() or i.isupper():
            row = ord(i.upper()) - ord('A')
            col = ord(key[ki % len(key)].upper()) - ord('A')
            c_text += TAB[row][col].lower() if i.islower() else TAB[row][col]
            ki += 1
        else:
            c_text += i
    return c_text


def decode(string, key):
    ki = 0
    m_text = ''

    for i in string:
        if i.islower() or i.isupper():
            for line in TAB:
                if line[ord(key[ki % len(key)].upper()) - ord('A')] == i.upper():
                    m_text += line[0].lower() if i.islower() else line[0]
                    ki += 1
                    break
        else:
            m_text += i
    return m_text


if __name__ == '__main__':
    m = 'W3lcome_to_Mi5C_Wryyy'
    k = 'high'
    print(encode(m, k))

    c = 'D3tivtm_zv_Tq5I_Dygef'
    print(decode(c, k))
