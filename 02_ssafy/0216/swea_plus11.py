import sys

sys.stdin = open('input.txt', 'r')


def othello(x, y, stone, n):
    # 내가 둔 돌 : stone , 적 돌 : target
    if stone == 1:
        target = 2
    else:
        target = 1

    # 상, 하 , 좌, 우 , 좌상, 우상, 좌하, 우하 검사
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    # 8 방향 검사 시작
    for i in range(8):

        nx = x + dx[i]
        ny = y + dy[i]
        # 공격을 해야할지 안해야할지 flag 로 구분
        flag = 0
        # 공격을 한다면 즉) flag == 1 이면 여태까지 지나온 길을 바꿔주겠다.
        atk_list = []

        # 다음 위치가 범위내에 들어오고, 다음 위치에 적돌이있다면?
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == target:
            # 적돌들을 공격리스트에 담기
            atk_list.append((nx, ny))
            while 1:
                new_x, new_y = nx, ny
                nx = new_x + dx[i]
                ny = new_y + dy[i]
                atk_list.append((nx, ny))
                # 계속 가면서 다음 위치가 있을떄까지 가고, 가다가 내 돌이 있다면?
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == stone:
                        # 공격 방향을 찾았다 공격 flag on
                        flag = 1
                        break
                    elif board[nx][ny] == 0:
                        break
                else:
                    break
        # 공격 flag 가 켜졌다면 ? 공격 시작
        if flag:
            while atk_list:
                atk_x, atk_y = atk_list.pop()
                board[atk_x][atk_y] = stone


T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    # 처음 시작 위치 돌
    # 백돌 : 2
    board[(n // 2) - 1][(n // 2) - 1] = 2
    board[(n // 2)][(n // 2)] = 2

    # 흑돌 : 1
    board[(n // 2)][(n // 2) - 1] = 1
    board[(n // 2) - 1][(n // 2)] = 1

    for _ in range(m):
        y, x, stone = map(int, input().split())
        board[x-1][y-1] = stone
        othello(x-1, y-1, stone, n)

    cnt_1 = 0
    cnt_2 = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt_1 += 1
            elif board[i][j] == 2:
                cnt_2 += 1

    print(f"#{tc} {cnt_1} {cnt_2}")

