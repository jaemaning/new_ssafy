import sys

sys.stdin = open('input.txt', 'r')

'''
T = int(input())

for tc in range(1,T+1):
    n = int(input())
    n_list = list(map(int, input().split()))
    a_list = sorted(n_list)
    b_list = sorted(n_list, reverse=True)
    result = []
    for i in range(5):
        result.append(b_list[i])
        result.append(a_list[i])

    print(f'#{tc} {" ".join(map(str, result))}')
'''

# sort 안쓰고 풀기.
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    result = [0] * n

    for i in range(n):
        max_idx = i
        min_idx = i
        if i % 2:
            for j in range(i, n):
                if n_list[j] < n_list[min_idx]:
                    min_idx = j
            result[i] = n_list[min_idx]
            n_list[i], n_list[min_idx] = n_list[min_idx], n_list[i]
        else:
            for j in range(i, n):
                if n_list[j] > n_list[max_idx]:
                    max_idx = j
            result[i] = n_list[max_idx]
            n_list[i], n_list[max_idx] = n_list[max_idx], n_list[i]

    print(f"#{tc} {' '.join(map(str, result[:10]))}")
