import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
A = [i for i in range(1, 13)]

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    result = []
    cnt = 0

    for i in range(1 << len(A)):  # 부분집합 개수
        for j in range(len(A)):
            if i & (1 << j):
                result.append(A[j])

        if len(result) == n and sum(result) == k:
            cnt += 1

        result = []

    print(f"#{tc} {cnt}")
