import sys
from collections import deque
input = sys.stdin.readline

que = deque()
n = int(input().rstrip())

for _ in range(n):
    new_method = list(input().strip().split())

    if new_method[0] == "push":
        que.append(int(new_method[1]))

    elif new_method[0] == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)

    elif new_method[0] == "size":
        print(len(que))

    elif new_method[0] == "empty":
        if que:
            print(0)
        else:
            print(1)

    elif new_method[0] == "front":
        if que:
            print(que[0])
        else:
            print(-1)

    elif new_method[0] == "back":
        if que:
            print(que[-1])
        else:
            print(-1)

