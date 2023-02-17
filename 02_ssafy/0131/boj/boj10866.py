# boj 10866 덱
import sys
from collections import deque

input = sys.stdin.readline
que = deque()

tc = int(input())

for _ in range(tc):
    do_list = list(input().split())

    if do_list[0] == "push_front":
        que.insert(0, do_list[1])

    if do_list[0] == "push_back":
        que.append(do_list[1])

    if do_list[0] == "pop_front":
        if que:
            print(que.popleft())
        else:
            print(-1)

    if do_list[0] == "pop_back":
        if que:
            print(que.pop())
        else:
            print(-1)

    if do_list[0] == "size":
        print(len(que))

    if do_list[0] == "empty":
        if que:
            print(0)
        else:
            print(1)

    if do_list[0] == "front":
        if que:
            print(que[0])
        else:
            print(-1)

    if do_list[0] == "back":
        if que:
            print(que[-1])
        else:
            print(-1)

