# 믈놀이를 가자
import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


# 1번 방법
def bfs(sx, sy):
    '''
    :param sx: 시작 x 위치
    :param sy: 시작 y 위치
    :return: 최소 이동 횟수
    '''
    day = 1
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((sx, sy))

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 다음 위치가 범위안에 있고 방문한적이 없다면
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                    # 만약 W 물을 만났다면 ? 탈출
                    if w_map[nx][ny] == "W":
                        return day
                    # 계속 땅이라면 ? 계속 진행
                    else:
                        visited[nx][ny] = True
                        q.append((nx, ny))

        day += 1


# 2번 방법 융합
def cal_dist(wp, lp):

    for lx, ly in lp:
        min_dist = 9999999
        for wx, wy in wp:
            dist = abs(lx - wx) + abs(ly - wy)
            min_dist = min(dist, min_dist)
        dp.append(min_dist)

    return


T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    w_map = [list(input()) for _ in range(n)]
    ans = 0
    # 상하좌우
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    wp = []
    lp = []
    dp = []

    for i in range(n):
        for j in range(m):
            # 땅과 물을 모두 각각 저장
            if w_map[i][j] == 'L':
                lp.append([i, j])
            else:
                wp.append([i, j])

    # 물이 땅에 비해 굉장히 적을 경우 이 방법 이 효과적
    if len(wp) < len(lp):
        cal_dist(wp, lp)
        ans = sum(dp)
    # 위에 해당 안되는 경우라면 이 경우가 효과적
    else:
        for i, j in lp:
            score = bfs(i, j)
            ans += score

    print(f"#{tc} {ans}")
