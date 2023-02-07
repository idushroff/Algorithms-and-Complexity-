def linear_search(list, target):
    """This function returns the index position of the target if
    found otherwise None."""

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def search(A, x, lo, hi):
    if lo > hi:
        return -1
    else:
        m1 = int(lo + ((hi-lo)/3)) # 3 for array B
        if A[m1] == x:
            return m1
        else:
            if A[m1] > x:
                return search(A, x, lo, m1-1)
            else:
                m2 = int(lo + 2*(hi-lo)/3)
                if A[m2] == x:
                    return m2
                else:
                    if A[m2] < x:
                        return search(A, x, m2+1, hi)
                    else:
                        return search(A, x, m1+1, m2-1)

# B = [0, 2, 2, 3, 5, 6, 8, 9, 9]
# print(search(B, 5, 0, 9))

# 844096
C = [0, 4, 4, 6, 8, 9]
print(search(C, 5, 0, 9))