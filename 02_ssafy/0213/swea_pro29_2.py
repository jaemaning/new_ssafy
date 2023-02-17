import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    stack = []
    s = input().strip()

    for c in s:
        stack.append(c)

        if len(stack) >= 2 and stack[-2] == c:
            del stack[-2:]

    print(f"#{tc} {len(stack)}")