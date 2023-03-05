# 뱀과 사다리 게임
import sys
from collections import deque
input = sys.stdin.readline


def check_dfs(n_idx):

    if len(adj_list[n_idx]) == 1:
        return check_dfs(adj_list[n_idx][0])
    else:
        return n_idx


def bfs(start):

    q = deque(adj_list[start])
    cnt = 0

    while True:
        cnt += 1

        for _ in range(len(q)):
            n_idx = q.popleft()
            if n_idx == 100:
                return cnt

            next = check_dfs(n_idx)

            for i in adj_list[next]:
                q.append(i)


# 사다리의수(n) 뱀의 수(m)
n, m = map(int, input().split())
# 101 칸 만들어두기 => 1부터 시작
adj_list = [[] for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    adj_list[x].append(y)

for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)

for i in range(1, len(adj_list)):
    if not adj_list[i]:
        for j in range(1+i, 7+i):
            adj_list[i].append(j)

ans = bfs(1)
print(ans)
