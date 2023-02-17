# 실습3 숫자를 정렬하자
# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.
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


def count_sort(a, b, k):
    """
    :param a: 정렬이 안된 리스트.
    :param b: 정렬후 리스트.
    :param k: a 리스트의 맥스값.
    :return:
    """
    c = [0] * (k + 1)

    for i in range(my_len(a)):
        c[a[i]] += 1

    for i in range(1, my_len(c)):
        c[i] += c[i - 1]

    for i in range(my_len(a) - 1, -1, -1):
        c[a[i]] -= 1
        b[c[a[i]]] = a[i]


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    sorted_list = [0] * n
    max_v = my_max(n_list)

    count_sort(n_list, sorted_list, max_v)
    print(f'#{tc} {" ".join(map(str, sorted_list))}')
