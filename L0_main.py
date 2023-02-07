# # s = 'supercalifragilisticexpialidocious'
# # for
#
# t = list('supercalifragilisticexpialidocious')
# m = 3
# p = 'lido'
# n = len(t)
# print('p1', n)
#
#
# def func1():
#     for i in range(1, n-m):
#         j = 0
#         while j < m and p[j] == t[i+j]:
#             j += 1
#         if j == m:
#             return i
#     return -1
#
#
# print(func1())
#
# sum = 0
# for i in range(1, 589):
#     sum += i
#
#
# from itertools import permutations
# l = list(permutations(range(1, 5)))
# print(l)
#
# i = 0
# for i in l:
#     print(i)
# i += 1
# for j in i:
#     sum = 0
#     if j == 1:
#         sum =


L = [[1, 2, 3], [1, 2], [1, 2, 3, 5, 6, 8], [1, 8, 6, 10, 21], [1, 4, 6, 9]]
Q = [3, 0, 1]
Q_1 = [1, 0, 3]


def func_X(L, Q):
    l = []
    for i in L[Q[0]]:
        l.append([i, 0])
    for q in Q:
        for i in L[q]:
            for tupp in l:
                if tupp[0] == i:
                    tupp[1] += 1

    s = []
    for tupp in l:
        if tupp[1] == len(Q):
            s.append(tupp[0])
    return s


print(func_X(L, Q))
print(func_X(L, Q_1))
