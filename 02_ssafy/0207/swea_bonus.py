# 활주로 건설
import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    n, length = map(int, input().split())
    box = []
    cnt = 0
    flag_x = [0] * n
    flag_y = [0] * n

    for _ in range(n):
        box.append(list(map(int, input().split())))

    # 가로줄 체크
    # 왼 -> 오
    for x in range(n):
        pre_num = box[x][0]
        flag_cnt = 0
        for i in range(n):
            # 높이 차 2 이상
            if abs(pre_num - box[x][i]) >= 2:
                break

            if box[x][i] == pre_num:
                flag_cnt += 1

            elif pre_num < box[x][i]:
                # flag_cnt 연속된 평지 수
                # 통과 케이스
                if flag_cnt >= length:
                    flag_cnt = 1
                    pre_num = box[x][i]

                else:
                    break
            # pre_num > i 인 case => flag_cnt 값만 1로 되돌린 후 오 -> 왼에서 체크
            else:
                flag_cnt = 1
                pre_num = box[x][i]
                for j in range(1, length):
                    if i + j < n:
                        if box[x][i+j] == box[x][i]:
                            flag_cnt -= 1
                        else:
                            break
                    else:
                        break
                else:
                    flag_cnt -= 1
        else:
            flag_x[x] += 1

    # 오 -> 왼
    for x in range(n):
        pre_num = box[x][-1]
        flag_cnt = 0
        for i in range(n - 1, -1, -1):
            # 높이 차 2 이상
            if abs(pre_num - box[x][i]) >= 2:
                break

            if box[x][i] == pre_num:
                flag_cnt += 1

            elif pre_num < box[x][i]:
                # flag_cnt 연속된 평지 수
                # 통과 케이스
                if flag_cnt >= length:
                    flag_cnt = 1
                    pre_num = box[x][i]

                else:
                    break
            # pre_num > i 인 case => flag_cnt 값만 1로 되돌린 후 오 -> 왼에서 체크
            else:
                flag_cnt = 1
                pre_num = box[x][i]
                for j in range(1, length):
                    if i + j < n:
                        if box[x][i+j] == box[x][i]:
                            flag_cnt -= 1
                        else:
                            break
                    else:
                        break
                else:
                    flag_cnt -= 1
        else:
            flag_x[x] += 1

    # 세로줄 체크
    # 위 아래
    for x in range(n):
        pre_num = box[0][x]
        flag_cnt = 0
        for i in range(n):
            # 높이 차 2 이상
            if abs(pre_num - box[i][x]) >= 2:
                break

            if box[i][x] == pre_num:
                flag_cnt += 1

            # pre_num < box[i][x] 인 경우 즉 이전 숫자보다 해당숫자가 더 클때
            elif pre_num < box[i][x]:
                # flag_cnt 연속된 평지 수
                # 통과 케이스
                if flag_cnt >= length:
                    flag_cnt = 1
                    pre_num = box[i][x]

                else:
                    break
            # pre_num > box[i][x] 인 case => flag_cnt 값만 1로 되돌린 후 오 -> 왼에서 체크
            else:
                flag_cnt = 1
                pre_num = box[i][x]
                for j in range(1, length):
                    if i + j < n:
                        if box[i+j][x] == box[i][x]:
                            flag_cnt -= 1
                        else:
                            break
                    else:
                        break
                else:
                    flag_cnt -= 1
        else:
            flag_y[x] += 1

    # 아래 위
    for x in range(n):
        pre_num = box[-1][x]
        flag_cnt = 0
        for i in range(n - 1, -1, -1):
            # 높이 차 2 이상
            if abs(pre_num - box[i][x]) >= 2:
                break

            if box[i][x] == pre_num:
                flag_cnt += 1

            elif pre_num < box[i][x]:
                # flag_cnt 연속된 평지 수
                # 통과 케이스
                if flag_cnt >= length:
                    flag_cnt = 1
                    pre_num = box[i][x]

                else:
                    break
            # pre_num > box[i][x] 인 case => flag_cnt 값만 1로 되돌린 후 오 -> 왼에서 체크
            else:
                flag_cnt = 1
                pre_num = box[i][x]
                for j in range(1, length):
                    if i + j < n:
                        if box[i+j][x] == box[i][x]:
                            flag_cnt -= 1
                        else:
                            break
                    else:
                        break
                else:
                    flag_cnt -= 1
        else:
            flag_y[x] += 1

    print(flag_x, flag_y)

    # for q in flag_x:
    #     if q == 2:
    #         cnt += 1
    #
    # for qq in flag_y:
    #     if qq == 2:
    #         cnt += 1
    #
    # print(f"#{tc} {cnt}")
