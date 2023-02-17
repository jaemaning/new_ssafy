# boj 11866 요세푸스 문제 0
from collections import deque

n, k = map(int, input().split())

que = deque()
result = []

for i in range(1, n+1):
    que.append(i)

while que:
    for _ in range(k-1):
        temp = que.popleft()
        que.append(temp)
    result.append(que.popleft())

print("<",end="")
print(", ".join(map(str,result)),end="")
print(">")