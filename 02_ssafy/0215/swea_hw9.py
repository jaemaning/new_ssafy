# 계산기
import sys
sys.stdin = open('input.txt', 'r')


def midtoend(s):
    stk = []
    result = ""
    for c in s:
        if str.isdigit(c):
            result += c
        else:
            if stk:
                result += "+"
            else:
                stk.append(c)

    while stk:
        result += stk.pop()

    return result


def endtomid(s):
    stk = []
    result = 0
    for c in s:
        if str.isdigit(c):
            stk.append(int(c))
        else:
            if len(stk) > 1:
                b = stk.pop()
                a = stk.pop()

                # 어차피 + 밖에 없음
                result += a
                result += b

    while stk:
        result += stk.pop()

    return result


for tc in range(1,11):
    n = int(input())
    s = input().strip()

    rlt = midtoend(s)
    result = endtomid(rlt)

    print(f"#{tc} {result}")
