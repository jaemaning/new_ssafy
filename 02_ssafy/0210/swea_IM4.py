# 파리퇴치 3
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = -1
    # print(box)

    # 상 하 좌 우 좌상 우상 우하 좌하
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]

    # + 모양(0-3)
    # 중심 이동
    for x in range(n):
        for y in range(n):
            # 발사 범위 + 중심
            cnt = box[x][y]
            for i in range(1, m):
                ndx = list(map(lambda q: q * i, dx))
                ndy = list(map(lambda q: q * i, dy))
                for j in range(4):
                    # +모양 범위 지정
                    nx = x + ndx[j]
                    ny = y + ndy[j]
                    if 0 <= nx < n and 0 <= ny < n:
                        cnt += box[nx][ny]
                        # print(f"cnt : {cnt}, box : {box[nx][ny]}")
                if cnt > max_cnt:
                    max_cnt = cnt

    # x 모양(4-7)
    # 중심 이동
    for x in range(n):
        for y in range(n):
            # 발사 범위 + 중심
            cnt = box[x][y]
            for i in range(1, m):
                ndx = list(map(lambda q: q * i, dx))
                ndy = list(map(lambda q: q * i, dy))
                for j in range(4,8):
                    # +모양 범위 지정
                    nx = x + ndx[j]
                    ny = y + ndy[j]
                    if 0 <= nx < n and 0 <= ny < n:
                        cnt += box[nx][ny]
                        # print(f"cnt : {cnt}, box : {box[nx][ny]}")
                if cnt > max_cnt:
                    max_cnt = cnt


    print(f"#{tc} {max_cnt}")
