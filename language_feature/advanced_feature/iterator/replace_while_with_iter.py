import sys
f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
    sys.stdout.write(chunk)
    break

"""
iter(iterable) -> iterator
iter(callable, sentinel) -> iterator
"""

