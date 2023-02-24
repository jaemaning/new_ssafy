# debug 검사용
import sys
sys.stdin = open('input.txt','r')

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

T = int(input())

block = [[], [1, 3, 0, 2], [3, 0, 1, 2], [2, 0, 3, 1], [1, 2, 3, 0], [1, 0, 3, 2]]

warm_list = [6,7,8,9,10]

def check(sx, sy):
    max_v = 0
    for d in range(4):
        cnt = 0
        direction = d
        x = sx
        y = sy
        while True:

            nx = sx + dx[direction]
            ny = sy + dy[direction]

            if 0 <= nx < N and 0 <= ny < N:

                if (sx == nx and sy == ny):
                    break

                elif map_list[nx][ny] == 1:
                    direction = block[1][direction]
                    cnt += 1

                elif map_list[nx][ny] == 2:
                    direction = block[2][direction]
                    cnt += 1

                elif map_list[nx][ny] == 3:
                    direction = block[3][direction]
                    cnt += 1

                elif map_list[nx][ny] == 4:
                    direction = block[4][direction]
                    cnt += 1

                elif map_list[nx][ny] == 5:
                    direction = block[5][direction]
                    cnt += 1

                elif map_list[nx][ny] in warm_list:
                    find = warm_hall[map_list[nx][ny]].index([nx, ny])
                    re_x, re_y = warm_hall[map_list[nx][ny]].pop(find)

                    nx, ny = warm_hall[map_list[nx][ny]][0]
                    warm_hall[map_list[nx][ny]].append([re_x, re_y])

                elif map_list[nx][ny] == -1:
                    break

                # nx = x + dx[direction]
                # ny = y + dy[direction]

                # x, y = nx, ny

            else:
                cnt += 1
                # nx = x + dx[block[5][direction]]
                # ny = y + dy[block[5][direction]]
                direction = block[5][direction]

            x, y = nx, ny


        if cnt > max_v:
            max_v = cnt

    return max_v


for test_case in range(1, T + 1):
    warm_hall = [0, 0, 0, 0, 0, 0, [], [], [], [], []]
    N = int(input())
    result = 0

    map_list = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if map_list[i][j] in warm_list:
                warm_hall[map_list[i][j]].append([i, j])

    for i in range(N):
        for j in range(N):
            if map_list[i][j] == 0:
                max_cnt = check(i, j)
                if max_cnt > result:
                    result = max_cnt

    print(f'#{test_case} {result}')