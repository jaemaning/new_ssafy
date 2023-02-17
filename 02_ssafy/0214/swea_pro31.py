# 4일차 - 그래프 경로
import sys
sys.stdin = open('input.txt', 'r')


def dfs(S):
    # S 에서 출발 G로 도착 가능한지
    # 가능: 1, 불가능: 0
    result.append(S)
    for i in graphs[S]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


T = int(input())

for tc in range(1, T + 1):
    v, e = map(int, input().split())
    graphs = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    result = []

    for _ in range(e):
        start, end = map(int, input().split())
        graphs[start].append(end)

    S, G = map(int, input().split())

    visited[S] = True
    dfs(S)
    if G in result:
        ans = 1
    else:
        ans = 0
    print(f"#{tc} {ans}")
