#！ -*- coding:utf-8 -*-

import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

#捕获分组，命中的关键字符也会被存放到结果中
res = re.split(r"(;|,|\s)\s*", line)
print(res)

#命中的关键字不会被存放到结果中
res = re.split(r"[;,\s]\s*", line)
print(res)