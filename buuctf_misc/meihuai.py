import matplotlib.pyplot as plt
'''
buuctf misc 梅花香之苦寒来
'''

with open('meihuai.txt', 'r') as f:
    string = f.readline()

    # 删除括号 ascii 0x28 0x29; 分割坐标 ascii 0x0a; 注意去掉最后一个空字符串
    strings = string.replace('28', '').replace('29', '').split('0a')[:-1]
    # 转换坐标 '372c313233'->['37','313233']->['7', '123']->(7,123)
    coordinates = list(map(
        lambda s: tuple(map(lambda s_ascii: int(s_ascii[1::2]), s.split('2c'))),
        strings))
    x = list(map(lambda c: c[0], coordinates))
    y = list(map(lambda c: c[1], coordinates))
    plt.figure()
    plt.scatter(x, y, s=1)
    plt.axis('equal')
    plt.savefig('meihuai.png')
