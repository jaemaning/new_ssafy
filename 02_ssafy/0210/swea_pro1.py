import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    n = int(input())
    s = ""
    for _ in range(n):
        ci, ki = input().strip().split()
        s += ci * int(ki)

    print(f"#{tc}")
    for i in range((len(s)//10)+1):
        start = i*10
        end = (i+1)*10
        if end <= len(s):
            print(s[start:end])
        else:
            print(s[start:])
