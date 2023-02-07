import math

# The binsearch function finds the key in the Array and returns corresponding index,
# returns -1 if not found


def binsearch(A, lo, hi, key):
    # A is an array
    # lo indexes A
    # hi indexes A
    # mid indexes A
    if lo > hi:
        return -1
    mid = lo + math.floor((hi-lo)/2)
    # snapshot()
    if A[mid] == key:
        return mid
    else:
        if A[mid] > key:
            return binsearch(A, lo, mid-1, key)
        else:
            return binsearch(A, mid+1, hi, key)


A = [4, 9, 13, 22, 41, 83, 96]
# clear_frames()
index = binsearch(A, 0, 6, 42)
#print('index:', index)
print(index)
# show_animation(size=[8,6])