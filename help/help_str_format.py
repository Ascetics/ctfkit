# -*- coding:utf8 -*-

msg = list()
# %s 接收字符串
msg.append("i am %s, which is a database." % "mysql")
msg.append("i am %s, which is a %s." % ("db2", "database"))
msg.append("i am %s, which is a %s, %s." % ("oracle", "database", "too"))
msg.append("these are database, %s" % (["mysql", "db2", "oracle"]))

name = "Kevin"
age = 29
# %s可以接收任意变量，将其转换为字符串。这样做可读性差，建议还是根据数据类型用不同的%
msg.append("i am %s, age %s." % (name, age))
msg.append("i am %s, age %d." % (name, age))
msg.append("percent is %s" % 99.769273703747)

# %f 接收浮点数，默认保留6位小数。# percent is 99.769273703747
msg.append("percent is %f" % 99.769273703747)
# 保留2位小数，四舍五入。# percent is 99.77
msg.append("percent is %.2f" % 99.769273703747)
# 打印百分号。 percent is 99.77 %
msg.append("percent is %.2f %%" % 99.769273703747)

# 事实上，字符串格式化遵循下面的格式
# %[(name)][flag][width][.precision]type
# name是用来替换的键名
# flag有+-空格0
# flag +表示右对齐，正数前加+，负数前加-
# flag -表示左对齐，正数前不加，负数前加-
# flag 空格表示右对齐，正数前加空格，负数前加-
# flag 0表示右对齐，正数前啥都不加，负数前加-
# width表示对齐宽度
# .precision表示浮点数保留小数位
tpl = "i am %(name)-10s, age %(age)3d, percent %(pp)8.2f %%"
# i am Kevin     , age   9, percent    98.39 %
# i am Jeffson   , age 136, percent  -192.34 %
# i am Urazimil  , age  69, percent    93.10 %
msg.append(tpl % ({"name": "Kevin", "age": 9, "pp": 98.39263}))
msg.append(tpl % ({"name": "Jeffson", "age": 136, "pp": -192.3439263}))
msg.append(tpl % ({"name": "Urazimil", "age": 69, "pp": 93.1}))

# 字典方式格式化，对比字符串的格式化方法，这种方式更灵活多样.
# 如果使用了%s %d 或 %f等方式格式化，那么输出百分号符号的方法就是%%
msg.append(
    "i am %(name)s, age %(age)d, percent %(pp).2f %%."
    % ({"name": "Kevin", "age": 19, "pp": 97.562333477})
)

# 除了以上%格式符号，还有format方法格式化
# 没有使用%s %d 或 %f等方式格式化，那么输出百分号符号就是%
tpl = "i am {name}, age {age}, percent {pp} %."
msg.append(tpl.format(name="Kevin", pp=97.562333477, age=29))
msg.append(tpl.format(**{"name": "Kevin", "age": 29, "pp": 97.562333477}))
msg.append(tpl.format_map({"name": "Kevin", "age": 29, "pp": 97.562333477}))
tpl = "i am {2}, age {0}, percent {1} %."
msg.append(tpl.format(29, 97.56233347, "Kevin"))

# 还有这种方式，取后面传入的第几个列表的第几个元素。
tpl = "i am {0[0]}, age {0[1]}, percent {0[0]} %."
msg.append(tpl.format([1, 2, 3], [11, 22, 33]))
tpl = "i am {1[0]}, age {1[1]}, percent {1[0]} %."
msg.append(tpl.format([1, 2, 3], [11, 22, 33]))

# 还有这种方式，*取出列表里的元素？暂时没搞懂以后搞懂。
tpl = "i am {:s}, age {:d}, percent {:f} %."
msg.append(tpl.format(*["Kevin", 29, 97.562333477]))

# 再了解其他介个格式化符号
# :b for binary 二进制方式显示数字
# :o for octoanry 八进制方式显示数字
# :d for decimal 十进制方式显示数字
# :x,:X for hexadecimal 十六进制方式显示数字，x小写，X大写
# :% for percent 以百分比方式显示，取小数点后6位，自带百分号
# numbers: 1111, 17, 15, f, F, 1595.272937%
tpl = "numbers: {:b}, {:o}, {:d}, {:x}, {:X}, {:%}"
msg.append(tpl.format(*[15, 15, 15, 15, 15, 15.952729374]))

for i in msg:
    print(i)
    pass

# for输出结果
# i am mysql, which is a database.
# i am db2, which is a database.
# i am oracle, which is a database, too.
# these are database, ['mysql', 'db2', 'oracle']
# i am Kevin, age 29.
# i am Kevin, age 29.
# percent is 99.769273703747
# percent is 99.769274
# percent is 99.77
# percent is 99.77 %
# i am Kevin     , age   9, percent    98.39 %
# i am Jeffson   , age 136, percent  -192.34 %
# i am Urazimil  , age  69, percent    93.10 %
# i am Kevin, age 19, percent 97.56 %.
# i am Kevin, age 29, percent 97.562333477 %.
# i am Kevin, age 29, percent 97.562333477 %.
# i am Kevin, age 29, percent 97.562333477 %.
# i am Kevin, age 29, percent 97.56233347 %.
# i am 1, age 2, percent 1 %.
# i am 11, age 22, percent 11 %.
# i am Kevin, age 29, percent 97.562333 %.
# numbers: 1111, 17, 15, f, F, 1595.272937%