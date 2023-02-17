# 4일차 - 종이 붙이기

T = int(input())


def recur(n):
    if n == 1:
        return 1
    # 홀수
    if n % 2:
        return recur(n - 1) * 2 - 1
    # 짝수
    else:
        return recur(n - 1) * 2 + 1


for tc in range(1, T + 1):
    n = int(input()) // 10
    print(recur(n))
