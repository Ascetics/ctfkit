# -*- coding:utf8 -*-

import keyword

# 各个进制表示
print("十进制11，也就是:11：", 11)
print("二进制11，也就是3：", 0b11)
print("八进制11，也就是9：", 0o11)
print("十六进制11，也就是17", 0x11)

# 将十六进制数转换为十进制数
num = 'b'
v = int(num, base=16)
print(v)

# bit_length的用法
age = 0
while age < 0x10:
    print(age, ":", age.bit_length())
    age += 1
    pass

################################################################################

print(int(True))  # 1
print(int(False))  # 0

print(bool(None))  # False
print(bool(0))  # False
print(bool(""))  # False
print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False

################################################################################

test = "Kevin"
# i
# vi
# Kevi
v1 = test[3]
v2 = test[2:4]
v3 = test[0:-1]
print(v1, len(v1))
print(v2, len(v2))
print(v3, len(v3))

# 大小写转换capitalize、lower、upper、casefold、swapcase ##########################
# 首字母大写
test = "alex"
print(test.capitalize())

# 英文字母的大写转换为小写
test = "aLex"
print(test.lower())
# 更牛逼的大写转换为小写，任意字母
test = "ΘΠ"
print(test.casefold())
# 转换大小写
test = "θπΘΠ"
print(test.swapcase())

# 居中填充center、居左填充ljust、居右填充rjust #####################################
# 以某字符串开头startwith、以某字符串结尾endwith、查找子字符串find等实用方法。 ##########
# 居中填充 center ***Alex**
# 居左填充 ljust  Alex*****
# 居右填充 rjust  *****Alex
test = "Alex"
vc = test.center(9, "*")
vl = test.ljust(9, "*")
vr = test.rjust(9, "*")
print(vc, vl, vr)

# 从第6个开始到第8个结束（不含），计算子字符串个数
test = "aLexalexer"
print(test.count("ex", 6, 8))

# 以***开头结尾
test = "aLexalexer"
print(test.endswith("ex", 6, 8))
print(test.startswith("al", 4, 6))

# 查找子字符串
test = "aLexalexer"
print(test.find("ex"))
print(test.find("ex", 5, 7))  # [5, 8)
print(test.find("ex", 5, 8))  # [5, 8]

# 格式化字符串、输出对齐格式化。 ####################################################
# 格式化
# i am {name}, age {a}
# i am Alex, age 19
test = "i am {name}, age {a}"
v1 = test.format(name="Alex", a=19)
v2 = test.format_map({"a": 19, "name": "Alex"})
print(v1)
print(v2)
# 格式化
# i am {0}, age {1}
# i am Alex, age 19
test = "i am {0}, age {1}"
print(test)
v3 = test.format("Alex", 19)
print(v3)

# 用expandtabs来实现对齐
# 找到\t也就是tab，将tab转换为空格
# tab前面的字符和转换的空格加起来长度一致
# username            email               password
# lingmk              lingmk@example.com  123456
# alex                alex@gamil.com      1qaz2wsx
# Kevin               kevin@qq.com        password
test = ('username\temail\tpassword\n'
        'lingmk\tlingmk@example.com\t123456\n'
        'alex\talex@gamil.com\t1qaz2wsx\n'
        'Kevin\tkevin@qq.com\tpassword\n')
v = test.expandtabs(20)
print(v)

# 字母数字的判断，这个比较复杂。 ####################################################
# is判断
# isalpha 字符串全是字母，不含阿拉伯数字，不包含罗马数字，不含符号
# isnumeric 字符串全是表示顺序的数字字符，比如阿拉伯数字2、汉字二贰、符号②、罗马数字Ⅱ
# islanum  isalpha或isnumeric
# isdigit 字符串全是包含阿拉伯数字的字符，比如2、②
# isdecimal 字符串全是字符表示的数，比如2
#
# string    isalpha   isnumeric isalnum   isdigit   isdecimal
# 2         False     True      True      True      True
# 二         True      True      True      False     False
# 贰         True      True      True      False     False
# ②         False     True      True      True      False
# two       True      False     True      False     False
# Ⅱ         False     True      True      False     False
# +2        False     False     False     False     False
# θπ        True      False     True      False     False
twos = ["2", "二", "贰", "②", "two", "Ⅱ", "+2", "θπ"]
v = "string\tisalpha\tisnumeric\tisalnum\tisdigit\tisdecimal\n"
for s in twos:
    v += s + "\t"
    v += str(s.isalpha()) + "\t"
    v += str(s.isnumeric()) + "\t"
    v += str(s.isalnum()) + "\t"
    v += str(s.isdigit()) + "\t"
    v += str(s.isdecimal()) + "\n"
    pass
