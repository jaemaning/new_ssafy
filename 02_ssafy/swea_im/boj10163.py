# boj 10163 - 색종이

n = int(input())
box = [[0] * 1001 for _ in range(1001)]

for i in range(1,n+1):
    x, y, w, h = map(int, input().split())

    for hy in range(h):
        for wx in range(w):
            box[y+hy][x+wx] = i

for num in range(1, n+1):
    cnt = 0
    for i in range(1001):
        cnt += box[i].count(num)
    print(cnt)
