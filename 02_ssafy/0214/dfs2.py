# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, n):
    # 방문 체크 배열
    visited = [[0] * n for _ in range(n)]
    stack = []
    visited[x][y] = 1

    while 1:
        # 현재 위치가 도착지점이라면 탐색 종료
        if arr[x][y] == 3:
            print("도착")
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 다음 위치 계산 후, 갈 수 있는 곳인지 그리고 이전에 방문하지 않았던 곳인지
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 1 and not visited[nx][ny]:
                # 돌아올 위치를 스택에 저장 (현재위치)
                stack.append((x, y))
                visited[nx][ny] = 1
                # 다음 위치로 이동
                x, y = nx, ny
                # dfs 특성을 위해 break
                break
            # 4방향을 모두 살펴봤는데 갈 수 있는 곳인 없다?
        else:
            if stack:
                x, y = stack.pop()
            else:
                break



# 0은 길, 1은 벽, 3은 도착지점
arr = [[0, 0, 0, 0, 1, 3],
       [1, 1, 1, 0, 1, 0],
       [0, 0, 1, 0, 1, 0],
       [0, 1, 1, 0, 1, 0],
       [0, 1, 1, 0, 1, 0],
       [0, 0, 0, 0, 0, 0], ]
