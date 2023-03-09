def dfs(start):

    visited[start] = 1

    next = adj_list[start]

    for i in next:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)


T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    adj_list = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    visited[0] = 1
    cnt = 1

    for _ in range(m):
        start, end = map(int, input().split())
        adj_list[start].append(end)
        adj_list[end].append(start)

    s = 1
    while True:
        dfs(s)

        if sum(visited) == n+1:
            break

        s = visited.index(0)
        cnt += 1

    print(f'#{tc} {cnt}')
