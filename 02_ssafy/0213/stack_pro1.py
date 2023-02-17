import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    s = input()
    top = -1
    stack = [0] * 100
    result = 1

    for c in s:
        if c == "(" or c == "{" or c == "[":
            top += 1
            stack[top] = c
        elif top > -1:
            if c == ")":
                top -= 1
                if stack[top + 1] != "(":
                    result = 0
                    break
            elif c == "}":
                top -= 1
                if stack[top + 1] != "{":
                    result = 0
                    break
            elif c == "]":
                top -= 1
                if stack[top + 1] != "[":
                    result = 0
                    break
        elif top == -1 and (c == ")" or c == "}" or c == "]"):
            result = 0
            break
    else:
        if top == -1:
            result = 1
        else:
            result = 0

    print(f"#{tc} {result}")