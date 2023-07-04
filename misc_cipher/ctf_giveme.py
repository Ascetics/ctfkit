# -*- coding:utf8 -*-
"""
一表人才，二表反行
"""

ciphertext = 'DXFLOXKAKFATOSBC'

original_list = ['M', 'R', 'K', 'S', 'A', 'B', 'L', 'U', 'D', 'C', 'N', 'V', 'H', 'F', 'O', 'W', 'T', 'G', 'P', 'X',
                 'E', 'I', 'Q', 'Y']
reversed_list = original_list[::-1]

flag = ''
for char in ciphertext:
    for olist in original_list:
        if char == olist:
            oindex = original_list.index(olist)
            flag += reversed_list[oindex]

print(flag)
