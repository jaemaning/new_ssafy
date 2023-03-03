# 줄기세포배양
import sys
sys.stdin = open('input.txt','r')

from collections import deque

def bfs(q):

    # 상하좌우
    dx = (-1,1,0,0)
    dy = (0,0,-1,1)

    time = 0

    while time != k:
        time += 1

        for _ in range(len(q)):
            # x좌표 y좌표 s == 초기 값 원본
            x, y, s = q.popleft()

            if c_map[x][y] == 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 방문 한적이 없으면
                    if c_map[nx][ny] == -1:
                        c_map[nx][ny] = s
                        q.append()

            else:
                c_map[x][y] -= 1
                q.append(x,y,s)


            


    return



T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    c_map = [[-1] * (2*k+m) for _ in range(k)]

    for _ in range(n):
        fe_line = [-1] * k
        n_line = list(map(int,input().split()))
        new_line = fe_line + n_line + fe_line
        c_map.append(new_line)

    for _ in range(k):
        padding = [-1] * (2*k+m)
        c_map.append(padding)

    q = deque()
    for i in range(n):
        for j in range(m):
            if c_map[k+i][k+j] != 0:
                q.append((k+i, k+j, c_map[k+i][k+j]))
            else:
                c_map[k+i][k+j] = -1
        
    for i in range(2*k+n):
        print(c_map[i])