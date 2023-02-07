def Merge(B, C, A):
    p = len(B)
    q = len(C)
    i = j = k = 0
    while i < p and j < q:
        if B[i] <= C[j]:
            A[k] = B[i]
            i = i + 1
        else:
            A[k] = C[j]
            j = j + 1
        k = k + 1
    if i == p:
        A[k: p + q] = C[j: q]
    else:
        A[k: p + q] = B[i: p]


def Mergesort(A):
    if len(A) > 1:
        n = len(A)
        B = A[:n // 2]
        C = A[n // 2:]
        Mergesort(B)
        Mergesort(C)
        Merge(B, C, A)


def SPANMOST(A):
    n = len(A)
    Mergesort(A)
    # print('here', A)
    i = 0
    maxfreq = 0
    while i < n:
        runlength = 1
        while i + runlength < n and A[i + runlength] == A[i]:
            runlength = runlength + 1
        if runlength > maxfreq:
            maxfreq = runlength
            mode = A[i]
        i = i + runlength
    return mode


L = [[1, 2, 3], [1, 2], [1, 2, 3, 5, 6, 8], [1, 8, 6, 10, 21], [1, 4, 6, 9], [7], [11]]
A = []

for sublist in L:
    for item in sublist:
        A.append(item)
print(A)
print(SPANMOST(A))