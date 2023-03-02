# 새로운 불면증 치료법

T = int(input())

for tc in range(1, T + 1):
    n = input()
    nn = n
    len_n = len(n)
    num_list = set()

    while len(num_list) != 10:
        for i in str(nn):
            num_list.add(i)

        nn = int(nn) + int(n)

    print(f'#{tc} {nn - int(n)}')
