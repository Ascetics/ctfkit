"""
polybius密码，也叫棋盘密码
"""

TAB = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'ij', 'k'],
    ['l', 'm', 'n', 'o', 'p'],
    ['q', 'r', 's', 't', 'u'],
    ['v', 'w', 'x', 'y', 'z']]


def resovle(string):
    ms = ['']
    for i in range(0, len(string), 2):
        line, col = int(string[i]), int(string[i + 1])
        if 1 <= line <= 5 and 1 <= col <= 5:
            temp = []
            for m in ms:
                if line == 2 and col == 4:
                    temp.append(m + 'i')
                    temp.append(m + 'j')
                else:
                    temp.append(m + TAB[line - 1][col - 1])
            ms = temp
        else:
            raise IndexError(str(line) + ',' + str(col))
    return ms


def main():
    c_msg = '4423244324433534315412244543'
    m_msg = resovle(c_msg)
    for s in m_msg:
        print(s)
    pass


if __name__ == '__main__':
    main()
