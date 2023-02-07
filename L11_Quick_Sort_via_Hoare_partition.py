"""Hoare partition is an algorithm that is used to
 partition an array about a pivot. All elements
 smaller than the pivot are on it's left (in any order)
 and all elements greater than the pivot are on it's
 right (in any order). Quicksort algorithm uses hoare
 paritition to partition the array."""


def HoarePartition(A, lo, hi):
    # A is an array
    p = A[lo]
    i = lo
    j = hi
    # i indexes A
    # j indexes A
    while i < j:
        # snapshot()
        while i < hi and A[i] <= p:
            i = i + 1
            # snapshot()
        while j >= lo and A[j] > p:
            j = j - 1
            # snapshot()
        A[i], A[j] = A[j], A[i]
        # snapshot()
    A[i], A[j] = A[j], A[i]
    # snapshot()
    A[lo], A[j] = A[j], A[lo]
    # snapshot()
    print(A) """this will print each round of the hoare partition round!!! YAYY!!!!"""
    return j


# clear_frames()
# array = [6, 3, 1, 7, 9, 5, 8, 2, 4, 0]
# print("HP", HoarePartition(array, 0, len(array) - 1))
# show_animation(size=[8,7])


# Note we could also use LomutoPartition from lecture 10 but
# using Hoare's partitioning algorithm is more traditional
def Quicksort(A, lo, hi):
    # A is an array
    # snapshot(printstack=True)
    if lo < hi:
        s = HoarePartition(A, lo, hi)
        Quicksort(A, lo, s - 1)
        Quicksort(A, s + 1, hi)


# clear_frames()

array = [6, 3, 1, 7, 9, 5, 8, 2, 4, 0]
print(Quicksort(array, 0, len(array) - 1))

# show_animation(size=[12, 9])