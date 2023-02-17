# 1일차 min max

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    n_lst = list(map(int, input().split()))
    # 적당히 크고 작은값.
    min_v = 1000001
    max_v = -9999

    for i in range(n):
        if max_v < n_lst[i]:
            max_v = n_lst[i]
        if min_v > n_lst[i]:
            min_v = n_lst[i]

    print(f"#{tc} {max_v - min_v}")
