T = int(input())

for tc in range(1,T+1):
    n = float(input())
    ans = ""

    while n:
        n *= 2
        if n >= 1:
            n = n-1
            ans += "1"
        else:
            ans += "0"

        if len(ans) >= 13:
            ans = "overflow"
            break


    print(f"#{tc} {ans}")
