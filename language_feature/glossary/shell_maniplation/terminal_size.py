import os

sz = os.get_terminal_size()
print(sz)
print(sz.columns)
print(sz.lines)
sz = os.terminal_size((50, 24))
