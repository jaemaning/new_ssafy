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


def my_index(arr, n):
    """
    :param arr: array
    :param n: target number
    :return: target index
    """
    for i in range(len(arr)):
        if arr[i] == n:
            return i


for tc in range(1, 11):
    number = int(input())
    dump_list = list(map(int, input().split()))

    for _ in range(number):
        max_idx = my_index(dump_list, my_max(dump_list))
        min_idx = my_index(dump_list, my_min(dump_list))

        dump_list[max_idx] -= 1
        dump_list[min_idx] += 1

    print(f"#{tc} {my_max(dump_list) - my_min(dump_list)}")
