'''
s = input()
stk = [0] * (len(s) + 1)
icp = {"*": 2, "/": 2, "+": 1, "-": 1, ""}
isp = {"*": 2, "/": 2, "+": 1, "-": 1}

# 토큰하나 가져오기
for c in s:
    if c in icp:
        pass
    else:

'''
icp = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 3}
isp = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}


def get_postfix(infix):
    postfix = ""  # 결과로 출력할 후위 표기식
    stack = []

    # infix 안에 있는 문자들을 하나씩 떼와서 처리
    for c in infix:
        # 피연산자인경우
        if "0" <= c <= "9":
            postfix += c
        # 연산자인 경우
        else:
            # 닫는 괄호가 나오는 경우
            if c == ")":
                # 여는 괄호가 나올때 까지 pop 해서 결과에 출력
                while stack:
                    char = stack.pop()
                    if char == "(":
                        break
                    postfix += char
            # 다른 연산자가 나오는 경우
            else:
                # 현재 토큰(연산자)의 우선순위보다
                # stack[top] 의 우선순위가 같거나 높으면 계속 pop
                while stack and isp[stack[-1]] >= icp[c]:
                    postfix += stack.pop()
                # 아니면 push
                stack.append(c)
    # 남아 있는 연산자 출력
    while stack:
        postfix += stack.pop()

    return postfix


print(get_postfix("2+3*4/5"))

# 후위 표기식 결과 계산


def get_result(postfix):
    stack = []

    for c in postfix:
        # 피연산자를 만나면 스택에 넣기
        if "0" <= c <= "9":
            stack.append(int(c))

        # 연산자를 만나면 피연산자를 두개 꺼내서 계산
        else:
            b = stack.pop()
            a = stack.pop()

            if c == "+":
                rlt = a+b
            elif c== "-":
                rlt = a-b
            elif c == "*":
                rlt = a*b
            elif c == "/":
                rlt = a/b

            stack.append(rlt)

    return stack[0]


print(get_result(get_postfix("2+3*4/5")))