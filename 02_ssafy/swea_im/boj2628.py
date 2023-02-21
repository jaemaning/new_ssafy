# boj 2628 - 종이자르기

c, r = map(int, input().split())
n = int(input())
k = [[0],[0]]

for _ in range(n):
    tp, num = map(int,input().split())
    k[tp].append(num)

k[0].append(r)
k[1].append(c)

k[0].sort()
k[1].sort()
# print(k[1])

max_cntx = -1
for i in range(len(k[0])-1):
    if k[0][i+1] - k[0][i] > max_cntx:
        max_cntx = k[0][i+1] - k[0][i]

max_cnty = -1
for i in range(len(k[1])-1):
    if k[1][i+1] - k[1][i] > max_cnty:
        max_cnty = k[1][i+1] - k[1][i]

print(max_cntx * max_cnty)