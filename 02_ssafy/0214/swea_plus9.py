import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    s = input().strip()
    stack = []
    open_cnt = 0
    result = 0

    for c in s:
        stack.append(c)
        if c == "(":
            open_cnt += 1
        else:
            open_cnt -= 1
            # 쇠막대 닫힘
            if stack[-2] == ")":
                result += 1
            # 레이저
            else:
                result += open_cnt

    print(result)