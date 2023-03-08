# 히스토그램
import sys
input = sys.stdin.readline

n = int(input())

result = n
stack = []
max_h = 0
max_h_idx = 0
min_h = 9999999999999999
min_h_idx = 0
pre = 0

for i in range(n):
    h = int(input())
    # 만약 현재 높이가 이전 높이보다 작다면?
    if h <= pre:
        if h < pre:
            stack = []
        # 역대 최저 높이보다 현재 높이가 또 작다면?
        if min_h >= h:
            min_h = h
            result = max(result, h * (i+1))
            min_h_idx = i
        # 역대 최저 높이보단 현재 높이가 크다면?
        else:
            result = max(result, h * (i-min_h_idx))
    # 현재 높이가 이전 높이보다 크다면?
    else:
        result = max(result, h)
        stack.append(pre)
        result = max(result, pre * len(stack))
    pre = h

result = max(result, n*min_h)
print(result)