import sys

sys.stdin = open('input.txt', 'r')

def dfs(x, y, cnt):
    # 좌 우 하
    dx = [0, 0, 1]
    dy = [-1, 1, 0]

    # 1인 지점이라면
    if ladder[x][y] == 1:
        # 왼쪽 오른쪽 먼저 탐색
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            # 탈출 했지만 당첨이 아님.
            if nx >= 100:
                return cnt
            # 사다리 다음 경로로 갈때
            elif 0 <= ny < 100 and ladder[nx][ny] == 1 and flag[nx][ny] == False:
                flag[nx][ny] = True
                x, y = nx, ny
                cnt += 1
                return dfs(x, y, cnt)
            # 그 외 (라인 밖으로 나가 0을 만난경우 , 사다리 맵밖으로 나간경우)
            else:
                continue
    else:
        return


for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    min_start = -1
    min_cnt = 99999
    for start in range(100):
        flag = [[False] * 100 for _ in range(100)]
        cnt = dfs(0, start, 0)
        if cnt and cnt < min_cnt:
            min_cnt = cnt
            min_start = start
        
    print(f'#{tc} {min_start}')