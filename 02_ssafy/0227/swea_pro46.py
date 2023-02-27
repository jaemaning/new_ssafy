# 이진수

T = int(input())

for tc in range(1, T + 1):
    n, num = input().split()
    n = int(n)
    ans = 0
    result = ""

    # 16 => 10
    for s in num:
        if s.isdigit():
            ans += int(s) * (16**(n-1))
        else:
            s = ord(s) - 55
            ans += s * (16**(n-1))

        n -= 1

    # 10 => 2
    while ans:
        result += str(ans % 2)
        ans //= 2

    print(f'#{tc} {"0"+result[::-1]}')