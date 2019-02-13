#! -*- coding:utf-8 -*-

from collections import defaultdict


def test_defaultdict():
    d = defaultdict(list)
    pairs = [('a',1), ('a',2), ('b',4)]
    for key, value in pairs:
        print(key + " " + str(value))
        d[key].append(value)

    print(d)
    for ik in d.keys():
        print(d.get(ik))


def test_setdefault():
    strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
    counts = {}

    for kw in strings:
        counts[kw] = counts.setdefault(kw, 0) + 1

    print(counts)


if __name__ == "__main__":
    test_defaultdict()
    test_setdefault()