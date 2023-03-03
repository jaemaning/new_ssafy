# 파핑파핑 지뢰찾기
import sys

sys.stdin = open('input.txt', 'r')

'''
2
3
..*
..*
**.
5
..*..
..*..
.*..*
.*...
.*...

'''

from collections import deque

def bfs(sx, sy):
    q = deque()
    q.append((sx,sy))
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()
        tmp = deque()
        flag = 1

        # for _ in range(n):
        #     print(visited[_])
        # print(cnt)
        # print('---------------')

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 지뢰 발견하면 flag 컨트롤
                if b_map[nx][ny] == "*":
                    flag = 0
                else:
                    tmp.append((nx,ny))

        # 지뢰를 발견하지 않았다면? 이동
        if flag:
            while tmp:
                mx, my = tmp.popleft()
                visited[mx][my] = 1
                q.append((mx,my))


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    b_map = [list(input().strip()) for _ in range(n)]
    cnt = 0

    # 8방향 탐색
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1 or b_map[i][j] == "*":
                continue
            else:
                check_list = []
                for k in range(8):
                    nnx = i + dx[k]
                    nny = j + dy[k]

                    if 0 <= nnx < n and 0 <= nny <n:
                        check_list.append(b_map[nnx][nny])

                if not "*" in check_list:
                    cnt += 1
                    bfs(i,j)

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                cnt += 1
            if b_map[i][j] == "*":
                cnt -= 1

    print(f"#{tc} {cnt}")
