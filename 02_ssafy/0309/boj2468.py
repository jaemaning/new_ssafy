# 안전 영역
import sys
input = sys.stdin.readline
from collections import deque


def bfs(sx, sy):
    global cnt

    cnt += 1
    q = deque()
    q.append((sx,sy))

    while q:
        
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]:
                visited[nx][ny] = 0
                q.append((nx,ny))

    return


n = int(input())

f_map = [list(map(int, input().split())) for _ in range(n)]


# 상하좌우
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

ans = 0




for k in range(100):
    visited = [[1] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if f_map[i][j] <= k:
                visited[i][j] = 0

    for sx in range(n):
        for sy in range(n):
            if visited[sx][sy]:
                visited[sx][sy] = 0
                bfs(sx, sy)
                
    ans = max(ans, cnt)

print(ans)