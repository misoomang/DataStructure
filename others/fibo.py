# def fibo(n):
#     a = [0, 1]
#     print(a)
#
#     if n == 0 and n == 1:
#         return a
#     else:
#         for i in range(2, n):
#             a.append(a[i-1] + a[i-2])
#         return a
#
# if __name__ == '__main__':
#     input_num = input('请输入数字')
#     print('斐波那契数列: ', fibo(int(input_num)))


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)
