# boj 5430

import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):

    prompts_ = input().strip()
    n = int(input())
    n_list = input().strip()[1:-1].split(',')
    que = deque(n_list)
    r_cnt = 0

    if n == 0:
        que = deque([])

    for prom in prompts_:
        if prom == "R":
            r_cnt += 1
        else:
            if que:
                if r_cnt % 2 == 0:
                    que.popleft()
                else:
                    que.pop()
            else:
                print("error")
                break
    
    else:
        if r_cnt % 2 == 0:
            print("[",",".join(map(str,que)),"]",sep="")
        else:
            que.reverse()
            print("[",",".join(map(str,que)),"]",sep="")