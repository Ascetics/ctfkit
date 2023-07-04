"""
Morse Code 摩尔斯电码编码表：

国际摩尔斯电码（字母）
A 	·- 	    B 	-··· 	C 	-·-· 	D 	-·· 	E 	· 	    F 	··-· 	G 	--·
H 	···· 	I 	·· 	    J 	·--- 	K 	-·- 	L 	·-·· 	M 	-- 	    N 	-·
O 	--- 	P 	·--· 	Q 	--·- 	R 	·-· 	S 	··· 	T 	- 	    U 	··-
V 	···- 	W 	·-- 	X 	-··- 	Y 	-·-- 	Z 	--··

国际摩尔斯电码（数字）
1 	·---- 	2 	··--- 	3 	···-- 	4 	····- 	5 	·····
6 	-···· 	7 	--··· 	8 	---·· 	9 	----· 	0 	-----

国际摩尔斯电码（标点）
. 	·-·-·- 	: 	---··· 	, 	--··-- 	    ; 	-·-·-· 	? 	··--·· 	= 	-···-
' 	·----· 	/ 	-··-· 	! 	-·-·-- 	    - 	-····- 	_ 	··--·- 	" 	·-··-·
( 	-·--· 	) 	-·--·- 	$ 	···-··- 	& 	·-··· 	@ 	·--·-· 	+ 	·-·-·
"""


def _check_and_get_dec_graph_dic(string):
    """
    检查电码只包含点、线、分隔符，并确定是哪一种风格
    :param string: 电码
    :return: 电码字符风格
    """
    chs = {c for c in string}
    if {'·', '-', ' '} == chs:
        return {'dot': '·', 'dash': '-', 'sep': ' '}
    elif {'·', '-', '/'} == chs:
        return {'dot': '·', 'dash': '-', 'sep': '/'}
    elif {'·', '_', ' '} == chs:
        return {'dot': '·', 'dash': '_', 'sep': ' '}
    elif {'·', '_', '/'} == chs:
        return {'dot': '·', 'dash': '_', 'sep': '/'}
    elif {'.', '-', ' '} == chs:
        return {'dot': '.', 'dash': '-', 'sep': ' '}
    elif {'.', '-', '/'} == chs:
        return {'dot': '.', 'dash': '-', 'sep': '/'}
    elif {'.', '_', ' '} == chs:
        return {'dot': '.', 'dash': '_', 'sep': ' '}
    elif {'.', '_', '/'} == chs:
        return {'dot': '.', 'dash': '_', 'sep': '/'}
    else:
        raise ValueError(
            f'All characters must be consistant: dot, dash, separator. But got {chs}.')


def _check_enc_graph_dic(graph_dic):
    """
    检查电码风格
    :param graph_dic:电码风格：点、线、分隔符
    :return: 电码字符风格
    """
    if ({'dot': '·', 'dash': '-', 'sep': ' '} != graph_dic and
        {'dot': '·', 'dash': '-', 'sep': '/'} != graph_dic and
        {'dot': '·', 'dash': '_', 'sep': ' '} != graph_dic and
        {'dot': '·', 'dash': '_', 'sep': '/'} != graph_dic and
        {'dot': '.', 'dash': '-', 'sep': ' '} != graph_dic and
        {'dot': '.', 'dash': '-', 'sep': '/'} != graph_dic and
        {'dot': '.', 'dash': '_', 'sep': ' '} != graph_dic and
        {'dot': '.', 'dash': '_', 'sep': '/'} != graph_dic):
        raise ValueError(f'illegal graph_dic {graph_dic}')


