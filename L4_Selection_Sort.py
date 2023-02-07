# Function to swap between two array elements
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Sorting Array in ascending order using selection sort
def selection_sort(A):
    # A is an array
    for i in range(0, len(A)):  # i indexes A
        # snapshot()
        min = i  # min indexes A
        # snapshot()
        for j in range(i + 1, len(A)):  # j indexes A
            # snapshot()
            if A[j] < A[min]:
                min = j
                # snapshot()
        # snapshot()
        swap(A, i, min)
        # snapshot()
    return A


X = [23, 12, 42, 6, 69, 18, 3]
# clear_frames()
print(selection_sort(X))
# show_animation(size=[10, 6])