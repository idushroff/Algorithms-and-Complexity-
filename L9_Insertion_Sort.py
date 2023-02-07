def InsertionSort(A):
    # A is an array
    snapshot()
    for i in range(1, len(A)):  # i indexes A
        snapshot()
        v = A[i]
        j = i - 1  # j indexes A
        while j >= 0 and v < A[j]:
            snapshot()
            A[j + 1] = A[j]
            j = j - 1
        snapshot()
        A[j + 1] = v
        snapshot()


clear_frames()

A = [3, 1, 4, 5, 9, 2, 6, 8, 7, 0]
InsertionSort(A)

show_animation(size=[8, 5])