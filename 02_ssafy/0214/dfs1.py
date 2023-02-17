def dfs(s, v):
    # 초기화
    visited = [False] * (v + 1)
    stack = []
    # 현재 방문한 정점을 i 라고 하자
    i = s
    visited[s] = True
    print(node[i])

    while 1:
        # 인접리스트 시
        for w in adjL[i]:
            if visited[w] == False:
                stack.append(w)
                i = w
                print(node[i])
                visited[w] = True
        else:
            # 내가 최근에 방문했던 정점을 스택에 넣어 놓았음.
            # 하나 꺼내서 그 위치로 돌아간다.
            if stack:
                i = stack.pop()
            # 스택이 비어 있는 경우 => 탐색 종료
            else:
                break
        # 인접 행렬 시
        '''for w in range(1, v + 1):
            if adjA[i][w] == 1 and visited[w] == False:
                # w는 길이 있으니까 현재 위치 i를 스택에 저장
                stack.append(i)
                # 현재위치 i를 다음 위치 w로 변경
                i = w
                print(node[i])
                visited[w] = True
                # 현재 위치 i에서 더 확인할 필요가 없음
                break'''
        # 내가 i에서 탐색을 해봤는데 더이상 탐색할 정점이 없다.


    return


# 현재 정점 i에서 탐색할 수 있는 다음 정점 w에 대해서
#  w로 가는 길이 있고, w를 방문한적이 없다면 w 방문


# 인접행렬, 인접리스트
# 인접 행렬
#       x  A  B  C  D  E  F  G
adj = [[0, 0, 0, 0, 0, 0, 0, 0],  # X
       [0, 0, 1, 1, 0, 0, 0, 0],  # A
       [0, 1, 0, 0, 1, 1, 0, 0],  # B
       [0, 1, 0, 0, 0, 1, 0, 0],  # C
       [0, 0, 1, 0, 0, 0, 1, 0],  # D
       [0, 0, 1, 1, 0, 0, 1, 0],  # E
       [0, 0, 0, 0, 1, 1, 0, 1],  # F
       [0, 0, 0, 0, 0, 0, 1, 0], ]  # G

'''
정점의 개수, 간선의 개수 -> 간선 정보
7 8
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7
'''
v, e = map(int, input().split())
adjA = [[0] * (v + 1) for _ in range(v + 1)]
# 인접 리스트
adjL = [[] for _ in range(v + 1)]
for i in range(e):
    start, to = map(int, input().split())
    # 인접 리스트
    adjL[start].append(to)
    # 무향 그래프 (방향이 없는 그래프) 만 아래 추가
    adjL[to].append(start)

    # 인접 행렬
    adjA[start][to] = 1
    # 무향 그래프 (방향이 없는 그래프) 만 아래 추가
    adjA[start][to] = 1

node = ["", "A", "B", "C", "D", "E", "F", "G"]

dfs(1, 7)
