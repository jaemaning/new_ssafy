# 오큰수
import sys

input = sys.stdin.readline

a = int(input())

n_list = list(map(int, input().split()))

stack = []
result = [-1] * a

'''
14
3 1 15 6 11 20 5 2 7 9 4 8 10 22
'''

# 앞부터 가자
for i in range(a - 1):
    if n_list[i] < n_list[i + 1]:
        result[i] = n_list[i + 1]
        while stack:
            x, idx = stack.pop()
            if x < n_list[i + 1]:
                result[idx] = n_list[i + 1]
            else:
                stack.append((x, idx))
                break
    else:
        stack.append((n_list[i], i))

print(' '.join(map(str, result)))
