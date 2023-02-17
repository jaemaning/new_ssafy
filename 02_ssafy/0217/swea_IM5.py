# 원재의 메모리 복구하기
# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    num = input()[::-1]
    cnt = 0
    # 초기값 설정
    flag = int(num[0])
    if flag == 1:
        cnt += 1

    for c in num:
        c = int(c)
        # c == 1
        if c and c != flag:
            flag = c
            cnt += 2
        # c == 0 일때 무작정 돌면 안된다
        # c == 0 이면 왼쪽에 1이 있을때 2번 돌리자
        elif c == 0 and c != flag:
            flag = c

    print(f"#{tc} {cnt}")
