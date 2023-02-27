import sys
sys.stdin = open('input.txt', 'r')

def dfs(start):

    visited[start] = 1

    next = adj_list[start]

    for i in next:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)


T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    adj_list = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    visited[0] = 1
    cnt = 1

    # 인접리스트 만들기
    for _ in range(m):
        start, end = map(int, input().split())
        adj_list[start].append(end)
        adj_list[end].append(start)

    # 1번 인덱스부터 검사, 다른 인덱스부터 시작해도 상관없음
    s = 1
    while True:
        dfs(s)

        # 만약 모두 방문 했으면 브레이크
        if sum(visited) == n+1:
            break

        # 하나라도 방문 안하게 있으면 해당 인덱스 찾아서 다시 dfs 진행
        s = visited.index(0)

        # 무리 숫자 세기 위해 카운트
        cnt += 1

    print(f'#{tc} {cnt}')
