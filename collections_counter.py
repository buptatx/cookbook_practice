#! -*- coding:utf-8 -*-

from collections import Counter


def test_counter():
    cwords = []
    with open("./collections_counter.py", "r", encoding="utf-8") as mf:
        cwords = mf.read().replace("\n", "").split(" ")

    word_counts = Counter([i for i in cwords if i != ""])
    print(word_counts)
    top_three = word_counts.most_common(3)
    print(top_three)

if __name__ == "__main__":
    test_counter()