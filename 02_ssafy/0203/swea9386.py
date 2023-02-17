import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    n_list = input()
    cnt = 0
    max_v = 0
    for num in n_list:
        num = int(num)
        if num:
            cnt += 1
        else:
            if max_v < cnt:
                max_v = cnt
            cnt = 0

    # 마지막까지 1이 이어져 0이 발견되지 않는 경우를 대비
    # 마지막으로 값을 한번더 체크
    if max_v < cnt:
        max_v = cnt

    print(f"#{tc} {max_v}")
