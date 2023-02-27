# 토마토
def tomato(q):
    while q:
        z, y, x = q.popleft()


from collections import deque

x, y, z = map(int, input().split())

tomato_box = [[list(map(int, input().split())) for _ in range(y)] for _ in range(z)]

q = deque()

print(tomato_box)

for i in range(x):
    for j in range(y):
        for k in range(z):
            if tomato_box[k][j][i] == "1":
                q.append((k, j, i))
