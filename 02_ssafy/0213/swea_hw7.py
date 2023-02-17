# 파스칼의 삼각형

T = int(input())
box = [[0] * 10 for i in range(10)]
for i in range(10):
    box[i][i] = 1
    box[i][0] = 1


def pascal(n):
    global target_number

    while target_number < n:
        for i in range(target_number + 1):
            if box[target_number][i] == 0:
                box[target_number][i] = box[target_number-1][i-1] + box[target_number-1][i]

        target_number += 1


target_number = 2
pascal(10)

for tc in range(1, T + 1):
    n = int(input())
    print(f"#{tc}")
    for row in box[:n]:
        print(" ".join(map(str, row)).strip(" 0"))
