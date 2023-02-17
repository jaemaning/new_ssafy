def my_len(n):
    cnt = 0
    for _ in n:
        cnt += 1

    return cnt


def my_max(n):
    rlt = n[0]
    for i in range(1, len(n)):
        if n[i] > rlt:
            rlt = n[i]

    return rlt


def my_min(n):
    rlt = n[0]
    for i in range(1, len(n)):
        if n[i] < rlt:
            rlt = n[i]

    return rlt


def my_sum(n):
    rlt = 0
    for i in range(len(n)):
        rlt += n[i]

    return rlt


def my_index(arr, n):
    """
    :param arr: array
    :param n: target number
    :return: target index
    """
    for i in range(len(arr)):
        if arr[i] == n:
            return i


def reverse_index(arr, n):
    """
    :param arr: array
    :param n: target number
    :return: target index
    """
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == n:
            return i


a = [1, 2, 3, 4, 5]
b = "1235"
print(my_len(b))
print(my_max(a))
print(my_min(a))
print(my_sum(a))
