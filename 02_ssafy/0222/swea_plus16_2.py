# 정사각형 방
import sys
sys.stdin = open('input.txt', 'r')


def dfs(sx, sy):
    # global cnt
    cnt = 1
    x, y = sx, sy

    while True:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and room[nx][ny] == room[x][y] + 1:
                cnt += 1
                x, y = nx, ny
                break
        else:
            return cnt


from collections import deque


def bfs(sx,sy):
    global cnt

    q = deque()
    q.append((sx,sy))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and room[nx][ny] == room[x][y] + 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx,ny))
                break

        cnt += 1


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    room = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 1

    # 상하좌우
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    start=[]

    for i in range(n):
        for j in range(n):
            cnt = dfs(i, j)
            if max_cnt <= cnt:
                max_cnt = cnt
                start.append((room[i][j],cnt))


    start.sort()
    for i in range(len(start)):
        if start[i][1] == max_cnt:
            ans = start[i][0]
            break

    print(f"#{tc} {ans} {max_cnt}")

    # start.sort()
    #
    # # 마지막 처음 들어온 값들 검증.
    # for i in range(len(start)):
    #     visited = [[False] * n for _ in range(n)]
    #     re_x, re_y = start[i][1]
    #     cnt = 0
    #     bfs(re_x, re_y)
    #     if cnt == max_cnt:
    #         print(f"#{tc} {start[i][0]} {max_cnt}")
    #         break

