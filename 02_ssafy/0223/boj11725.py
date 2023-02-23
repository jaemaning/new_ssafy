# 트리의 부모 찾기
def check_p(p):

    visited[p] = True

    for i in tree[p]:
        if visited[i] == False:
            result[i] = p
            check_p(i)

    return


n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)

visited = [1] * (n+1)
result = [0] * (n+1)

visited[0] = 0
p_lst = [1]
while sum(visited):

    for p in p_lst:
        visited[p] = 0
        for i in tree[p]:
            if visited[i] == 1:
                result[i] = p
                p_lst.append(i)


for i in range(2,len(result)):
    print(result[i])