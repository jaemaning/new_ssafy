# 사랑의 카운슬러
import sys
sys.stdin = open('input.txt','r')


def perm(n,visited):

    if len(rlt) == n:
        result.append(rlt[:])
        return

    for i in range(n):
        if visited[i] == 0:
            # print(visited)
            visited[i] = 1
            rlt.append(n_list[i])
            perm(n, visited)
            visited[i] = 0
            rlt.pop()


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    n_list = []
    visited = [0] * n
    result = []
    rlt = []

    for _ in range(n):
        n_list.append(list(map(int,input().split())))

    perm(n,visited)
    print(result)