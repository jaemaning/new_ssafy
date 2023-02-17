import sys

sys.stdin = open('input.txt', 'r')

def midtoend(s):
    isp = {"+" : 1, "*" : 2}
    result = []
    stack = []

    for c in s:
        if str.isdigit(c):
            result.append(c)
        else:
            while stack and isp[stack[-1]] >= isp[c]:
                result.append(stack.pop())
            stack.append(c)
    while stack:
        result.append(stack.pop())

    return result


def endtomid(res):
    num = 0
    stack = []
    for c in res:
        # 숫자이면
        if str.isdigit(c):
            stack.append(int(c))
        else:
            b = stack.pop()
            a = stack.pop()

            if c == "+":
                stack.append(a+b)
            elif c == "*":
                stack.append(a*b)

    return stack[0]


for tc in range(1, 11):
    n = int(input())

    s = list(input().strip())

    res = midtoend(s)
    result = endtomid(res)

    print(f"#{tc} {result}")
