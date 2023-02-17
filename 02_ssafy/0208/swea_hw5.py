import sys

sys.stdin = open('input.txt', 'r')

str_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for tc in range(1, T+1):
    count_list = [0] * 10
    ttc, n = input().split()
    n_list = list(input().strip().split())

    for idx, s in enumerate(str_list):
        count_list[idx] = n_list.count(s)

    print(ttc)
    for idx, i in enumerate(count_list):
        for _ in range(i):
            print(str_list[idx], end=" ")
    print()