# 4일차 - 종이 붙이기

T = int(input())
cache = [0] * 1001
cache[1] = 1
cache[2] = 3

for tc in range(1, T + 1):
    n = int(input()) // 10
    for i in range(3, n + 1):
        # 홀수
        if i % 2 and cache[i] == 0:
            cache[i] = (cache[i - 1] * 2) - 1
        # 짝수
        if i % 2 == 0 and cache[i] == 0:
            cache[i] = (cache[i - 1] * 2) + 1

    print(f"#{tc} {cache[n]}")
