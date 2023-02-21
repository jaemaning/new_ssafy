'''
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
def bfs(G,V,s):
    '''
    G = 그래프
    V = 정점 개수
    s = 시작 정점
    '''

    visited = [False] * (V+1)
    q = []
    q.append(s)
    visited[s] = True
    
    while q:
        now = q.pop(0)
        print(now)
        for i in G[now]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)


V, E = map(int,input().split())

G = [[] for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())

    G[start].append(end)
    G[end].append(start)

bfs(G,V,1)