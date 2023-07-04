# -*- coding:utf8 -*-
"""
Baudot Code 一种5bit编码，比ASCII还要古老
0x00 是ascii的NULL
0x0A 是ascii的LF
0x0D 是ascii的CR
0x05 是ascii的ENQ
0x07 是ascii的BELL
"""

LETTERS = [chr(0x00), 'E', chr(0x0A), 'A', ' ', 'S', 'I', 'U', chr(0x0D), 'D',
           'R', 'J', 'N', 'F', 'C', 'K', 'T', 'Z', 'L', 'W', 'H', 'Y', 'P', 'Q',
           'O', 'B', 'G', 'Figures', 'M', 'X', 'V', 'Letters']
FIGURES = [chr(0x00), '3', chr(0x0A), '-', ' ', '\'', '8', '7', chr(0x0D),
           chr(0x05), '4', chr(0x07), ',', '!', ':', '(', '5', '+', ')', '2',
           '$', '6', '0', '1', '9', '?', '&', 'Figures', '.', '/', ';',
           'Letters']


def dec(c):
    tab = LETTERS
    m = ''
    for i in c:
        if LETTERS[i] == 'Letters':
            tab = LETTERS
        elif LETTERS[i] == 'Figures':
            tab = FIGURES
        else:
            m += tab[i]
    return m


def main():
    c = [0b11111, 0b11001, 0b00011, 0b00111, 0b01001, 0b11011, 0b10110, 0b11111,
         0b10000, 0b01110, 0b11011, 0b10110, 0b11111, 0b01001, 0b00001]
    m = dec(c)
    print(m)


if __name__ == '__main__':
    main()
