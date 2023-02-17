'''
  = > n,v ( n : 노드 수, v : 간선 수)
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''

n, v = map(int, input().split())
graphs = [[] for _ in range(n + 1)]
for _ in range(v):
    start, end = map(int, input().split())
    graphs[start].append(end)
    graphs[end].append(start)

print(graphs)


# 7 8  = > n,v ( n : 노드 수, v : 간선 수)
def dfs(n, now):
    stack = []
    visited = [False] * (n + 1)
    visited[now] = True
    print(now, end=" ")

    while 1:

        for n in graphs[now]:
            if not visited[n]:
                print(n, end=" ")
                visited[n] = True
                now = n
                stack.append(now)
                break
        else:
            now = stack.pop()
            if not stack:
                break

    print()


dfs(n, 1)
