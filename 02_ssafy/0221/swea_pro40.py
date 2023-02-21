# 노드의 거리
import sys

sys.stdin = open('input.txt', 'r')
from collections import deque


def bfs(start):
    visited = [False] * (V + 1)
    q = deque()
    q.append(start)
    day = 0

    while q:

        for _ in range(len(q)):

            n = q.popleft()

            if n == G:
                return day

            for i in graph[n]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True

        day += 1

    return 0

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        start, end = map(int, input().split())

        graph[start].append(end)
        graph[end].append(start)

    S, G = map(int, input().split())

    ans = bfs(S)
    print(f"#{tc} {ans}")
