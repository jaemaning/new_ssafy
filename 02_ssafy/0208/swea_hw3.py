import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())
    box = []
    max_v = -1
    temp1 = 0
    temp2 = 0

    # 열 + 박스만들기
    for _ in range(100):
        row = list(map(int, input().split()))
        if max_v < sum(row):
            max_v = sum(row)
        box.append(row)

    # 행
    for j in range(100):
        temp = 0
        for i in range(100):
            temp += box[i][j]

        if temp > max_v:
            max_v = temp

    # 대각선

    for k in range(100):
        temp1 += box[k][k]

    for idx, k in enumerate(range(99, -1, -1)):
        temp2 += box[idx][k]

    if temp1 > max_v:
        max_v = temp1

    if temp2 > max_v:
        max_v = temp2

    print(f"#{tc} {max_v}")
