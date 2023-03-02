# 오목 판정
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    ans = "NO"

    board = [input().strip() for _ in range(n)]
    t_board = list(map(list, zip(*board)))

    # 가로 세로
    for i in range(n):
        cnt = 0
        for j in range(n):
            if board[i][j] == "o":
                cnt += 1
            else:
                cnt = 0

            if cnt == 5:
                ans = "YES"

    for i in range(n):
        cnt = 0
        for j in range(n):
            if t_board[i][j] == "o":
                cnt += 1
            else:
                cnt = 0

            if cnt == 5:
                ans = "YES"


    # 대각선 우하
    for i in range(n - 4):
        for j in range(n - 4):
            cnt = 0
            for k in range(5):
                if board[i + k][j + k] == 'o':
                    cnt += 1
                else:
                    cnt = 0

            if cnt == 5:
                ans = 'YES'

    # 대각선 좌하
    for i in range(n - 4):
        for j in range(n - 1, 3, -1):
            cnt = 0
            for k in range(5):
                if board[i + k][j - k] == 'o':
                    cnt += 1
                else:
                    cnt = 0

            if cnt == 5:
                ans = 'YES'

    print(f'#{tc} {ans}')
