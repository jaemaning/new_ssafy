# boj 2606 바이러스
import sys
input = sys.stdin.readline

def dfs(start):

    check_list[start] = False
    for i in com_list[start]:
        if check_list[i]:
            check_list[i] = False
            result.append(i)
            dfs(i)


computers = int(input())
connections = int(input())
com_list = [[] for _ in range(computers+1)]
check_list = [True] * (computers+1)
result = []

for _ in range(connections):
    start, end = map(int, input().split())
    com_list[start].append(end)
    com_list[end].append(start)

dfs(1)
print(len(result))