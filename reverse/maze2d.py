# -*- coding:utf8 -*-
"""
二维迷宫，深度优先算法
MAZE = ['WWWWWWWWWWWWWWW',
        'WA$$WWWWWW$$$$W',
        'WWW$WWWWW$$WW$W',
        'W$$$WWWWW$WWW$W',
        'W$WWWWWWW$WWW$W',
        'W$WWWWWWW$W$$$W',
        'W$$$$$WWW$W$WWW',
        'WWWWW$WWW$W$WWW',
        'WWWWW$WWW$W$$$W',
        'WWW$$$WW$$WWW$W',
        'WWW$WWWW$WW$$$W',
        'W$$$WW$$$WW$WWW',
        'W$WWWW$WWWW$WWW',
        'W$$$$$$WWWW$$EW',
        'WWWWWWWWWWWWWWW', ]
0上，1右，2下，3左
路径操作：11223322211112223322332211111001100100000001011122223322211223322211
"""

START = 'A'  # 起点
FINISH = 'E'  # 终点
PASS = '$'  # 通路
WALL = 'W'  # 墙壁不通
MAZE_ROW = 15  # 迷宫行数
MAZE_COL = 15  # 迷宫列数
# 迷宫
MAZE = ['WWWWWWWWWWWWWWW',
        'WA$$WWWWWW$$$$W',
        'WWW$WWWWW$$WW$W',
        'W$$$$$$WW$WWW$W',
        'W$WWWWWWW$WWW$W',
        'W$WWWWWWW$W$$$W',
        'W$$$$$WWW$W$WWW',
        'WWWWW$WWW$W$WWW',
        'WWWWW$WWW$W$$$W',
        'WWW$$$WW$$WWW$W',
        'WWW$WWWW$WW$$$W',
        'W$$$WW$$$WW$WWW',
        'W$WWWW$WWWW$WWW',
        'W$$$$$$WWWW$$EW',
        'WWWWWWWWWWWWWWW', ]
VISIT = [[0 for j in range(MAZE_COL)] for i in range(MAZE_ROW)]  # 辅助标记
UP = 0  # 上
DOWN = 2  # 下
LEFT = 3  # 左
RIGHT = 1  # 右
FOUND = False  # 到达终点
RESULT = []  # 路径操作


def help2d(i, j):
    global START, FINISH, WALL, PASS, MAZE, MAZE_ROW, MAZE_COL
    global VISIT, UP, DOWN, LEFT, RIGHT, FOUND, RESULT
    VISIT[i][j] = 1
    for step in {UP, DOWN, LEFT, RIGHT}:
        newi, newj = i, j
        if step == UP:
            newi -= 1
        elif step == DOWN:
            newi += 1
        elif step == LEFT:
            newj -= 1
        elif step == RIGHT:
            newj += 1

        if (0 <= newi < MAZE_ROW and 0 <= newj < MAZE_COL) and \
            (MAZE[newi][newj] == PASS or MAZE[newi][newj] == FINISH) and \
            VISIT[newi][newj] == 0:
            if MAZE[newi][newj] == PASS:
                help2d(newi, newj)
                if FOUND:
                    RESULT.append(step)  # 到达终点时才记录路径
            elif MAZE[newi][newj] == FINISH:
                FOUND = True
                RESULT.append(step)
                print('Bingo!')
                return


if __name__ == '__main__':
    help2d(1, 1)
    RESULT.reverse() # 递归记录，需要反向
    for x in RESULT:
        print(x, end='')
