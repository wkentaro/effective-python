from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from Queue import deque
from Queue import Queue
import time
from threading import Lock
from threading import Thread


def main():
    queue = Queue()

    def consumer():
        print('Consumer waiting')
        queue.get()
        print('Consumer done')

    thread = Thread(target=consumer)
    thread.start()

    print('Producer putting')
    queue.put(object())
    thread.join()
    print('Producer done')


if __name__ == '__main__':
    main()
