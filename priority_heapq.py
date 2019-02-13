#! -*- coding:utf-8 -*-

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        print(self._queue)
        heapq.heappush(self._queue, (-priority, self._index, item))
        print(self._queue)
        self._index += 1

    def pop(self):
        print(self._queue)
        ele = heapq.heappop(self._queue)[-1]
        print(self._queue)
        return ele

    def length(self):
        return len(self._queue)


class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "Item({!r})".format(self.name)


def test_priority_queue():
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    q.push(Item('suck'), 5)

    for i in range(0, q.length()):
        print(q.pop())


if __name__ == "__main__":
    test_priority_queue()