import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    n_arr = list(map(list, zip(*arr)))
    print(arr)
    print(n_arr)

    mx_cnt = 2
    for lst in arr:
        cnt = 0
        for i in lst:
            # 1 만났을때
            if i == 1:
                cnt += 1
            # 0 만났을때
            else:
                if cnt > mx_cnt:
                    mx_cnt = cnt
                cnt = 0

        if cnt > mx_cnt:
            mx_cnt = cnt

    n_mx_cnt = 2
    for lst in n_arr:
        n_cnt = 0
        for j in lst:
            if j == 1:
                n_cnt += 1
            else:
                if n_cnt > n_mx_cnt:
                    n_mx_cnt = n_cnt
                n_cnt = 0

        if n_cnt > n_mx_cnt:
            n_mx_cnt = n_cnt


    print(f'#{tc} {mx_cnt, n_mx_cnt}')