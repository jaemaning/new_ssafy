# boj 3197 - 백조의 호수
from collections import deque
import sys
input = sys.stdin.readline

def bird_bfs(que):

    # 중복 제거를 위해 set 으로 저장
    memo = set()

    # 백조 만나지는지 아래 ice_bfs 함수에서 day 마다 검사할 예정
    # 처음은 초기 백조의 위치 (que) 가 들어오고 다음부턴 memorize 된 백조의 이동된 위치 (memo) 가 들어옴
    while que:
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

            # 만약 물 옆에 있는 얼음 이라면? 다음번에 녹아 백조가 이동할 예정이니 memo 해둠
            elif 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == "X":
                memo.add((nx, ny))

    # 중복 제거가 되었다면 다시 큐로 전환하여 return
    return deque(memo)


def ice_bfs(lake, memo, q):

    day = 0

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 물에서 사방 탐색한 결과 얼음 이면 물로 바꾸고 해당 위치를 큐에 저장
                if 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == "X":
                    lake[nx][ny] = '.'
                    q.append((nx, ny))

        # 하루가 끝났다면 백조가 만났는지 검사 초기값은 받아오고 두번쨰부턴 검사 후 위치 저장한값을 넣어줌
        memo = bird_bfs(memo)
        day += 1

        # 만났으면 만날 날짜 리턴
        if memo == 1:
            return day

    # 끝까지 안만나면 -1 리턴
    return -1


# 시작
R, C = map(int, input().split())

# 상하좌우
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 백조의 초기위치찾기
lake = [list(input().strip()) for _ in range(R)]
que = deque()
q = deque()

# 백조의 위치도 물이다.. 백조와 물의 시작 위치 설정하기.
for i in range(R):
    for j in range(C):
        if lake[i][j] == "L":
            que.append((i,j))
            q.append((i,j))

        if lake[i][j] == ".":
            flag = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == "X":
                    flag = 1
            if flag:
                q.append((i,j))

# 시작 위치
start_x, start_y = que.popleft()
start = deque((start_x,start_y))
lake[start_x][start_y] = "T"
ans = ice_bfs(lake, deque([(start_x,start_y)]), q)
print(ans)
