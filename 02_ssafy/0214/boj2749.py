# boj 2749 - 피보나치 수 3
from collections import deque

cache = deque()
cache.append(0)
cache.append(1)

n = int(input())

for _ in range(n - 1):
    cache.append(sum(cache) % 1000000)
    cache.popleft()

print(cache[-1])
