# Shell sort in python


def shellSort(array, n):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    # interval = n // 2
    interval = 3
    # interval = n // 3
    # interval = n // 4
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        print(temp)
        interval //= 3


data = [16, 4, 17, 13, 9, 6, 8, 5, 10, 11, 7, 3]
size = len(data)
shellSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
