#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
用list实现实现一个简单的LRU（最近最少使用）
"""


class Lru:
    def __init__(self, size=5):
        self.size = size
        self.cached = {}
        self.lru_list = list()          # 因为列表是有序的，最新使用则插入到列表首部

    def get(self, key):
        if key in self.cached:
            if key in self.lru_list:
                self.lru_list.remove(key)
            if len(self.lru_list) >= self.size:
                self.lru_list.pop()
            self.lru_list.insert(0, key)        # 让key位于列表首部，表示最新使用key
            return self.cached.get(key)
        else:
            return None

    def set(self, key, value):
        if key in self.cached:
            if key in self.lru_list:
                self.lru_list.remove(key)
            self.lru_list.insert(0, key)
        elif len(self.lru_list) == self.size:
            expired_key = self.lru_list.pop()
            self.cached.pop(expired_key, None)
            self.lru_list.insert(0, key)
        else:
            self.lru_list.insert(0, key)
        self.cached[key] = value


if __name__ == '__main__':
    lru_test = Lru()
    lru_test.set('a', 1)
    lru_test.set('b', 1)
    lru_test.set('c', 1)
    lru_test.set('d', 1)
    lru_test.set('e', 1)
    lru_test.set('f', 1)
    print(lru_test.lru_list)
    print(lru_test.get('a'))
