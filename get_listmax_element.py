#! -*- coding:utf-8 -*-


def get_max(mlist):
    if len(mlist) == 0:
        return 0
    elif len(mlist) == 1:
        return mlist[0]
        
    temp = 0
    for i in mlist:
        temp = i if i>temp else temp

    return temp


if __name__ == "__main__":
    x = [1,2,23,4,5,6,0]
    y = get_max(x)
    print(y)
    print(max(x))
    x.sort(reverse=True)
    print(x[0])