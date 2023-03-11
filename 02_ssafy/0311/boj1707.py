# 이분 그래프
import sys
input = sys.stdin.readline


def dfs(s, cnt):
    global flag

    if check_list[s] == 4:
        check_list[s] = cnt % 2
        print(cnt)
    else:
        print('야호')
        if check_list[s] != cnt % 2:
            flag = 1

    for next in graph[s]:
        if not visited[next]:
            visited[next] = 1
            dfs(next, cnt+1)


T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    check_list = [4] * (v+1)
    flag = 0

    for _ in range(e):
        start, end = map(int, input().split())

        graph[start].append(end)
        graph[end].append(start)

    # print(visited)
    print(graph)
    visited[1] = 1
    dfs(1, 0)

    print(check_list)

    if flag:
        print("NO")
    else:
        print("YES")
