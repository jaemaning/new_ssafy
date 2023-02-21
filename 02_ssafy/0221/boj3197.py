# boj 3197 - 백조의 호수
from collections import deque
import copy


def bird_bfs(que):

    re_road = deque()
    step = 0

    # 백조 만나지는지 아래 ice_bfs 함수에서 day 마다 검사할 예정
    while que:
        lenq = len(que)
        step += 1
        for _ in range(lenq):
            x, y = que.popleft()

            # for _ in range(R):
            #     print(lake[_])
            # print()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 만났으면 리턴
                if 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == 'L':
                    return 1

                # 길이라면 L 로 길을 변경하며 나가고
                if 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == ".":
                    lake[nx][ny] = "T"
                    que.append((nx, ny))
                    re_road.append((nx, ny))

        # 두번째 돌때부터 시작해서 마지막 값만을 memoization 하기 위해
        # 양갈래로 시작 해야함..
        if step >= 2:
            for _ in range(len(re_road)-lenq):
                re_road.popleft()

        # print(re_road)
    return re_road
    # 길 회복
    # 혹시 녹은곳 까지 미리 가있기 ? memoization
    # for i, j in re_road:
    #     lake[i][j] = "."


def ice_bfs(lake, que):
    # 초기값
    q = deque()

    for i in range(R):
        for j in range(C):
            if lake[i][j] == ".":
                q.append((i, j))

    day = 0

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == "X":
                    lake[nx][ny] = '.'
                    q.append((nx, ny))

        if day:
            memo = bird_bfs(memo)
        else:
            memo = bird_bfs(que)

        day += 1

        if memo == 1:
            return day

    return -1


R, C = map(int, input().split())

# 상하좌우
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 백조의 초기위치찾기
lake = [list(input()) for _ in range(R)]
tmp = copy.deepcopy(lake)
que = deque()
max_ans = -1
for i in range(R):
    for j in range(C):
        if lake[i][j] == "L":
            sx, sy = i, j
            lake[i][j] = "S"
            que.append((sx, sy))
            ans = ice_bfs(lake, que)
            lake[i][j] = "L"
            if ans > max_ans:
                max_ans = ans
            lake = tmp

print(max_ans)
