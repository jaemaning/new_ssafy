def bfs(G, v, N):
    visited = [0] * (N+1)
    q = [v]
    visited[v] = 1

    while q:
        t = q.pop(0)
        # print(t, end=' ')
        for i in G[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1
    return visited
    # print(visited)


t = int(input())
for tc in range(1, t+1):
    # 정점/노드 개수
    V, E = map(int, input().split())

    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        n1, n2 = map(int, input().split())
        G[n1].append(n2)
        G[n2].append(n1)

    # 출발 노드/도착 노드
    sn, gn = map(int, input().split())

    visit = bfs(G, sn, V)
    ans = visit[gn] - 1 if visit[gn] else 0
    print(f'#{tc} {ans}')