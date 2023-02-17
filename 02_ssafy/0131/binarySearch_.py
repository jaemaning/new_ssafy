def binarySearch(arr, n, key):
    start = 0
    end = n - 1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == key:
            return middle
        elif arr[middle] < key:
            start = middle + 1
        else:
            end = middle - 1

    return False


a = [0, 5, 8, 9, 10, 13, 15]
print(a)
print(binarySearch(a, len(a), 15))
