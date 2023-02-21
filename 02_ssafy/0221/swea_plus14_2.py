# 미로 2

import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(sx, sy):
    '''
    :param sx: 시작 x 위치
    :param sy: 시작 y 위치
    :return: 성공 가능 여부
    '''

    # visited = [[False] * 100 for _ in range(100)]
    # 상하좌우
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    q = deque()
    q.append((sx, sy))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and miro[nx][ny] == 3:
                return 1
            if 0 <= nx < n and 0 <= ny < n and miro[nx][ny] == 0:
                miro[nx][ny] = 1
                q.append((nx, ny))

    return 0


for tc in range(1, 11):
    _ = int(input())
    n = 100

    miro = [list(map(int,list(input()))) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if miro[i][j] == 2:
                sx, sy = i, j

    print(f"#{tc} {bfs(sx, sy)}")
