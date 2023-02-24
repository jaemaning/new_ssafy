# 믈놀이를 가자
import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def bfs(q):
    '''
    :param sx: 시작 x 위치
    :param sy: 시작 y 위치
    :return: 최소 이동 횟수
    '''
    day = 1

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 다음 위치가 범위안에 있고 방문한적이 없다면
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                    visited[nx][ny] = day
                    q.append((nx, ny))

        day += 1


T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    q = deque()
    # 상하좌우
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    visited = [[0] * m for _ in range(n)]


    for i in range(n):
        tmp = input()
        for j in range(len(tmp)):
            if tmp[j] == "W":
                q.append((i, j))
                visited[i][j] = "W"

    bfs(q)
    ans = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 'W':
                ans += visited[i][j]

    print(f"#{tc} {ans}")
