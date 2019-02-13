#! -*- coding:utf-8 -*-

import json
from collections import OrderedDict


def test_ordereddict():
    d = OrderedDict()
    d["foo"] = 1
    d['1'] = 11
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    d['foo'] = 5


    n = {}
    n["foo"] = 1
    n['1'] = 11
    n["bar"] = 2
    n["spam"] = 3
    n["grok"] = 4


    for ik in d:
        print(ik + str(d[ik]))

    for k,v in d.items():
        print(k + str(v))

    print(json.dumps(d))
    print(d.keys())
    print("-"*10)

    for ik in n:
        print(ik + str(n[ik]))

    for k,v in n.items():
        print(k + str(v))
    print(json.dumps(n))
    print(n.keys())
    print("-"*10)

    sorted(n)
    print(json.dumps(n))
    print(n.keys())

if __name__ == "__main__":
    test_ordereddict()