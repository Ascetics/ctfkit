# -*- coding:utf8 -*-
"""
三维迷宫，深度优先算法，迷宫是二维字符串列表
从@经过*走到&，键盘ad控制z的-+，键盘ws控制y的-+，键盘oi控制x的-+
二维数组为x坐标，每个二维数组 行是y坐标，列是z坐标，定义坐标为（x,y,z）
z[0]
##****#
##*##*#
#######
###***#
###*#*#
###*#*#
###*###
z[1]
#######
#**##*#
#######
######*
**####*
#**###*
##**##*
z[2]
##**###
#*#*#*#
#*#***#
#**###*
##****#
#######
######*
z[3]
***####
*######
*######
*##@##*
*####**
#######
######*
z[4]
#######
#######
####**#
###**##
**#####
#**####
##***#*
z[5]
#######
#*#####
#*###*#
**###*#
####*##
####*##
####*#*
z[6]
#***###
#*#****
######*
*####**
*****##
#####&#
#####**

操作路径：
idwdisidwwaaawaasossaisddddossoaawawaowwwwddodssddwoowaaasiaissdsdddidwoosssiiiiiaw
"""
START = '@'  # 起点
FINISH = '&'  # 终点
PASS = '*'  # 通路
WALL = '#'  # 墙壁不通
MAZE_X = 7  # 迷宫X数
MAZE_Y = 7  # 迷宫Y数
MAZE_Z = 7  # 迷宫Z数
# 迷宫，二维数组为x坐标，每个二维数组 行是y坐标，列是z坐标，定义坐标为（x,y,z）
MAZE = [
    ['##****#',
     '##*##*#',
     '#######',
     '###***#',
     '###*#*#',
     '###*#*#',
     '###*###', ],
    ['#######',
     '#**##*#',
     '#######',
     '######*',
     '**####*',
     '#**###*',
     '##**##*', ],
    ['##**###',
     '#*#*#*#',
     '#*#***#',
     '#**###*',
     '##****#',
     '#######',
     '######*', ],
    ['***####',
     '*######',
     '*######',
     '*##@##*',
     '*####**',
     '#######',
     '######*', ],
    ['#######',
     '#######',
     '####**#',
     '###**##',
     '**#####',
     '#**####',
     '##***#*', ],
    ['#######',
     '#*#####',
     '#*###*#',
     '**###*#',
     '####*##',
     '####*##',
     '####*#*', ],
    ['#***###',
     '#*#****',
     '######*',
     '*####**',
     '*****##',
     '#####&#',
     '#####**', ],
]
VISIT = [[[0 for z in range(MAZE_Z)] for y in range(MAZE_Y)] for x in
         range(MAZE_X)]  # 辅助标记

# 二维数组为x坐标，每个二维数组 行是y坐标，列是z坐标，定义坐标为（x,y,z）
X_MINUS, X_PLUS = 'o', 'i'
Y_MINUS, Y_PLUS = 'w', 's'
Z_MINUS, Z_PLUS = 'a', 'd'
RESULT = []  # 路径操作


def help3d(x, y, z):
    global START, FINISH, WALL, PASS, MAZE, MAZE_Z, MAZE_Y, MAZE_X, VISIT
    global X_MINUS, X_PLUS, Y_MINUS, Y_PLUS, Z_MINUS, Z_PLUS, RESULT

    VISIT[x][y][z] = 1

    if MAZE[x][y][z] == FINISH:
        print(''.join(RESULT))
        return

    for step in (X_MINUS, X_PLUS, Y_MINUS, Y_PLUS, Z_MINUS, Z_PLUS,):
        newx, newy, newz = x, y, z
        if step == X_MINUS:
            newx -= 1
        elif step == X_PLUS:
            newx += 1
        elif step == Y_MINUS:
            newy -= 1
        elif step == Y_PLUS:
            newy += 1
        elif step == Z_MINUS:
            newz -= 1
        elif step == Z_PLUS:
            newz += 1

        if (
            0 <= newx < MAZE_X and 0 <= newy < MAZE_Y and 0 <= newz < MAZE_Z
            and (
                MAZE[newx][newy][newz] == PASS
                or MAZE[newx][newy][newz] == FINISH
            )
            and VISIT[newx][newy][newz] == 0
        ):
            RESULT.append(step)
            help3d(newx, newy, newz)
            RESULT.pop(-1)
            VISIT[newx][newy][newz] = 0


if __name__ == '__main__':
    help3d(3, 3, 3)
