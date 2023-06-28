# -*- coding:utf8 -*-
"""
FPS游戏操作用ASDW控制前后左右，画出轨迹
"""
import matplotlib.pyplot as plt

f = open('fps.txt', 'r')
lines = f.readlines()
f.close()

line = lines[0]
print(line)

point_color = 'red'
space_color = 'white'
x = [0]
y = [0]
color = [point_color]

for c in line:
    if c == 'd':
        x.append(x[-1] + 1)
        y.append(y[-1])
        color.append(point_color)
    elif c == 'a':
        x.append(x[-1] - 1)
        y.append(y[-1])
        color.append(point_color)
    elif c == 'w':
        x.append(x[-1])
        y.append(y[-1] + 1)
        color.append(point_color)
    elif c == 's':
        x.append(x[-1])
        y.append(y[-1] - 1)
        color.append(point_color)
    elif c == 'e':
        x.append(x[-1] + 1)
        y.append(y[-1])
        color.append(space_color)


fig, ax = plt.subplots()
ax.scatter(x, y, s=10, c=color)
plt.axis('equal')
# ax.set_aspect(aspect=1.)
plt.show()
