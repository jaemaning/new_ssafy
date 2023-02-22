'''
4
1 2 1 3 3 4 3 5
'''
n = 5
e = int(input())
tree = list(map(int, input().split()))

# 1. 인덱스 번호 => 부모 노드의 번호
child_left = [0] * (n + 1)
child_right = [0] * (n + 1)

for i in range(e):
    parent = tree[i * 2]
    child = tree[i * 2 + 1]

    # 왼쪽 자식이 없다면 왼쪽 자식부터 채우기
    if child_left[parent] == 0:
        child_left[parent] = child
    # 왼쪽 자식이 있다면 오른쪽 자식 채우기
    else:
        child_right[parent] = child

print(child_left)
print(child_right)

# 2. 인덱스 번호가 => 자식노드의 번호
parent = [0] * (n + 1)
for i in range(e):
    p = tree[i*2]
    c = tree[i*2+1]
    parent[c] = p

print(parent)

# 5번 노드의 조상 노드 탐색
now = 5

# parent[now] == 0  이면 now 가 root 노드 이기 떄문에 부모 노드가 존재 하지 않는다.
while parent[now] != 0:
    print(parent[now])
    now = parent[now]
