# N 과 M (8)
import sys
input = sys.stdin.readline


def comb(m):

    if len(comb_list) == m:
        print(" ".join(map(str, comb_list)))
        return

    start = n_list.index(comb_list[-1]) if comb_list else 0
    for i in range(start, n):
        comb_list.append(n_list[i])
        comb(m)
        comb_list.pop()


n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()

result = []
comb_list = []

comb(m)
