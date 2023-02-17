import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, 1 + T):
    n, k = map(int, input().split())
    cnt = 0

    box = [list(map(int, input().split())) for _ in range(n)]

    # 가로
    for x in range(n):
        for y in range(n - k + 1):
            check = 0
            for i in range(k):
                check += box[x][y + i]

            # 양옆 범위 확인 후, 1확인
            # y가 start 시작점 k 길이까지
            if 0 <= y - 1 and y + k < n:
                if check == k and box[x][y - 1] == 0 and box[x][y + k] == 0:
                    cnt += 1
            elif 0 <= y - 1:
                if check == k and box[x][y - 1] == 0:
                    cnt += 1
            elif y + k < n:
                if check == k and box[x][y + k] == 0:
                    cnt += 1
    # 세로
    for x in range(n):
        for y in range(n - k + 1):
            check = 0
            for i in range(k):
                check += box[y + i][x]

            # 양옆 범위 확인 후, 1확인
            # y가 start 시작점 k 길이까지
            if 0 <= y - 1 and y + k < n:
                if check == k and box[y - 1][x] == 0 and box[y + k][x] == 0:
                    cnt += 1
            elif 0 <= y - 1:
                if check == k and box[y - 1][x] == 0:
                    cnt += 1
            elif y + k < n:
                if check == k and box[y + k][x] == 0:
                    cnt += 1

    print(f"#{tc} {cnt}")
