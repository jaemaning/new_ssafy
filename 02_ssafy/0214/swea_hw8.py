import sys
sys.stdin = open('input.txt', 'r')

from collections import deque


def bfs(start, end):
    global result

    que = deque()
    que.append(start)
    while que:
        now = que.popleft()

        if now == end:
            result = 1
            break

        for i in graphs[now]:
            que.append(i)


for _ in range(10):
    tc, road_number = map(int, input().split())
    road_list = list(map(int, input().split()))
    graphs = [[] for _ in range(100)]
    result = 0
    x = 0
    for i in range(road_number*2):
        if not i % 2:
            x = road_list[i]
        else:
            graphs[x].append(road_list[i])

    bfs(0, 99)
    print(f"#{tc} {result}")
