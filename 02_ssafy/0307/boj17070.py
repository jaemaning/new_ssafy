def dfs(x, y, end, d):
    global ans

    if x == end[0] and y == end[1]:
        ans += 1
        return

    # 방향이 가로라면?
    if d == 1:
        # 다음 방향은 가로 or 대각으로 갈 가능성이 있음.
        # 가로
        nx, ny = x, y+1
        if nx < n and ny < n and p_map[nx][ny] == 0:
            dfs(nx, ny, end, 1)
        # 대각
        nx, ny = x+1, y+1
        if nx < n and ny < n and p_map[nx][ny] == 0 and p_map[nx-1][ny] == 0 and p_map[nx][ny-1] == 0:
            dfs(nx, ny, end, 3)

    # 방향이 세로라면?
    elif d == 2:
        # 다음 방향은 세로 or 대각으로 갈 가능성이 있음.
        # 세로
        nx, ny = x+1, y
        if nx < n and ny < n and p_map[nx][ny] == 0:
            dfs(nx, ny, end, 2)
        # 대각
        nx, ny = x+1, y+1
        if nx < n and ny < n and p_map[nx][ny] == 0 and p_map[nx-1][ny] == 0 and p_map[nx][ny-1] == 0:
            dfs(nx, ny, end, 3)
        

    # 방향이 대각선이라면?
    else:
        # 다음 방향은 가로 or 세로 or 대각으로 갈 가능성이 있음.
        # 가로
        nx, ny = x, y+1
        if nx < n and ny < n and p_map[nx][ny] == 0:
            dfs(nx, ny, end, 1)
        # 세로
        nx, ny = x+1, y
        if nx < n and ny < n and p_map[nx][ny] == 0:
            dfs(nx, ny, end, 2)
        nx, ny = x+1, y+1
        if nx < n and ny < n and p_map[nx][ny] == 0 and p_map[nx-1][ny] == 0 and p_map[nx][ny-1] == 0:
            dfs(nx, ny, end, 3)



n = int(input())

p_map = [list(map(int, input().split())) for _ in range(n)]

# 시작 방향은 가로
# 왼쪽으로는 못감
d = 1

start = (0, 1)
end = (n-1, n-1)
ans = 0

dfs(0,1,end,1)
print(ans)