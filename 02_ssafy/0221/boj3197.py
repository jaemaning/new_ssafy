# boj 3197 - 백조의 호수
from collections import deque

def bird_bfs(sx, sy):

    que = deque()
    que.append((sx, sy))

    # 백조 만나지는지 아래 ice_bfs 함수에서 day 마다 검사할 예정
    while que:
        pass





def ice_bfs(lake):
    # 초기값
    q = deque()

    for i in range(R):
        for j in range(C):
            if lake[i][j] == ".":
                q.append((i, j))

    day = 0

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == "X":
                    lake[nx][ny] = '.'
                    q.append((nx,ny))

        day += 1



R, C = map(int, input().split())

lake = [list(input()) for _ in range(R)]

# 상하좌우
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 백조의 초기위치찾기

for i in range(R):
    for j in range(C):
        if lake[i][j] == "L":
            sx, sy = i, j
            lake[i][j] = "S"
            break
    else:
        continue
    break
