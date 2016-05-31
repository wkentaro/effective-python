from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)


it = minimize()
next(it)
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))
