# 벽 부수고 이동하기
from collections import deque


def bfs(sx, sy, cnt):
    q = deque()
    q.append((sx, sy, cnt))
    day = 0

    while q:
        day += 1
        for _ in range(len(q)):
            x, y, cnt = q.popleft()

            if x == n - 1 and y == m - 1:
                return day

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if b_map[nx][ny] and cnt:
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt - 1))

                    elif not b_map[nx][ny]:
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt))

    return -1


n, m = map(int, input().split())

b_map = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 상하좌우
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

ans = 0
result = []
flag = 0
visited[0][0] = 1

day = bfs(0, 0, 1)

print(day)
