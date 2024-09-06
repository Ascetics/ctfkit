# -*- coding:utf8 -*-
"""
二维迷宫DFS算法
一维数组是X，第二维度是Y
"""

START = 'S'  # 起点
FINISH = 'E'  # 终点
PASS = '1'  # 通路
WALL = '0'  # 墙壁不通
MAZE_X = 26  # 迷宫第一维度
MAZE_Y = 25  # 迷宫第二维度
# 迷宫
MAZE = ('S0000000000000000000000000'
        '11101111110000111111111000'
        '00101000011110100101001100'
        '01101011010011100101000100'
        '00111001110000011101001100'
        '01001100011011110001010000'
        '01000100001010001111011100'
        '01111101110010000100000100'
        '01000001010111000100010100'
        '01111111010001011111110100'
        '01010000010101000000010100'
        '01010111110101111011110110'
        '01010100000100001010000100'
        '01000100010111111010000100'
        '01010111110001000010111100'
        '01010000001011011110100100'
        '01011111101010010000100100'
        '01000100101010110111111100'
        '01011111111010100100101000'
        '01000100100011110100101110'
        '01110110000010010100001010'
        '01000011111110011101111010'
        '01000000000000000001000010'
        '011111111111100001111111E0'
        '00000000000000000000000000')
VISIT = [0 for y in range(MAZE_Y) for x in range(MAZE_X)]  # 辅助标记
Y_MINUS = 'w'
Y_PLUS = 's'
X_MINUS = 'a'
X_PLUS = 'd'
RESULT = []  # 路径操作


def help2d(x, y):
    global START, FINISH, WALL, PASS, MAZE, MAZE_X, MAZE_Y
    global VISIT, Y_MINUS, Y_PLUS, X_MINUS, X_PLUS, RESULT

    index = y * MAZE_X + x
    VISIT[index] = 1

    if MAZE[y * MAZE_X + x] == FINISH:
        print(''.join(RESULT))
        return

    for step in (Y_MINUS, Y_PLUS, X_MINUS, X_PLUS,):
        newx, newy = x, y
        if step == Y_MINUS:
            newy -= 1
        elif step == Y_PLUS:
            newy += 1
        elif step == X_MINUS:
            newx -= 1
        elif step == X_PLUS:
            newx += 1
        newindex = newy * MAZE_X + newx
        if (
                0 <= newx < MAZE_X and 0 <= newy < MAZE_Y
                and VISIT[newindex] == 0.
                and (MAZE[newindex] == PASS or MAZE[newindex] == FINISH
        )
        ):
            RESULT.append(step)
            help2d(newx, newy)
            RESULT.pop(-1)
            VISIT[newindex] = 0


if __name__ == '__main__':
    help2d(0, 0)
