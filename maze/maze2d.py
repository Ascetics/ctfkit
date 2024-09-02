# -*- coding:utf8 -*-
"""
二维迷宫，深度优先算法，迷宫是字符串列表
MAZE = ['WAWWWWWWWWWWWWW', #--Y
        'W$$$WWWWWW$$$$W',
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
#        |
#        X
0上，1右，2下，3左
起点A坐标(0, 1)
终点E坐标(14, 14)
路径操作：211223322211112223322332211111001100100000001011122223322211223322211
"""

START = 'A'  # 起点
FINISH = 'E'  # 终点
PASS = '$'  # 通路
WALL = 'W'  # 墙壁不通
MAZE_X = 15  # 迷宫行数
MAZE_Y = 15  # 迷宫列数
# 迷宫
MAZE = ['WAWWWWWWWWWWWWW',
        'W$$$WWWWWW$$$$W',
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
VISIT = [[0 for y in range(MAZE_Y)] for x in range(MAZE_X)]  # 辅助标记
UP = '0'  # 上
DOWN = '2'  # 下
LEFT = '3'  # 左
RIGHT = '1'  # 右
RESULT = []  # 路径操作


def help2d(x, y):
    global START, FINISH, WALL, PASS, MAZE, MAZE_X, MAZE_Y
    global VISIT, UP, DOWN, LEFT, RIGHT, RESULT

    VISIT[x][y] = 1

    if MAZE[x][y] == FINISH:
        print(''.join(RESULT))
        return

    for step in (UP, DOWN, LEFT, RIGHT,):
        newx, newy = x, y
        if step == UP:
            newx -= 1
        elif step == DOWN:
            newx += 1
        elif step == LEFT:
            newy -= 1
        elif step == RIGHT:
            newy += 1
        if (
            0 <= newx < MAZE_X and 0 <= newy < MAZE_Y
            and VISIT[newx][newy] == 0.
            and (MAZE[newx][newy] == PASS or MAZE[newx][newy] == FINISH)
        ):
            RESULT.append(step)
            help2d(newx, newy)
            RESULT.pop(-1)
            VISIT[newx][newy] = 0


if __name__ == '__main__':
    help2d(0, 1)
