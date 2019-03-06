#！ -*- coding:utf-8 -*-

class Stack(object):
    def __init__(self):
        self.item = []

    def push(self, ele):
        self.item.append(ele)

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.item.pop()

    def size(self):
        return len(self.item)

    def is_empty(self):
        return self.size() == 0


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(9)
    s.push(3)

    for i in range(0, 6):
        print("current size: %d , pop element :%s " % (s.size(), s.pop()))