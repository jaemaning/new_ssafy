# 우주선 착륙2
import sys
sys.stdin = open('input.txt', 'r')

# 좌상 상 우상 좌 우 좌하 하 우하
dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    space_map = [list(map(int,input().split())) for _ in range(n)]

    result = 0

    for x in range(n):
        for y in range(m):
            # 현재 위치의 높이
            now = space_map[x][y]
            cnt = 0

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and space_map[nx][ny] < now:
                    cnt += 1
            
            if cnt >= 4:
                result += 1
    
    print(f"#{tc} {result}")