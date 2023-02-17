# 2164 카드2
from collections import deque
n = int(input())
que = deque()

for i in range(1,n+1):
    que.append(i)


while len(que) != 1:
    que.popleft()
    shuffle_number = que.popleft()
    que.append(shuffle_number)

print(que[0])

