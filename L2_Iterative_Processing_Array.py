# We wrote this version in the live lecture. Below is a version that matches the one from the slides.

A = [3,7,4,2,8]   # len(A) = 5
#    0 1 2 3 4


def find1(A,x):
    # A is an array
    # j indexes A
    for j in range(0,len(A)):
        # snapshot()
        if A[j] == x:
            return j
    return -1


# clear_frames()
print(find1(A,2))
# show_animation(size=[8,5])


# The find function finds the value in the Array and returns corresponding index,
# returns -1 if not found


def find(A,x,n):
    # A is an array
    j = 0 # j indexes A
    while j < n:
        # snapshot()
        if A[j] == x:
            return j
        j = (j + 1)
    return -1


A = [6,9,2,3,7,5,8]
x = 7 # value to find
n = 7 # size of Array
# clear_frames()
print(find(A,x,n))
# show_animation(size=[8,4])