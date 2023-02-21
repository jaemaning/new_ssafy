# boj 3197 - 백조의 호수
from collections import deque

def bird_bfs(que):

    memo = deque()

    # 백조 만나지는지 아래 ice_bfs 함수에서 day 마다 검사할 예정
    while que:
        lenq = len(que)

        for _ in range(lenq):
            x, y = que.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 만났으면 리턴
                if 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == 'L':
                    return 1

                # 길이라면 T 로 길을 변경하며 나가고
                if 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == ".":
                    lake[nx][ny] = "T"
                    que.append((nx, ny))

                elif 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == "X":
                    memo.append((nx, ny))

    return memo


def ice_bfs(lake, memo):
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

        memo = bird_bfs(memo)

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
que = deque()

for i in range(R):
    for j in range(C):
        if lake[i][j] == "L":
            sx, sy = i, j
            lake[i][j] = "."
            que.append((sx, sy))
            ans = ice_bfs(lake, que)
            break
    else:
        continue
    break

print(ans)
