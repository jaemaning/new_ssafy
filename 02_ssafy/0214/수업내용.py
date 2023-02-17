'''def f(i, k):  # i : 현재위치, k : 목표치 - 기본형태
    if i == k:
        print(B)
        return
    else:
        B[i] = A[i]
        f(i + 1, k)


A = [10, 20, 30]
B = [0] * 3
f(0, len(A))
'''
'''
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''
'''n = 7  # 노드 수
m = 8  # 간선 수
graphs = [[] for _ in range(n + 1)]
check_list = [False] * (n + 1)
result = []

for _ in range(m):
    x, y = map(int, input().split())
    graphs[x].append(y)
    graphs[y].append(x)
print(graphs)


def dfs(i):
    check_list[i] = True  # 방문처리
    result.append(i)

    for j in graphs[i]:
        if not check_list[j]:
            dfs(j)'''


'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 저장 방식
adjL = [[] for _ in range(V + 1)]  # 인접리스트 저장 방식

for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]

    # 인접행렬 저장 방식
    adjM[v1][v2] = 1
    adjM[v2][v1] = 1

    # 인접리스트 저장 방식
    adjL[v1].append(v2)
    adjL[v2].append(v1)

print(adjM)