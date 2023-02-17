# Forth

# 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    s = list(input().split())
    stk = []
    result = 0

    for c in s:
        if c == ".":
            if len(stk) == 1:
                result = stk[0]
            else:
                result = "error"
            break

        if str.isdigit(c):
            stk.append(int(c))
        else:
            if len(stk) > 1:
                b = stk.pop()
                a = stk.pop()

                if c == "+":
                    ans = a + b
                elif c == "-":
                    ans = a - b
                elif c == "*":
                    ans = a * b
                elif c == "/":
                    ans = a // b

                stk.append(ans)

            else:
                result = "error"
                break

    print(f"#{tc} {result}")
