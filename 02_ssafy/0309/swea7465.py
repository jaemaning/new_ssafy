# 창용 마을 무리의 개수

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())

    adj_list = [[] for _ in range(n + 1)]
    visited = [0] * (n+1)
    stk = []
    cnt = 0

    for _ in range(m):
        start, end = map(int, input().split())

        adj_list[start].append(end)
        adj_list[end].append(start)

    for i in range(1, n+1):
        if visited[i] == 0:
            cnt += 1
            stk.append(i)
            while stk:
                x = stk.pop()
                if visited[x] == 0:
                    visited[x] = 1
                    for j in adj_list[x]:
                        print(visited)
                        stk.append(j)

    print(cnt)