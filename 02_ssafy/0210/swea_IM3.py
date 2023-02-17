# 고대 유적
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    t_box = list(map(list, zip(*box)))
    max_cnt = -1

    for x in range(n):
        line = box[x]
        cnt = 0
        for px in line:
            if px == 1:
                cnt += 1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 0
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 0

    for x in range(m):
        line = t_box[x]
        cnt = 0
        for px in line:
            if px == 1:
                cnt += 1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 0
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 0

    print(f"#{tc} {max_cnt}")
