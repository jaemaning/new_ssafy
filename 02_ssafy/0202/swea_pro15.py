import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    cnt = 0
    box = [[0] * 10 for _ in range(10)]

    for _ in range(n):
        x1, y1, x2, y2, color = map(int, input().split())

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if color == 1:
                    box[i][j] += 1
                if color == 2:
                    box[i][j] += 2

    for i in range(10):
        for j in range(10):
            if box[i][j] == 3:
                cnt += 1

    print(f"#{tc} {cnt}")
