# 보급로
import sys
sys.stdin = open('input.txt','r')

from collections import deque

def bfs(sx,sy):

    # 시작위치
    q = deque()
    q.append((sx,sy))

    # 상하좌우
    dx = (-1,1,0,0)
    dy = (0,0,-1,1)

    # 값 비교를 위한 배열 만들기
    min_map = [[999999999] * n for _ in range(n)]
    # 시작 위치 값은 0
    min_map[0][0] = 0
    
    while q:

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and min_map[x][y] + l_map[nx][ny] < min_map[nx][ny]:
                min_map[nx][ny] = min_map[x][y] + l_map[nx][ny]
                q.append((nx,ny))
            
    return min_map



T = int(input())

for tc in range(1, T+1):
    n = int(input())

    l_map = [list(map(int,list(input()))) for _ in range(n)]

    min_map = bfs(0,0)

    print(f"#{tc} {min_map[n-1][n-1]}")