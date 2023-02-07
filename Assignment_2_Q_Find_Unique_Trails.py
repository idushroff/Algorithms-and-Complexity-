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
    return A


def count(arr, n):
    # The count function calculates the frequency of each trail
    # This function returns the list s which has all the trails with a count of 1 (indicating their confined within one region)

    mp = dict()
    # Traverse through array elements and count frequencies
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

    # Traverse through map and print frequencies
    s = []
    for x in mp:
        if mp[x] == 1:
            s.append(x)
    return s


def fnd_idx(char, lst):
    # This function serves to find the index values of the trails with a count of 1.
    # Returning a tuple with the region and index value of the trail in the region.
    for x in range(len(lst)):
        try:
            idx = lst[x].index(char)
            return [x, idx]
        except ValueError:
            pass
    return None


def DISCONNECTED(L):
    # check if region contains unique trails only.
    unique_regions = []
    for elem in ss:
        result = fnd_idx(elem, L)
        region = result[0]
        if len(L[region]) == 1:
            unique_regions.append(region)
        else:
            # check if all other elements in this region are also unique to this region
            region_is_unique = True
            for item in L[region]:
                if item not in ss:
                    region_is_unique = False

            if region_is_unique:
                unique_regions.append(region)
    return unique_regions[0]


# Driver Code
L = [[0, 1, 2, 3], [1, 2], [1, 2, 3, 5, 6, 8], [1, 8, 6, 10, 21], [1, 4, 6], [7, 9], [11]]
A = []
# collapse the list of list L into one list
for sublist in L:
    for item in sublist:
        A.append(item)
# Pre-Sort the list A for making simplifying the process of counting trail frequency
B = Mergesort(A)
n = len(B)
# Assign the output of the frequency counter to the list ss
ss = count(B, n)  # list ss is a list of all trails with count 1
DISCONNECTED(ss)



# print('uni_regions = ans ->', unique_regions[0])