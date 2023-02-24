# 트리의 지름

# 정점의 개수
v = int(input())
# node
node = [[]for _ in range(v+1)]

for _ in range(v):
    n, *c = map(int,input().split())

    for i in range(len(c)//2):
        node[i*2]