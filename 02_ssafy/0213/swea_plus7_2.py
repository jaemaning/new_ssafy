# 4일차 - 거듭제곱
import sys
sys.stdin = open('input.txt', 'r')

def dubblelin(n, m):
    if m == 1:
        return n
    return n * dubblelin(n, m-1)


for _ in range(10):
    tc = int(input())
    n, m = map(int, input().split())
    result = dubblelin(n, m)

    print(f"#{tc} {result}")