import sys
from collections import deque
input = sys.stdin.readline

def dfs(v):

    if check_list[v] == False:
        check_list[v] = True
        dfs_list.append(v)
        for i in graphs[v]:
            dfs(i)


n, m, v = map(int, input().split())
graphs = [[] for _ in range(n+1)]
check_list = [False] * (n+1)
dfs_list = []
bfs_list = []
que = deque()

for _ in range(m):
    start, end = map(int, input().split())
    graphs[start].append(end)
    graphs[end].append(start)

for sor in graphs:
    sor.sort()

que.append(v)
check_list[v] = True
bfs_list.append(v)

while que:
    next = que.popleft()
    for i in graphs[next]:
        if check_list[i] == False:
            que.append(i)
            bfs_list.append(i)
            check_list[i] = True


check_list = [False] * (n+1)
dfs(v)

print(" ".join(map(str,dfs_list)))
print(" ".join(map(str,bfs_list)))
