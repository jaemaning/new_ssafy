# 구간합

T = int(input())
for tc in range(1, T + 1):

    n, m = map(int, input().split())
    n_lst = list(map(int, input().split()))

    # 적당히 큰 값, 작은 값을 매칭
    # 다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )
    min_v = 1000 ** 10
    max_v = -9999

    for i in range(n - m + 1):
        # m개씩 묶은 리스트와 합의 값을 저장할 곳
        result = n_lst[i:i + m]
        ans = 0

        # m개씩 묶은 값의 합 구하기.
        for num in result:
            ans += num

        # 최대값 최소값 구하기.
        if ans < min_v:
            min_v = ans

        if ans > max_v:
            max_v = ans

    print(f"#{tc} {max_v - min_v}")
