# 성공적인 공연 기획
'''
5
11111
09
110011
1
02011
'''

T = int(input())

for tc in range(1, T + 1):
    n_list = list(map(int,list(input())))

    cnt = 0
    ans = 0
    for idx, i in enumerate(n_list):
        while idx > cnt:
            ans += 1
            cnt += 1

        if idx <= cnt:
            cnt += i

    print(f'#{tc} {ans}')
