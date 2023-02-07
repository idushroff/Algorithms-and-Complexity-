def BinSearch(A, k):
    # A is an array
    lo = 0
    hi = len(A) - 1
    # lo indexes A, hi indexes A
    # snapshot()
    while lo <= hi:
        # m indexes A
        m = lo + (hi - lo) // 2
        # snapshot()
        if A[m] == k:
            # snapshot()
            return m
        if A[m] > k:
            hi = m - 1
            # snapshot()
        else:
            lo = m + 1
            # snapshot()
    return -1


# clear_frames()
BinSearch([10, 20, 30, 40, 50], 10)
# show_animation(size=[8,7])