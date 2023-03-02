# 진기의 최고급 붕어빵
import sys
sys.stdin = open('input.txt','r')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int,input().split())

    people_list = list(map(int,input().split()))
    people_list.sort()
    q = deque(people_list)

    ans = 'Possible'

    bread_cnt = 0
    cnt = 1

    while q:
        person = q.popleft()

        if person // m == 0:
            ans = 'Impossible'
            break
        else:
            if (person // m) * k - cnt < 0:
                ans = 'Impossible'
                break

        cnt += 1

    print(f'#{tc} {ans}')
