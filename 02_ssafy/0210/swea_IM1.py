# 파리 퇴치
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, 1 + T):
    # n x n 공간 , m x m 파리채
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = -1
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            cnt = 0
            for k in range(m):
                cnt += sum(box[i + k][j:j + m])
            if max_cnt < cnt:
                max_cnt = cnt

    print(f"#{tc} {max_cnt}")
