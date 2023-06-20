# -*- coding:utf8 -*-
"""
二维迷宫，深度优先算法，迷宫是一行字符串
MAZE = ['#+0000000000000', #--Y
        '#0#########0##0',
        '#000#####000##0',
        '###0#####0####0',
        '#000#####0####0',
        '#0#######&000#0',
        '#000000000##000', ]
#        |
#        X
w上，s下，a左，d右
起点+坐标(0, 1)
终点&坐标(7, 9)
路径操作3个：
ssddssaassddddddddw
ddddddddddssaasss
dddddddddddddssssssaawaaa
"""

START = '+'  # 起点
FINISH = '&'  # 终点
PASS = '0'  # 通路
WALL = '#'  # 墙壁不通
MAZE_X = 7  # 迷宫行数
MAZE_Y = 15  # 迷宫列数
# 迷宫
MAZE = ('#+0000000000000'
        '#0#########0##0'
        '#000#####000##0'
        '###0#####0####0'
        '#000#####0####0'
        '#0#######&000#0'
        '#000000000##000'
        )
VISIT = [0 for y in range(MAZE_Y) for x in range(MAZE_X)]  # 辅助标记
UP = 'w'  # 上
DOWN = 's'  # 下
LEFT = 'a'  # 左
RIGHT = 'd'  # 右
RESULT = []  # 路径操作


def help2d(x, y):
    global START, FINISH, WALL, PASS, MAZE, MAZE_X, MAZE_Y
    global VISIT, UP, DOWN, LEFT, RIGHT, RESULT

    VISIT[x * MAZE_Y + y] = 1

    if MAZE[x * MAZE_Y + y] == FINISH:
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
            and VISIT[newx * MAZE_Y + newy] == 0.
            and (
                MAZE[newx * MAZE_Y + newy] == PASS
                or MAZE[newx * MAZE_Y + newy] == FINISH
        )
        ):
            RESULT.append(step)
            help2d(newx, newy)
            RESULT.pop(-1)
            VISIT[newx * MAZE_Y + newy] = 0


if __name__ == '__main__':
    help2d(0, 1)
