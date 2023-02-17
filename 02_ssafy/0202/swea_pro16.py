import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    cnt = 0
    max_cnt = -1

    box = [list(map(int, input().split())) for _ in range(n)]

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    cnt += box[nx][ny]

            cnt += box[i][j]
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 0

    print(f"#{tc} {max_cnt}")
