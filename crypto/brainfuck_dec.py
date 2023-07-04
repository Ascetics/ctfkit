# -*- coding:utf8 -*-
#
# https://github.com/pocmo/Python-Brainfuck
from crypto import brainfuck

sourcecode = """
    ++++++++++[>+++++++>++++++++++>+++>+<<<<-]
    >++.>+.+++++++..+++.>++.<<+++++++++++++++.
    >.+++.------.--------.>+.>.
  """

brainfuck.evaluate(sourcecode)



