def max_element(A,n):
    # A is an array
    # i indexes A
    max = A[0]
    # snapshot()
    for i in range(1,len(A)):
        # snapshot()
        if A[i] > max:
            max = A[i]
        # snapshot()
    return max

# clear_frames()
A = [23,12,42,6,70,18,3]
n = 7 # size of Array
print(max_element(A,n))
# show_animation(size=[10,4])