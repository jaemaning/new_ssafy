import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    box = []

    for _ in range(n):
        box.append(list(input()))

    # 가로
    for i in range(n):
        for j in range(n - m + 1):
            if box[i][j:] == box[i][j:][::-1]:
                print(f"#{tc} {''.join(box[i][j:])}")

    # 세로
    for i in range(n):
        for j in range(n - m + 1):
            col_list = []
            for k in range(m):
                col_list.append(box[j + k][i])
            if col_list == col_list[::-1]:
                print(f"#{tc} {''.join(col_list)}")
