def LomutoPartition(A, lo, hi):
    # A is an array, lo indexes A, hi indexes A
    p = A[lo]
    s = lo # s indexes A
    snapshot()
    # i indexes A
    for i in range(lo + 1, hi + 1):
        snapshot()
        if A[i] < p:
            s = s + 1
            snapshot()
            A[s], A[i] = A[i], A[s]
            snapshot()
    A[s], A[lo] = A[lo], A[s]
    snapshot()
    return s

clear_frames()

array = [3, 1, 4, 5, 9, 2, 6, 8]
lo = 0
hi = len(array) - 1

LomutoPartition(array, lo, hi)

# show_animation(size=[8,6])