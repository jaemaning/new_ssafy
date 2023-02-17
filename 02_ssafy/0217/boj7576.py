from collections import deque

def bfs(arr):
    # sx, sy : 토마토의 초기 위치, arr : 토마토 초기위치 들
    que = deque()
    for sx, sy in arr:
        que.append((sx,sy))
    # 상 하 좌 우
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    max_v = 0

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and box[nx][ny] == 0:
                que.append((nx, ny))
                box[nx][ny] = box[x][y] + 1

    # que 를 다 돌았다면 마지막 day 가 답인데,
    # 그 전에 다 익을 수 있는 환경이었는지 검토
    for i in range(m):
        if 0 in box[i]:
            return -1
        else:
            if max(box[i]) > max_v:
                max_v = max(box[i])

    return max_v-1



n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(m)]
start = []

for r in range(m):
    for c in range(n):
        if box[r][c] == 1:
            start.append((r,c))

if start:
    result = bfs(start)
    print(result)
else:
    print(-1)