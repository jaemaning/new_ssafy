# 단지번호붙이기
from collections import deque
import sys
input = sys.stdin.readline


def bfs(sx, sy):

    q = deque()
    q.append((sx, sy))
    d_map[sx][sy] = 0
    cnt = 0

    while q:
        cnt += 1
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and d_map[nx][ny]:
                d_map[nx][ny] = 0
                q.append((nx,ny))

    result.append(cnt)
    return


n = int(input())

d_map = [list(map(int, list(input().strip()))) for _ in range(n)]

# 상하좌우
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
ans = 0
result = []

for i in range(n):
    for j in range(n):
        if d_map[i][j] == 1:
            bfs(i,j)
            ans += 1

print(ans)
result.sort()
for _ in result:
    print(_)
