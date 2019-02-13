#! -*- coding:utf-8 -*-

from collections import defaultdict
from itertools import groupby
from operator import itemgetter


def sort_with_defaultdict(data):
    temp = defaultdict(list)
    for i in data:
        temp[i["date"]].append(i)

    print(temp)


def sort_and_groupby_dict(data):
    data.sort(key=itemgetter('date'))
    for date, item in groupby(data, key=itemgetter('date')):
        print(date)
        for i in item:
            print(" ", i)


if __name__ == "__main__":
    data = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]
    sort_with_defaultdict(data)
    print(" "*20)
    sort_and_groupby_dict(data)