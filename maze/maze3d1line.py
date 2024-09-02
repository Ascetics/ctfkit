# -*- coding:utf8 -*-
"""
三维迷宫，深度优先算法，迷宫是一行字符串
"""
START = '@'  # 起点
FINISH = '&'  # 终点
PASS = '*'  # 通路
WALL = '#'  # 墙壁不通
MAZE_X = 7  # 迷宫X数
MAZE_Y = 7  # 迷宫Y数
MAZE_Z = 7  # 迷宫Z数

MAZE = (
    '##****###*##*###########***####*#*####*#*####*###'
    '########**##*##############***####*#**###*##**##*'
    '##**####*#*#*##*#***##**###*##****##############*'
    '***####*######*######*##@##**####**#############*'
    '##################**####**##**######**######***#*'
    '########*######*###*#**###*#####*######*######*#*'
    '#***####*#****######**####*******#######&######**')
VISIT = [0 for z in range(MAZE_Z)
         for y in range(MAZE_Y)
         for x in range(MAZE_X)]  # 辅助标记

# 三维坐标（二维数组的坐标）为z坐标
# 每个二维数组 二维坐标是y坐标，一维坐标是z坐标，定义坐标为（x,y,z）
Z_MINUS, Z_PLUS = 'o', 'i'
Y_MINUS, Y_PLUS = 'w', 's'
X_MINUS, X_PLUS = 'a', 'd'
RESULT = []  # 路径操作


def help3d(x, y, z):
    global START, FINISH, WALL, PASS, MAZE, MAZE_Z, MAZE_Y, MAZE_X, VISIT
    global Z_MINUS, Z_PLUS, Y_MINUS, Y_PLUS, X_MINUS, X_PLUS, RESULT

    index = z * MAZE_Y * MAZE_X + y * MAZE_X + x  # (x,y,z)转换为字符串下标
    VISIT[index] = 1

    if MAZE[index] == FINISH:
        print(''.join(RESULT))
        return

    for step in (Z_MINUS, Z_PLUS, Y_MINUS, Y_PLUS, X_MINUS, X_PLUS,):
        newz, newy, newx = z, y, x
        if step == Z_MINUS:
            newz -= 1
        elif step == Z_PLUS:
            newz += 1
        elif step == Y_MINUS:
            newy -= 1
        elif step == Y_PLUS:
            newy += 1
        elif step == X_MINUS:
            newx -= 1
        elif step == X_PLUS:
            newx += 1
        newindex = newz * MAZE_Y * MAZE_X + newy * MAZE_X + newx
        if (
                0 <= newx < MAZE_X and 0 <= newy < MAZE_Y and 0 <= newz < MAZE_Z
                and (MAZE[newindex] == PASS or MAZE[newindex] == FINISH)
                and VISIT[newindex] == 0
        ):
            RESULT.append(step)
            help3d(newx, newy, newz)
            RESULT.pop(-1)
            VISIT[newindex] = 0


if __name__ == '__main__':
    help3d(3, 3, 3)
