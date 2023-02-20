# 피자굽기
# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    ci = list(map(int, input().split())) + [21] * 200
    m_cnt = [0 for _ in range(m)]
    front, rear = 0, n-1
    result = 0
    qq = []

    while rear < n+m:
        if ci[front] == 21:
            front = (front + 1) % n
            continue

        ci[front] //= 2
        if ci[front] == 0:
            rear += 1
            m_cnt[front] += 1
            ci[front], ci[rear] = ci[rear], ci[front]
            qq.append([front,rear])

        front = (front + 1) % n
        print(ci)

    ans = ci.index(result)

    print(ans)

