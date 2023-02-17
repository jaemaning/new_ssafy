import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    p, target_a, target_b = map(int, input().split())

    if target_a <= p and target_b <= p:
        start, end = 1, p
        cnt_a = cnt_b = 0
        while start <= end:
            middle = (start + end) // 2

            if middle == target_a:
                break
            elif target_a > middle:
                cnt_a += 1
                start = middle
            else:
                cnt_a += 1
                end = middle

        start, end = 1, p

        while start <= end:
            middle = (start + end) // 2

            if middle == target_b:
                break
            elif target_b > middle:
                cnt_b += 1
                start = middle
            else:
                cnt_b += 1
                end = middle
    else:
        if target_a > p and target_b > p:
            result = 0
        else:
            if target_a > p:
                result = "B"
            else:
                result = "A"

    if cnt_a < cnt_b:
        result = "A"
    elif cnt_a > cnt_b:
        result = "B"
    else:
        result = 0

    print(f"#{tc} {result}")




