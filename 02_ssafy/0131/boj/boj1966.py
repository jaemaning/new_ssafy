# boj 1966 프린터큐
from collections import deque

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    que = list(map(int, input().split()))
    cnt = 0

    while que:
        max_v = max(que)
        if que[0] != max_v:
            # target index 즉 최댓값 위치를 찾아 맨앞으로 배치
            max_index = que.index(max_v)
            que = que[max_index:] + que[:max_index]
            if m - max_index < 0:
                m = len(que) + (m - max_index)
            else:
                m -= max_index

        if m == 0:
            cnt += 1
            break
        del que[0]
        m -= 1
        cnt += 1

    print(cnt)