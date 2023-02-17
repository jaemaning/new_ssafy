# boj 10799 쇠막대기

s = input().strip()
stack = []
opener_cnt = 0
cnt = 0

for c in s:
    # 스택에 쌓기.
    stack.append(c)
    # 닫힘이 나오면 두가지 경우이며 opener_cnt 를 감소시킨다.
    # 1. 레이저
    # 2. 막대 끝
    if c == ")":
        opener_cnt -= 1
        # 레이저인 경우 여태까지 열려있는 막대들의 숫자만큼 더한다.
        if stack[-2] == "(":
            cnt += opener_cnt
        # 막대 끝인 경우 막대숫자 1개를 더해준다.
        else:
            cnt += 1
    # 열림이 나오면 열림 숫자를 세기 위한 opener_cnt 를 증가시킨다.
    else:
        opener_cnt += 1

print(cnt)
