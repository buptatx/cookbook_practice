#! -*- coding:utf-8 -*-


def is_int(item):
    try:
        int(item)
        return True
    except ValueError:
        return False


def test_filter(data):
    res = list(filter(is_int, data))
    print(res)
   

if __name__ == "__main__":
    value = ['1', '2', '-3', '-', '4', 'N/A', '5', 1, 1.2312, False]
    test_filter(value)