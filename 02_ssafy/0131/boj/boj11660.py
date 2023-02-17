import sys
input = sys.stdin.readline

n, m = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]
sum_box = [[0] * n for _ in range(n)]

sum_box[0][0] = box[0][0]

for i in range(n):
    for j in range(n):
        if i > j:
            ans = 0
            for k in range(j+1):
                ans += box[i][k]
            ans += sum_box[i-1][j]
            sum_box[i][j] = ans
        else:
            ans = 0
            for k in range(i+1):
                ans += box[k][j]
            ans += sum_box[i][j-1]
            sum_box[i][j] = ans

for _ in range(m):

    x1, y1, x2, y2 = map(int, input().split())
    if x1 >= 2 and y1 >= 2:
        result = sum_box[x2-1][y2-1] + sum_box[x1-2][y1-2] - \
            sum_box[x1-2][y2-1] - sum_box[x2-1][y1-2]
    elif x1 >= 2:
        result = sum_box[x2-1][y2-1] - sum_box[x1-2][y2-1]
    elif y1 >= 2:
        result = sum_box[x2-1][y2-1] - sum_box[x2-1][y1-2]
    else:
        result = sum_box[x2-1][y2-1]

    print(result)
