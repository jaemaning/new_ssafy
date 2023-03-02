# 농작물 수확하기
import sys

sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(n):
    visited = [[False] * n for _ in range(n)]
    ans = 0
    q = deque()
    q.append((n // 2, n // 2))
    visited[n // 2][n // 2] = True
    ans += f_map[n // 2][n // 2]

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    day = 0
    while day != n // 2:
        day += 1
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    ans += f_map[nx][ny]

    return ans


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    f_map = [list(map(int, list(input()))) for _ in range(n)]

    rlt = bfs(n)
    print(f'#{tc} {rlt}')
