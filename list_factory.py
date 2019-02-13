#! -*- coding:utf-8 -*-

from collections import namedtuple

def test_namedtuple(data):
    stock = namedtuple("Stock", ['name', 'share', 'price'])
    total = 0.0
    for item in data:
        sitem = stock(*item)
        total += sitem.share*sitem.price

    print(total)


if __name__ == "__main__":
    data = [('ACME', 100, 123.45),
        ('IT', 10, 50)]
    test_namedtuple(data)