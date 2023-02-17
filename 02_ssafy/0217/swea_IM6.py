# 우주선착륙2
import sys

sys.stdin = open("input.txt", 'r')

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    # 8방향
    dx = (-1, -1, -1, 0, 0, 1, 1, 1)
    dy = (-1, 0, 1, -1, 1, -1, 0, 1)


    for x in range(n):
        for y in range(m):
            now = box[x][y]
            cnt = 0

            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < n and 0 <= ny < m and box[nx][ny] < now:
                    cnt += 1

            if cnt >= 4:
                result += 1

    print(f"#{tc} {result}")
