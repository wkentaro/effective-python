from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from Queue import deque
from Queue import Queue
import time
from threading import Lock
from threading import Thread


def main():
    queue = Queue(1)

    def consumer():
        time.sleep(0.01)
        queue.get()
        print('Consumer got 1')
        queue.get()
        print('Consumer got 2')

    thread = Thread(target=consumer)
    thread.start()

    queue.put(object())
    print('Producer put 1')
    queue.put(object())
    print('Producer put 2')
    thread.join()
    print('Producer done')


if __name__ == '__main__':
    main()
