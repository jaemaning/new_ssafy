# 10일차- 비밀번호
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    n, m = input().split()
    stack = []

    for c in m:
        stack.append(c)
        if len(stack) >= 2 and stack[-2] == c:
            del stack[-2:]

    print(f'#{tc} {"".join(stack)}')
