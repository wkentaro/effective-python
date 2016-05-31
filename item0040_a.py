from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def my_coroutine():
    while True:
        received = yield
        print('Received:', received)


it = my_coroutine()
next(it)
it.send('First')
it.send('Second')
