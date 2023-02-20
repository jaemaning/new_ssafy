t = 10
for tc in range(1, t + 1):
    _ = int(input())
    code = list(map(int, input().split()))

    i = 1
    # c 가 0이 아닌동안
    while True:
        c = code.pop(0) - i
        if c < 0:
            c = 0
        # c 가 0 보다 크다면 code 에 넣기
        code.append(c)
        # i 값 1 ~ 5 반복
        i = (i % 5) + 1
        if c == 0:
            break
    # q 리스트 풀어서 출력
    print(f'#{tc}', *q)