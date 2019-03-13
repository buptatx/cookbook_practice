#! -*- coding:utf-8 -*-

def get_sum(n):
    if n == 1:
        return n
    else:
        return get_sum(n-1) + n

def get_duplicate_number(inlist):
    c_sum = sum(inlist)
    o_sum = get_sum(len(inlist) -1)
    return c_sum - o_sum


if __name__ == "__main__":
    res = get_duplicate_number([1,2,3,4,5,6,2])
    print(res)