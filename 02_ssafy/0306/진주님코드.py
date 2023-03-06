# 디버깅 완료

import sys
sys.stdin = open('input.txt', 'r')

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0

    for i in range(n):
        for j in range(m):
            cnt = arr[i][j] # 중앙 값 먼저 세기
            for d in range(4):
                for k in range(1, arr[i][j]+1):
                    ni, nj = i + di[d] * k, j + dj[d] * k
                    if 0 <= ni < n and 0 <= nj < m:
                        cnt += arr[ni][nj]

            if cnt > ans:
               ans = cnt

    print(f'#{tc} {ans}')