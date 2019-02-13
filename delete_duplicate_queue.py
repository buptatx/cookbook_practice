#! -*- coding:utf-8 -*-

def dedupe(item):
    res = set()
    for i in item:
        if i not in res:
            yield i
            res.add(i)


if __name__ == "__main__":
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))