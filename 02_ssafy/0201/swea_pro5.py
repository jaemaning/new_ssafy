# swea 1일차 숫자카드
def my_max(n):
    rlt = n[0]
    for i in range(1, len(n)):
        if n[i] > rlt:
            rlt = n[i]

    return rlt


def reverse_index(arr, n):
    """
    :param arr: array
    :param n: target number
    :return: target index
    """
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == n:
            return i


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    cards = input()
    counting_list = [0] * 10

    for card in cards:
        counting_list[int(card)] += 1

    max_v = my_max(counting_list)
    value = reverse_index(counting_list, max_v)

    print(f"#{tc} {value} {max_v}")