print(v.expandtabs(10))

# 检验字符串是不是可用的变量名，是不是关键字。 ########################################

# isidentifier用来检验是否是可用的变量名
# 如果是关键字那么需要用keyword.iskeyword(s)
# name            isidentifier    iskeyword
# π               True            False
# 变量              True            False
# _123            True            False
# val             True            False
# def             True            True
# class           True            True
names = ["π", "变量", "_123", "val", "def", "class"]
val = "name\tisidentifier\tiskeyword\n"
for s in names:
    val += s + "\t"
    val += str(s.isidentifier()) + "\t"
    val += str(keyword.iskeyword(s)) + "\n"
    pass
print(val.expandtabs(16))

# 检验字符串中的字符是不是可以显示输出的。 ############################################
# 检验字符串中的字符是不是可以显示输出的
test = "abdl\tdjf\aso"
print(test)
v = test.isprintable()
print(v)

# 英文标题title #################################################################
# title() 将字符串每个单词首字母大写
# istitle判断时候不是title
#
# this is a title line. False
# This Is A Title Line. True
# 中文标题不是首字母大写规则 False
test = "this is a title line."
en_title = test.title()
cn_title = "中文标题不是首字母大写规则"
vtest = test.istitle()
ven_title = en_title.istitle()
vcn_title = cn_title.istitle()
print(test, vtest)
print(en_title, ven_title)
print(cn_title, vcn_title)

# join用当前字符串将另一个字符串test的每个字符间隔开来 ################################
#
# 你是风儿我是沙
# 你 是 风 儿 我 是 沙
# 你__是__风__儿__我__是__沙
test = "你是风儿我是沙"
print(test)
t1 = " "
v1 = t1.join(test)
print(v1)
t2 = "__"
v2 = t2.join(test)
print(v2)

# strip去除空白符空格、\t、\n。 ###################################################
# strip去除空白符
#
#  	left alex right		  20
# left alex right		  18
#  	left alex right 17
# left alex right 15
test = " \tleft alex right\t\t "
vl = test.lstrip()
vr = test.rstrip()
v = test.strip()
print(test, len(test))
print(vl, len(vl))
print(vr, len(vr))
print(v, len(v))

# strip去除指定字符串最多匹配的部分
#
# xalex 5
# lex 3   匹配左边xa
# xale 4  匹配右边x
# le 2    匹配左边xa和右边x
test = "xalex"
s = "9axa"
vl = test.lstrip(s)
vr = test.rstrip(s)
v = test.strip(s)
print(test, len(test))
print(vl, len(vl))
print(vr, len(vr))
print(v, len(v))

# maketrans和translate一起使用做字符串的对应替换。 ##################################
# maketrans和translate一起使用做字符串对应替换
#
# this is the test claus.
# 37i3 i3 37e 3e33 8l4u3.
t1 = "thawsc"
t2 = "374638"
m = str.maketrans(t1, t2)
v1 = "this is the test claus."
v2 = v1.translate(m)
print(v1)
print(v2)

# partition和split分割字符串。####################################################
# partition固定分成3份，左一份，匹配一份，右边一份。#
# split默认分割，匹配的去掉，剩下的各自成一份。可以指定分成几份的。
# partition and split
#
# ('spli', 't', 'partition')
# ('splitparti', 't', 'ion')
# ['spli', 'par', 'i', 'ion']
# ['spli', 'partition']
# ['spli', 'par', 'ition']
# ['spli', 'par', 'i', 'ion']
# ['splitparti', 'ion']
# ['splitpar', 'i', 'ion']
test = "splitpartition"
v1 = test.partition("t")
v2 = test.rpartition("t")
v3 = test.split("t")
v4 = test.split("t", 1)
v5 = test.split("t", 2)
v6 = test.rsplit("t")
v7 = test.rsplit("t", 1)
v8 = test.rsplit("t", 2)

print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)
print(v7)
print(v8)

# 只能分割换行符
#
# ['asd', 'sdf', 'dsdf']
# ['asd\n', 'sdf\n', 'dsdf\n']
test = "asd\nsdf\ndsdf\n"
v1 = test.splitlines()
v2 = test.splitlines(True)
print(v1)
print(v2)

# 在Python中，字符串是不可以改变的，这一点与Java类似。 ################################
# 如果字符串加法拼接或者调用函数，那么返回的是一个新的字符串，也就是内存中的一块新区域。
# 我们以replace函数为例。

# kevinkevinkevinkevin
# kaxeinkaxeinkevinkevin
s1 = "kevinkevinkevinkevin"
s2 = s1.replace("ev", "axe", 2)
print(s1)
print(s2)
