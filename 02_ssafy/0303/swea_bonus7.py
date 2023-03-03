# 정식이의 은행업무
import sys

sys.stdin = open('input.txt', 'r')


def bitoten(arr):
    ans = 0
    for i in range(len(arr)):
        ans += int(arr[i]) * (2 ** (len(arr) - i - 1))

    return ans


def tetoten(arr):
    ans = 0
    for i in range(len(arr)):
        ans += int(arr[i]) * (3 ** (len(arr) - i - 1))

    return ans


T = int(input())

for tc in range(1, T + 1):
    bi = list(input())
    te = list(input())

    bi_list = []
    te_list = []

    for i in range(len(bi)):
        copy_bi = bi[:]
        if copy_bi[i] == "1":
            copy_bi[i] = "0"
        else:
            copy_bi[i] = "1"

        bi_list.append(copy_bi[:])

    for i in range(len(te)):
        copy_te = te[:]
        if copy_te[i] == "0":
            for j in range(1, 3):
                copy_te[i] = str(j)
                te_list.append(copy_te[:])
        elif copy_te[i] == "1":
            copy_te[i] = "2"
            te_list.append(copy_te[:])
            copy_te[i] = "0"
            te_list.append(copy_te[:])
        else:
            for j in range(2):
                copy_te[i] = str(j)
                te_list.append(copy_te[:])

    for bi in bi_list:
        for te in te_list:
            if bitoten(bi) == tetoten(te):
                result = bitoten(bi)
                break
        else:
            continue
        break

    print(f'#{tc} {result}')
