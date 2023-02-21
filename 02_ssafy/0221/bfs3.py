dx = [-1,1,0,0]
dy = [0,0,-1,1]


n = 6

maze = [
    [0,0,0,0,0,0],
    [0,1,1,1,1,0],
    [0,0,0,1,0,0],
    [1,1,0,1,0,1],
    [0,0,0,1,0,0],
    [0,1,0,1,1,3]]

def bfs(sx,sy):
    '''
    sx = 시작 x 위치
    sy = 시작 y 위치
    '''
    q = []
    visited = [[False] * n for _ in range(n)]
    q.append((sx,sy))
    visited[sx][sy] = True

    day = 0
    while q:
        
        size = len(q)

        for _ in range(size):
            x, y = q.pop(0)
            print(x, y)
            if maze[x][y] == 3:
                print(f'탈출 : {day}', (x, y))
                return

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] != 1 and visited[nx][ny] == False:
                    q.append((nx,ny))
                    visited[nx][ny] = True
        
        day += 1
            

bfs(0,0)