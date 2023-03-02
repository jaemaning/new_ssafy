# 현주의 상자 바꾸기

T = int(input())

for tc in range(1, T + 1):
    n, q = map(int, input().split())
    n_list = [0 for _ in range(n + 1)]

    for i in range(1, q + 1):
        l, r = map(int, input().split())
        for j in range(l,r+1):
            n_list[j] = i

    print(f'#{tc}', end=" ")
    for i in range(1,n+1):
        print(n_list[i], end=" ")

    print()
