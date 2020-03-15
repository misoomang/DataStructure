#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
用collection.OrderDict实现(有序字典,根据k, v的赋值顺序对应先后顺序)
"""

import collections


class Lru:
    def __init__(self, size=5):
        self.size = size
        self.cached = collections.OrderedDict()

    def get(self, key):
        if key in self.cached:
            value = self.cached.pop(key, None)
            self.cached[key] = value
            return self.cached.get(key, None)
        else:
            return None

    def set(self, key, value):
        if key in self.cached:
            self.cached.pop(key, None)
        elif len(self.cached) == self.size:
            self.cached.popitem(last=False)         # 删除最末尾元素，因为最少使用
        self.cached[key] = value


if __name__ == '__main__':
    lru_test = Lru()
    lru_test.set('a', 1)
    lru_test.set('b', 1)
    lru_test.set('c', 1)
    lru_test.set('d', 1)
    lru_test.set('e', 1)
    lru_test.set('f', 1)
    print(lru_test.cached)
    for k, v in lru_test.cached.items():
        print(k, v)
