t = int(input())
for tc in range(1, t+1):
    # n: 사람 수, m: 시간(초), k: 붕어빵 개수
    n, m, k = map(int, input().split())
    # 시간 n개
    time_lst = list(map(int, input().split()))
    time_lst.sort()
    mx_time = sum(time_lst)
    ans = 'Possible'

    if k * m * mx_time < n:
        ans = 'Impossible'

    for i in range(n):
        if time_lst[i] < m:
            ans = 'Impossible'

    # 0 처리
    if time_lst[0] == 0:
        ans = 'Impossible'

    print(f'#{tc} {ans}')