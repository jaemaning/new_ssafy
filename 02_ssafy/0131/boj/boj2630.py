import sys

input = sys.stdin.readline


def box_check(row, col, n):
    blue_cnt = 0
    white_cnt = 0

    for i in range(n):
        if sum(box[row+i][col:col+n]) == 1 * n:
            blue_cnt += 1
        elif sum(box[row+i][col:col+n]) == 0:
            white_cnt += 1

    if blue_cnt == n:
        result[0] += 1
        return
    elif white_cnt == n:
        result[1] += 1
        return
    else:
        box_check(row, col, n // 2)
        box_check(row + (n // 2), col, n // 2)
        box_check(row, col + (n // 2), n // 2)
        box_check(row + (n // 2), col + (n // 2), n // 2)


n = int(input())
box = [list(map(int, input().split())) for _ in range(n)]
result = [0, 0]

box_check(0, 0, n)
print(result[1], result[0], sep="\n")
