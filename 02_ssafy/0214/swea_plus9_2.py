# import sys

# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    money = 0
    last_max = 0

    for i in n_list[::-1]:
        if last_max < i:
            last_max = i
        else:
            money += last_max-i
    
    print(f"#{tc} {money}")


