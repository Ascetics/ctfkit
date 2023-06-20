# -*- coding:utf8 -*-
"""
Z3 是微软研发的定理证明器
CTF时可以解决一些数学问题
本例解二元一次方程组
"""
from z3 import Int, Solver

# 定义变量
x = Int('x')
y = Int('y')

# 约束条件
solver = Solver()
solver.add(x + y == 5)
solver.add(x - y == 1)

# 解答
print(solver.check())
print(solver.model())
