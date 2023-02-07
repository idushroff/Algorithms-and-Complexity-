def LomutoPartition(A, lo, hi):
    # A is an array, lo indexes A, hi indexes A
    p = A[lo]
    s = lo # s indexes A
    # snapshot()
    # i indexes A
    for i in range(lo + 1, hi + 1):
        # snapshot()
        if A[i] < p:
            s = s + 1
            # snapshot()
            A[s], A[i] = A[i], A[s]
            # snapshot()
    A[s], A[lo] = A[lo], A[s]
    # snapshot()
    return s

# clear_frames()

array = [3, 1, 4, 5, 9, 2, 6, 8]
lo = 0
hi = len(array) - 1

LomutoPartition(array, lo, hi)

# show_animation(size=[8,6])

def QuickSelect(A, lo, hi, k):
    # A is an array, lo indexes A, hi indexes A
    # snapshot(printstack=True)
    # s indexes A
    s = LomutoPartition(A, lo, hi)
    if s - lo == k - 1:
        # snapshot(printstack=True)
        return A[s]
    else:
        if s - lo > k - 1:
            # snapshot(printstack=True)
            return QuickSelect(A, lo, s - 1, k)
        else:
            # snapshot(printstack=True)
            return QuickSelect(A, s + 1, hi, (k - 1) - (s - lo))

# clear_frames()
array = [3, 1, 4, 5, 9, 2, 6, 8]
print(QuickSelect(array, 0, len(array) - 1, 7))
# show_animation(size=[12,7])