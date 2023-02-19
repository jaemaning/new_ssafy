# 파리퇴치 3
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
# 상하좌우
dx1 = (-1, 1, 0, 0)
dy1 = (0, 0, -1, 1)
# 좌상 우상 좌하 우하
dx2 = (-1, -1, 1, 1)
dy2 = (-1, 1, -1, 1)

for tc in range(1, T+1):
    n, m = map(int, input().split())

    box = [list(map(int, input().split())) for _ in range(n)]

    max_cnt = 0

    for x in range(n):
        for y in range(n):
            cnt1 = cnt2 = box[x][y]
            for i in range(4):
                for j in range(1, m):
                    nx1 = x + (dx1[i] * j)
                    ny1 = y + (dy1[i] * j)
                    nx2 = x + (dx2[i] * j)
                    ny2 = y + (dy2[i] * j)

                    if 0 <= nx1 < n and 0 <= ny1 < n:
                        cnt1 += box[nx1][ny1]
                    if 0 <= nx2 < n and 0 <= ny2 < n:
                        cnt2 += box[nx2][ny2]
            
            if cnt1 > max_cnt:
                max_cnt = cnt1
            if cnt2 > max_cnt:
                max_cnt = cnt2
    
    print(f"#{tc} {max_cnt}")