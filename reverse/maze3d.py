# -*- coding:utf8 -*-
"""
三维迷宫，深度优先算法
从@经过*走到&，键盘ad控制x的-+，键盘ws控制y的-+，键盘oi控制z的-+
二维数组为z坐标，每个二维数组 行是y坐标，列是x坐标，定义坐标为（z,y,x）
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
"""
START = '@'  # 起点
FINISH = '&'  # 终点
PASS = '*'  # 通路
WALL = '#'  # 墙壁不通
MAZE_X = 7  # 迷宫X数
MAZE_Y = 7  # 迷宫Y数
MAZE_Z = 7  # 迷宫Z数字
# 迷宫，二维数组为z坐标，每个二维数组 行是y坐标，列是x坐标，定义坐标为（z,y,x）
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
VISIT = [[[0 for k in range(MAZE_Z)] for j in range(MAZE_Y)] for i in
         range(MAZE_X)]  # 辅助标记

# 二维数组为z坐标，每个二维数组 行是y坐标，列是x坐标，定义坐标为（z,y,x）
X_MINUS, X_PLUS = 'a', 'd'
Y_MINUS, Y_PLUS = 'w', 's'
Z_MINUS, Z_PLUS = 'o', 'i'
FOUND = False  # 到达终点
RESULT = []  # 路径操作


def help3d(z, y, x):
    global START, FINISH, WALL, PASS, MAZE, MAZE_X, MAZE_Y, MAZE_Z, VISIT
    global X_MINUS, X_PLUS, Y_MINUS, Y_PLUS, Z_MINUS, Z_PLUS, FOUND, RESULT
    VISIT[z][y][x] = 1
    for step in {X_MINUS, X_PLUS, Y_MINUS, Y_PLUS, Z_MINUS, Z_PLUS}:
        newz, newy, newx = z, y, x
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

        if (0 <= newx < MAZE_X and 0 <= newy < MAZE_Y and 0 <= newz < MAZE_Z) \
            and \
            (MAZE[newz][newy][newx] == PASS or
             MAZE[newz][newy][newx] == FINISH) \
            and VISIT[newz][newy][newx] == 0:
            if MAZE[newz][newy][newx] == PASS:
                help3d(newz, newy, newx)
                if FOUND:
                    RESULT.append(step)  # 到达终点时才记录路径
            elif MAZE[newz][newy][newx] == FINISH:
                FOUND = True
                RESULT.append(step)
                print('Bingo!')
                return


if __name__ == '__main__':
    help3d(3, 3, 3)
    RESULT.reverse()  # 递归记录，需要反向
    for x in RESULT:
        print(x, end='')
