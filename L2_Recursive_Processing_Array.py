# The find function finds the value in the Array and returns corresponding index,
# returns -1 if not found
def find(A, x, lo, hi):
    # A is an array
    # lo indexes A
    # hi indexes A
    # snapshot()
    if lo > hi:
        return -1
    elif A[lo] == x:
        return lo
    else:
        return find(A, x, lo+1, hi)


A = [6, 9, 2, 3, 7, 5, 8]

x = 7   # value to find
n = 7   # size of Array
# clear_frames()
print(find(A, x, 0, n-1))
# show_animation(size=[4,5])