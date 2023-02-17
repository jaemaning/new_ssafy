import sys
sys.stdin = open('input.txt', 'r')


def dfs(x,y):
    global ans
    # 시작 : 맨 마지막줄 2, 끝 : 맨 윗줄 3
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]


        if 0 <= nx < n and 0 <= ny < n and miro[nx][ny] == 0:
            miro[x][y] += 5
            dfs(nx,ny)

        if 0 <= nx < n and 0 <= ny < n and miro[nx][ny] == 3:
            ans = 1
            return


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    miro = []
    ans = 0

    for _ in range(n):
        miro.append(list(map(int, list(input()))))

    for i in range(n):
        for j in range(n):
            if miro[i][j] == 2:
                start_x = i
                start_y = j

    # print(start_x, start_y)

    dfs(start_x, start_y)

    # 탈출할 수 있으면 1, 탈출할 수 없으면 0 을 출력한다.
    # print(miro)
    print(f"#{tc} {ans}")
