import sys

sys.stdin = open("input.txt", 'r')

T = int(input())

for tc in range(1, 1 + T):
    box = [list(map(int, input().split())) for _ in range(9)]
    flag = 1

    # 가로
    for i in range(9):
        for num in range(1, 10):
            if num in box[i]:
                pass
            else:
                flag = 0
                break
        else:
            continue
        break


    # 세로
    for i in range(9):
        col_list = []
        for j in range(9):
            col_list.append(box[j][i])
        for k in range(1, 10):
            if num in col_list:
                pass
            else:
                flag = 0
                break
        else:
            continue
        break

    # 네모
    for x in [3, 6, 9]:
        nemo = []
        for i in range(x - 3, x):
            for j in range(3):
                nemo.append(box[i][j])

        for num in range(1, 10):
            if num in nemo:
                pass
            else:
                flag = 0
                break
        print(nemo)

            # nemo = []
            # for k in range(3, 6):
            #     nemo.append(box[i][j])
            # for num in range(1, 10):
            #     if num in nemo:
            #         pass
            #     else:
            #         flag = 0
            #         break
            #
            # nemo = []
            # for m in range(6, 9):
            #     nemo.append(box[i][j])
            # for num in range(1, 10):
            #     if num in nemo:
            #         pass
            #     else:
            #         flag = 0
            #         break

    print(flag)