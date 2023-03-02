# 사랑의 카운슬러
import sys
sys.stdin = open('input.txt','r')


def comb(n,visited):
    global min_v

    if len(rlt) == n//2:
        first_x = first_y = second_x = second_y = 0
        for i in range(n):
            if visited[i]:
                first_x += n_list[i][0]
                first_y += n_list[i][1]
            else:
                second_x += n_list[i][0]
                second_y += n_list[i][1]
        min_v = min(min_v, (first_x-second_x)**2 + (first_y-second_y)**2)
        return

    start = n_list.index(rlt[-1]) if rlt else 0
    for i in range(start, n):
        if visited[i] == 0:
            visited[i] = 1
            rlt.append(n_list[i])
            comb(n, visited)
            visited[i] = 0
            rlt.pop()


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    n_list = []
    visited = [0] * n
    result = []
    rlt = []
    min_v = 9999999999999999

    for _ in range(n):
        n_list.append(list(map(int,input().split())))

    comb(n,visited)
    print(f'#{tc} {min_v}')