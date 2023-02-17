import sys
inpust = sys.stdin.readline


def mapinfunc(x):
    global pre_x

    ans = int(x) + pre_x
    pre_x = ans

    return ans


n, m = map(int, input().split())
pre_x = 0
n_list = list(map(mapinfunc, input().split()))
n_list.append(0)

for _ in range(m):
    i, j = map(int, input().split())
    print(n_list[j-1] - n_list[i-2])
