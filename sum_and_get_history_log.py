#！ -*- coding:utf-8 -*-

from collections import deque

def my_sum(item):
    head, *tail = item
    res = head + my_sum(tail) if tail else head
    print(tail)
    return res


def get_keyline(fhandle, keyword, maxlen):
    prelines = deque(maxlen=maxlen)
    for line in fhandle:
        if keyword in line:
            yield line, prelines
        prelines.append(line)


def test_get_keyline(filename, keyword, maxlen):
    with open(filename, "r", encoding="utf-8") as mf:
        for line, prelines in get_keyline(mf, keyword, 5):
            for preline in prelines:
                print(preline, end='')
            print(line, end='')
            print("="*10)


def test_my_sum():
    inp = [10, 8, 9, 7, 6,4, 1,2,3]
    print(my_sum(inp))
    print(sum(inp))


def test_get_k():
    test_get_keyline("./overcook.py",'print', 5)       


if __name__ == "__main__":
    test_get_k()