def enc(string, graph_dic):
    """
    先统一转成01，再转成电码
    :param string: 明文
    :param graph_dic: 电码字符风格
    :return: 电码
    """
    _check_enc_graph_dic(graph_dic)
    string = string.strip('\n')

    enc_tab = {
        'a': '01', 'b': '1000', 'c': '1010', 'd': '100', 'e': '0', 'f': '0010',
        'g': '110', 'h': '0000', 'i': '00', 'j': '0111', 'k': '101',
        'l': '0100', 'm': '11', 'n': '10', 'o': '111', 'p': '0110', 'q': '1101',
        'r': '010', 's': '000', 't': '1', 'u': '001', 'v': '0001', 'w': '011',
        'x': '1001', 'y': '1011', 'z': '1100',
        #
        '1': '01111', '2': '00111', '3': '00011', '4': '00001', '5': '00000',
        '6': '10000', '7': '11000', '8': '11100', '9': '11110', '0': '11111',
        #
        '.': '010101', ':': '111000', ',': '110011', ';': '101010',
        '?': '001100', '=': '10001',
        '\'': '011110', '/': '10010', '!': '101011', '-': '100001',
        '_': '001101', '"': '010010',
        '(': '10110', ')': '101101', '$': '0001001', '&': '01000',
        '@': '011010', '+': '01010',
    }

    result = []
    for c in string:
        if enc_tab.get(c):
            dig_cipher = enc_tab.get(c)
            symbol_cipher = dig_cipher.replace('0', graph_dic['dot']).replace(
                '1', graph_dic['dash'])
            result.append(symbol_cipher + graph_dic['sep'])
        else:
            raise ValueError(f'illegal character {c}.')
    return ''.join(result)


def dec(string):
    """
    先统一转成01，再转成译文
    :param string:电码
    :return: 译文
    """
    string = string.strip('\n')
    graph_dic = _check_and_get_dec_graph_dic(string)

    string = string.strip(graph_dic['sep'])
    string = string.replace(graph_dic['dot'], '0')
    string = string.replace(graph_dic['dash'], '1')
    characters = string.split(graph_dic['sep'])

    dec_tab = {
        '01': 'a', '1000': 'b', '1010': 'c', '100': 'd', '0': 'e', '0010': 'f',
        '110': 'g', '0000': 'h', '00': 'i', '0111': 'j', '101': 'k',
        '0100': 'l', '11': 'm', '10': 'n', '111': 'o', '0110': 'p', '1101': 'q',
        '010': 'r', '000': 's', '1': 't', '001': 'u', '0001': 'v', '011': 'w',
        '1001': 'x', '1011': 'y', '1100': 'z',
        '01111': '1', '00111': '2', '00011': '3', '00001': '4', '00000': '5',
        '10000': '6', '11000': '7', '11100': '8', '11110': '9', '11111': '0',
        '010101': '.', '111000': ':', '110011': ',', '101010': ';',
        '001100': '?', '10001': '=', '011110': '\'', '10010': '/',
        '101011': '!', '100001': '-', '001101': '_', '010010': '"',
        '10110': '(', '101101': ')', '0001001': '$', '01000': '&',
        '011010': '@', '01010': '+',
    }

    result = []
    for c in characters:
        if dec_tab.get(c):
            result.append(dec_tab.get(c))
        else:
            raise ValueError(f'illegal character {c}')
    return ''.join(result)


if __name__ == '__main__':
    ciphers = [
        '-·-· - ··-· ··--·- ·---- ··· ··--·- ···- ···-- ·-· -·-- ··--·- -·-· ----- --- ·-·· -·-·--',
        '-·-·/-/··-·/··--·-/·----/···/··--·-/···-/···--/·-·/-·--/··--·-/-·-·/-----/---/·-··/-·-·--',
        '-.-. - ..-. ..--.- .---- ... ..--.- ...- ...-- .-. -.-- ..--.- -.-. ----- --- .-.. -.-.--',
        '-.-./-/..-./..--.-/.----/.../..--.-/...-/...--/.-./-.--/..--.-/-.-./-----/---/.-../-.-.--',
        '_·_· _ ··_· ··__·_ ·____ ··· ··__·_ ···_ ···__ ·_· _·__ ··__·_ _·_· _____ ___ ·_·· _·_·__',
        '_·_·/_/··_·/··__·_/·____/···/··__·_/···_/···__/·_·/_·__/··__·_/_·_·/_____/___/·_··/_·_·__',
        '_._. _ .._. ..__._ .____ ... ..__._ ..._ ...__ ._. _.__ ..__._ _._. _____ ___ ._.. _._.__',
        '_._./_/.._./..__._/.____/.../..__._/..._/...__/._./_.__/..__._/_._./_____/___/._../_._.__',

    ]
    for cipher in ciphers:
        plain = dec(cipher)
        print(plain)

    plain = ('abcdefghijklmnopqrstuvwxyz0123456789.:,;?=\'/!-_"()$&@+')
    print(enc(plain, {'dot': '·', 'dash': '-', 'sep': '/'}))
