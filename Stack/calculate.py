# -*- coding: UTF-8 -*-
# 用栈来计算 5+6*(9-7)-4/2+2

# 改为后缀表达式为5 6 9 7 - * + 4 2 / - 2 +

from Stack.stack import Stack


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def stack_calculate(list_suffix):
    stack = Stack()
    if not isinstance(list_suffix, list):
        return 'list of suffix error'
    for i in list_suffix:
        if is_number(i):
            stack.stack_push(i)
        elif i in ('+', '-', '*', '/', ):
            pop_1 = stack.stack_pop()
            pop_2 = stack.stack_pop()
            if i in ('-', '/'):
                stack.stack_push(pop_2 - pop_1) if i == '-' else stack.stack_push(pop_2 / pop_1)
            else:
                stack.stack_push(pop_2 + pop_1) if i == '+' else stack.stack_push(pop_2 * pop_1)
    return stack.stack_show()


if __name__ == '__main__':
    need_list = [5, 6, 9, 7, '-', '*', '+', 4, 2, '/', '-', 2, '+']
    print(stack_calculate(need_list))
