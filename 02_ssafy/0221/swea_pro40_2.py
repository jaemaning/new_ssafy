# 미로의 거리
import sys

sys.stdin = open('input.txt', 'r')

from collections import deque
def bfs(sx, sy):
    # visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((sx, sy))
    # visited[sx][sy] = True
    # 상하 좌우
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    day = 0

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and miro[nx][ny] == "3":
                    return day
                if 0 <= nx < n and 0 <= ny < n and miro[nx][ny] == "0":
                    # visited[nx][ny] = True
                    miro[nx][ny] = "1"
                    q.append((nx,ny))

        day += 1

    return 0


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    miro = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if miro[i][j] == "2":
                sx, sy = i, j

    ans = bfs(sx, sy)
    print(f"#{tc} {ans}")
