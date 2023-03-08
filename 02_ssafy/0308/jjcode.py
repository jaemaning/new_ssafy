def bfs(si, sj):
    global flag

    q = []
    q.append((si, sj))

    while q:
        ci, cj = q.pop(0)

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj

            if arr[ni][nj] == '3':
                flag += 1
                return

            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != '1':
                q.append((ni, nj))
                arr[ni][nj] = '1'

    return


t = 10
for tc in range(1, t + 1):
    _ = input()
    flag = 0
    n = 16
    arr = [list(input()) for _ in range(n)]
    # print(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                si, sj = i, j

    bfs(si, sj)
    print(f'#{tc} {flag}')
