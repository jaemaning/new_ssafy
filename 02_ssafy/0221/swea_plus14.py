# contact

import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def last_index(target, visited):
    for i in range(len(visited)-1,-1,-1):
        if visited[i] == target:
            return i


def bfs(s, visited):

    q = deque()
    q.append(s)
    visited[s] = 99999
    day = 0

    while q:
        day += 1
        for _ in range(len(q)):
            n = q.popleft()

            for i in graph[n]:
                if not visited[i]:
                    visited[i] = day
                    q.append(i)

    return day


for tc in range(1, 11):
    n, s = map(int, input().split())
    n_list = list(map(int, input().split()))
    graph = [set() for _ in range(101)]
    visited = [0] * 101

    for i in range(n // 2):
        start, end = n_list[i * 2], n_list[i * 2 + 1]
        graph[start].add(end)

    day = bfs(s, visited)
    ans = last_index(day-1, visited)

    print(f"#{tc} {ans}")
