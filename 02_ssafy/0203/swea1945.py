import sys

sys.stdin = open("input.txt", "r")

n_list = [2, 3, 5, 7, 11]
result = [0] * 5

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    for idx, i in enumerate(n_list):
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1

        result[idx] = cnt

    print(f"#{tc} {' '.join(map(str, result))}")
