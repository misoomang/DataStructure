# -*- coding: UTF-8 -*-


def gen_pnext(substring):
    """
    构造临时数组pnext
    """
    print(substring)
    index, m = 0, len(substring)
    pnext = [0]*m
    i = 1
    while i < m:
        if (substring[i] == substring[index]):
            pnext[i] = index + 1
            index += 1
            i += 1
        elif (index!=0):
            index = pnext[index-1]
        else:
            pnext[i] = 0
            i += 1
    return pnext

str = 'ababaaaba'

print(gen_pnext(list(str)))