# -*- coding:utf8 -*-
#
# https://github.com/pocmo/Python-Brainfuck
from misc_cipher import brainfuck

sourcecode = """
    ++++++++++[>+++++++>++++++++++>+++>+<<<<-]
    >++.>+.+++++++..+++.>++.<<+++++++++++++++.
    >.+++.------.--------.>+.>.
  """

brainfuck.evaluate(sourcecode)



