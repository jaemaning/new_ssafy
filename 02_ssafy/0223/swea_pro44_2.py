# 노드의 합

T = int(input())

for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    tree = [0] * (n+1)

    for _ in range(m):
        leaf_idx, num = map(int,input().split())
        tree[leaf_idx] = num
        while leaf_idx:
            leaf_idx //= 2
            tree[leaf_idx] += num

    print(f"#{tc} {tree[l]}")
