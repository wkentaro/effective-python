from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from Queue import deque
from Queue import Queue
import time
from threading import Lock
from threading import Thread


def main():
    in_queue = Queue()

    def consumer():
        print('Consumer waiting')
        work = in_queue.get()  # second done
        print('Consumer working')
        # working
        # ...
        print('Consumer done')
        in_queue.task_done()  # third done

    Thread(target=consumer).start()

    in_queue.put(object())  # first done
    print('Producer waiting')
    in_queue.join()  # forth done
    print('Producer done')


if __name__ == '__main__':
    main()
