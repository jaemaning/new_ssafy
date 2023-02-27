# 각자리수 2진수

T = int(input())

for tc in range(1, T + 1):
    n, num = input().split()
    n = int(n)
    result = ""

    # 16
    for s in num:
        cnt = 0
        ans = ""
        if s.isdigit():
            s = int(s)
            while cnt != 4:
                ans += str(s % 2)
                s //= 2
                cnt += 1

            result += ans[::-1]

        else:
            s = ord(s) - 55
            while cnt != 4:
                ans += str(s % 2)
                s //= 2
                cnt += 1

            result += ans[::-1]


    print(f'#{tc} {result}')
