#! -*- coding:utf-8 -*-

import heapq

num = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
large_three = heapq.nlargest(3, num)
small_three = heapq.nsmallest(3, num)

#heapq
print("largest three with heapq: " + ", ".join([str(x) for x in large_three]))
print("smallest three with heapq: " + ", ".join([str(x) for x in small_three]))
#min max
print("largest one with max:" + str(max(num)))
print("smallest one with min:" + str(min(num)))
#sort
print("largest three with sorted and slice: " + ", ".join([str(x) for x in sorted(num)[-3:][::-1]]))
print("smallest three with sorted and slice: " + ", ".join([str(x) for x in sorted(num)[:3]]))