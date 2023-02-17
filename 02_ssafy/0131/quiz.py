# 퀴즈
# 행 5 * 열 6 값을 임의로 할당(random)
# 2차원 배열의 모든 원소를 순회하면서 짝수인 원소의 개수를 세는 프로그램

import random
from pprint import pprint

n = 5  # 행
m = 6  # 열
cnt = 0

# 상하좌우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

graph = [[random.randrange(1, 10) for _ in range(m)] for _ in range(n)]
#
# for x in range(n):
#     for y in range(m):
#         # for k in range(4):
#         #     nx = x + dx[k]
#         #     ny = y + dy[k]
#         if 0 <= nx < n and 0 <= ny < m:
#             if not graph[nx][ny] % 2:
#                 cnt += 1
#
pprint(graph)
# print(cnt)

for x in range(n):
    for y in range(m):
        if not graph[x][y] % 2:
            cnt += 1

print(cnt)
cnt = 0

for y in range(m):
    for x in range(n):
        if not graph[x][y] % 2:
            cnt += 1

print(cnt)