# 벽돌깨기
import copy

def dfs(cnt, block_map):
    global min_v

    if cnt == n:
        v = 0
        for i in range(w):
            for j in range(h):
                if block_map[j][i] != 0:
                    v += 1

        min_v = min(min_v, v)
        return


    q = deque()
    back_q = deque()
    
    for i in range(w):
        for j in range(h):
            # 충돌 발생
            if block_map[j][i] != 0:
                q.append((j,i))
                back_map = copy.deepcopy(block_map)
                block_map[j][i] = 0

                while q:
                    x,y = q.popleft()

                    for k in range(4):
                        for dist in range(1,block_map[x][y]):
                            nx = x + dx[k+dist]
                            ny = y + dy[k+dist]

                            if 0 <= nx < h and 0 <= ny < w and block_map[nx][ny] != 0:
                                q.append((nx,ny))
                                block_map[nx][ny] = 0

                # 맵 정렬 (0 버블?)
                for i in range(w-1,-1,-1):

                    sort_q = deque()

                    for j in range(h-1,-1,-1):
                        sort_val = block_map[j][i]
                        if sort_val != 0:
                            sort_q.append(sort_val)
                    
                    height = h-1
                    for k in range(len(sort_q)):
                        height -= 1
                        block_map[height][i] = sort_q[k]


                dfs(cnt+1, block_map)
                # 맵 되돌리는 과정
                block_map = copy.deepcopy(back_map)




from collections import deque
T = int(input())

for tc in range(1,T+1):
    n, w, h = map(int, input().split())
    
    block_map = [list(map(int, input().split())) for _ in range(h)]

    min_v = 999999

    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    dfs(0, block_map)
    print(min_v)