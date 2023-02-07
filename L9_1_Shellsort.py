import math


# the initial gap for an array of length n should not be larger than ceil(n/3)
# each time through the loop we at least multiple g by 3
# the loop will certainly terminate when g = n
# hence it will run for O(log3(n)) iterations
def GetInitialGap(n):
    g = 4
    prev = 1
    while g <= math.ceil(n / 3.0):
        prev = g
        g = (g * 3) + 1
    return prev


def ShellSort(A):  # A is an array
    g = GetInitialGap(len(A))
    while g >= 1:
        # sort with gap g
        b = 0
        # snapshot()
        while b < g:
            i = b + g
            # snapshot()
            while i < len(A):  # i indexes A
                # snapshot()
                v = A[i]
                j = i - g;
                # snapshot()
                while j >= b and v < A[j]:  # j indexes A
                    # snapshot()
                    A[j + g] = A[j]
                    j = j - g
                # snapshot()
                A[j + g] = v
                i = i + g
            # snapshot()
            b = b + 1
        # snapshot()
        # previous gap in the sequence [1,4,13,40,121,...]
        g = int((g - 1) / 3)  # ensure the result is an integer, not a float


A = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# clear_frames()
print(ShellSort(A))
# show_animation(size=[12, 8])