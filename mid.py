
# #option A
# def COMPARE(A, mid):
#     if A[mid] >= 0 and ((mid > 0 and A[mid - 1] < 0) or (mid == 0)):
#         return 0
#     elif A[mid] >= 0:
#         return 1
#     else:
#         return -1

# #option B
# def COMPARE(A, mid):
#     if A[mid] >= 0 and ((mid < hi-1 and A[mid + 1] < 0) or (mid == hi-1)):
#         return 0
#     elif A[mid] >= 0:
#         return -1
#     else:
#         return 1
# #
# #option C
# def COMPARE(A, mid):
#     if A[mid] >= 0 and ((mid > 0 and A[mid - 1] < 0) or (mid == 0)):
#         return 0
#     elif A[mid] >= 0:
#         return 1
#     else:
#         return -1
#
# #option D
# def COMPARE(A, mid):
#     if A[mid] < 0 and ((mid > 0 and A[mid - 1] >= 0) or (mid == hi-1)):
#         return 0
#     elif A[mid] >= 0:
#         return -1
#     else:
#         return 1

# # A:
# def COMPARE(A, mid):
#   return (A[mid] - key)

# B:
# def COMPARE(A,mid):
#   return (key - A[mid])
# C:
# def COMPARE(A,mid):
#   return (A[mid] - mid)
# D:

import math

def COMPARE(A,mid):
  return mid - A[mid]



def DCSearch(A, lo, hi):
    if lo < hi:
        print(lo, hi)
        return -1
    else:
        mid = math.floor((lo + hi) / 2)
        r = COMPARE(A, mid)
    if r == 0:
        print('me', mid)
        return mid
    elif r > 0:
        return DCSearch(A, lo, mid-1)
    else:
        return DCSearch(A, mid + 1, hi)


A = [-5, -4, -2, -1, 1, 5, 8, 8]
lo = A[0]
hi = A[-1]
print(hi)
print(DCSearch(A, lo, hi))
