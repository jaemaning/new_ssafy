T = int(input())

for tc in range(1, T + 1):
    n, hex_num = input().split()
    n = int(n)
    ans = ""

    for i in range(n):
        num = int(hex_num[i], 16)
        for j in range(3,-1,-1):
            if num & (2**j):
                ans += "1"
            else:
                ans += "0"

    print(f'#{tc} {ans}')
