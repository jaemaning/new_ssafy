# 장훈이의 높은 선반
import sys
sys.stdin = open('input.txt','r')


def comb(num):
    global min_h

    '''
    :param n: 몇명을 고를지
    :return: 없음 
    '''

    if len(rlt) == num:
        height = 0
        for i in rlt:
            height += h_list[i]

        if height >= b:
            min_h = min(min_h,height)
        return

    start = h_idx_list.index(rlt[-1]) if rlt else 0
    for i in range(start,n):
        if not visited[i]:
            visited[i] = 1
            rlt.append(i)
            comb(num)
            visited[i] = 0
            rlt.pop()


T = int(input())

for tc in range(1, T+1):
    n, b = map(int,input().split())

    h_list = list(map(int,input().split()))

    min_h = 10000 * 20

    rlt = []
    visited = [0] * n
    h_idx_list = [i for i in range(n)]

    for i in range(1,n+1):
        comb(i)
        if min_h == b:
            break

    print(f'#{tc} {min_h-b}')