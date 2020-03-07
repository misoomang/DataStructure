# -*- coding: UTF-8 -*-


def binary_search(search_list: list, search_num):
    """
    折半查找
    :param search_list: 已排好序的数组(默认从小到大)
    :param search_num:  查询的数字
    :return:  该数字在数组中的位置
    """
    low = 0
    hight = len(search_list) - 1
    while low <= hight:
        mid = int((low + hight) / 2)
        if search_num < search_list[mid]:
            hight = mid
        elif search_num > search_list[mid]:
            low = mid
        else:
            return mid
    return 0


if __name__ == '__main__':
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = 5
    print(binary_search(a_list, num) + 1)
