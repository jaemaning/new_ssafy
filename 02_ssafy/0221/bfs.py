def bfs(G, v, n):
    '''
    G = graph 정보
    v = 시작 정점 번호
    n = 정점의 개수
    '''
    # 방문 배열
    visited = [False] * (n+1)
    q = []
    q.append(v)
    visited[v] = True

    while q:
        t = q.pop(0) # 큐에서 하나 꺼내옴
        print(node[t])

        for i in G[t]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)

node = ['x', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']


'''
9 9
1 2
1 3
1 4
2 3
2 5
2 6
4 7
4 8
4 9
'''


V, E = map(int, input().split())

G = [[] for _ in range(V+1)]

for i in range(E):
    start, end = map(int, input().split())
    G[start].append(end)
    G[end].append(start)

bfs(G,1,9)