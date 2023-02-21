# 미로 1
import sys
sys.stdin = open('input.txt' ,'r')

def dfs(x, y):
    global flag
    # 상하좌우
    dx = (-1,1,0,0)
    dy = (0,0,-1,1)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and miro[nx][ny] == 3:
            flag = 1
            return 1

        elif 0 <= nx < n and 0 <= ny < n and miro[nx][ny] == 0:
            miro[nx][ny] = 1
            dfs(nx, ny)

    if flag == 1:
        return 1

    return 0


for _ in range(10):
    tc = int(input())
    n = 16
    miro = [list(map(int, list(input()))) for _ in range(n)]
    flag = 0

    for i in range(n):
        for j in range(n):
            if miro[i][j] == 2:
                sx, sy = i, j
                break
        else:
            continue
        break

    ans = dfs(sx, sy)
    print(f"#{tc} {ans}")
