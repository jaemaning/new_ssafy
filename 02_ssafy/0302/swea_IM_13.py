# 러시아 국기 같은 깃발
import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T + 1):
    n, m = map(int,input().split())
    aa = [i for i in range(n)]
    ans = 999999999

    flag_map = [input().strip() for _ in range(n)]

    for i in range(1, n - 1):
        for start in range(1, n - i):
            cnt = 0
            w_list = aa[0:start]
            b_list = aa[start:start + i]
            r_list = aa[start + i:n]

            for w in w_list:
                cnt += m - flag_map[w].count("W")
            for b in b_list:
                cnt += m - flag_map[b].count("B")
            for r in r_list:
                cnt += m - flag_map[r].count("R")

            ans = min(ans, cnt)

    print(f'#{tc} {ans}')
