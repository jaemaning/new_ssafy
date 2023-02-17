import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    cnt = 1
    max_cnt = -1
    max_v = n_list[0]

    for i in range(1, len(n_list)):
        if n_list[i] > max_v:
            cnt += 1
            max_v = n_list[i]
        else:
            max_v = n_list[i]
            cnt = 1

        if max_cnt < cnt:
            max_cnt = cnt

    print(f"#{tc} {max_cnt}")