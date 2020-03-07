# -*- coding: UTF-8 -*-


def binary_search(search_list: list, search_num):
    """
    插值查找
    :param search_list: 已排好序的数组(默认从小到大)
    :param search_num:  查询的数字
    :return:  该数字在数组中的位置
    """
    low = 0
    high = len(search_list) - 1
    while low <= high:
        mid = int(low + (high - low) * (search_num - search_list[low]) / (search_list[high] - search_list[low]))
        if search_num < search_list[mid]:
            high = mid
        elif search_num > search_list[mid]:
            low = mid
        else:
            return mid
    return 0


if __name__ == '__main__':
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = 8
    print(binary_search(a_list, num) + 1)
