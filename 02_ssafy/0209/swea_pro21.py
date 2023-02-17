T = int(input())

for tc in range(1, T+1):
    s = input().strip()
    result = 0

    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            break
    else:
        result = 1

    print(f"#{tc} {result}")