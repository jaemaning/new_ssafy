# 토마토
def tomato(q):
    day = 1
    # 상 하 좌 우 위 아래
    dx = (0, 0, -1, 1, 0, 0)
    dy = (-1, 1, 0, 0, 0, 0)
    dz = (0, 0, 0, 0, 1, -1)

    while q:
        day += 1

        for _ in range(len(q)):
            sz, sy, sx = q.popleft()

            for i in range(6):
                nx = sx + dx[i]
                ny = sy + dy[i]
                nz = sz + dz[i]

                if 0 <= nx < x and 0 <= ny < y and 0 <= nz < z and tomato_box[nz][ny][nx] == 0:
                    tomato_box[nz][ny][nx] = day
                    q.append((nz,ny,nx))



from collections import deque

x, y, z = map(int, input().split())

tomato_box = [[list(map(int, input().split())) for _ in range(y)] for _ in range(z)]

q = deque()

for i in range(x):
    for j in range(y):
        for k in range(z):
            if tomato_box[k][j][i] == 1:
                q.append((k, j, i))

tomato(q)
max_v = -1
flag = 0
for j in range(y):
    for k in range(z):
        if 0 in tomato_box[k][j]:
            flag = 1
            break
        else:
            max_v = max(max_v, max(tomato_box[k][j]))
    else:
        continue
    break


if flag:
    print(-1)
else:
    print(max_v-1)