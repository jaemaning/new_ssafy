# 중복 가능 perm
import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
import copy

def perm(w,n):

    if len(perm_list) == n:
        result.append(perm_list[:])
        return
    
    for i in range(w):
        perm_list.append(i)
        perm(w,n)
        perm_list.pop()


def bfs(q,bomb_map):
    global min_v
    # print(bomb_map)


    while q:
        # print(q)
        # for i in range(h):
        #     print(bomb_map[i])
        sy = q.popleft()
        qq = deque()

        for sx in range(h):
            if bomb_map[sx][sy] != 0:
                # 시작
                qq.append((sx,sy,bomb_map[sx][sy]))
                bomb_map[sx][sy] = 0

                while qq:
                    x,y,splash = qq.popleft()

                    for k in range(4):
                        for dist in range(1,splash):
                            nx = x + (dx[k] * dist)
                            ny = y + (dy[k] * dist)

                            if 0 <= nx < h and 0 <= ny < w and bomb_map[nx][ny] != 0:
                                qq.append((nx,ny,bomb_map[nx][ny]))
                                bomb_map[nx][ny] = 0
                
                # 맵 정렬 필요
                for i in range(w-1,-1,-1):

                    sort_q = deque()

                    for j in range(h-1,-1,-1):
                        sort_val = bomb_map[j][i]
                        if sort_val != 0:
                            sort_q.append(sort_val)
                            bomb_map[j][i] = 0
                    
                    height = h
                    for _ in range(len(sort_q)):
                        val = sort_q.popleft()
                        height -= 1
                        bomb_map[height][i] = val
                    
                break

    cnt = 0
    for i in range(w):
        for j in range(h):
            if bomb_map[j][i] != 0:
                cnt += 1

    min_v = min(min_v, cnt)
    return



T = int(input())

for tc in range(1, T+1):
    n, w, h = map(int, input().split())

    b_map = [list(map(int, input().split())) for _ in range(h)]
    check_list = [i for i in range(w)]
    perm_list = []
    result = []

    perm(w,n)

    min_v = 9999999
    
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in result:
        if min_v == 0:
            break
        bb_map = copy.deepcopy(b_map)
        q = deque(i)
        bfs(q,bb_map)

    print(f'#{tc} {min_v}')