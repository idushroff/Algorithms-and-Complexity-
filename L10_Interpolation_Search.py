"""Interpolation search is an algorithm
for searching for a key in an array that
has been ordered by numerical values assigned
to the keys (key values).

The Interpolation Search is an improvement over Binary
Search for instances, where the values in a sorted
array are uniformly distributed."""


def InterpolationSearch(A, k):
    # A is an array
    # lo indexes A
    # hi indexes A
    lo = 0
    hi = len(A) - 1
    while lo < hi:
        # snapshot()
        if A[lo] > k or A[hi] < k:
            break
        if lo == hi:
            if A[lo] == k:
                # snapshot()
                return lo
            else:
                break
        m = lo + (k - A[lo]) * (hi - lo) // (A[hi] - A[lo]) # m indexes A
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
for i in range(15):
    print(InterpolationSearch([1, 2, 3, 5, 8, 13], i))
# show_animation(size=[8,10])