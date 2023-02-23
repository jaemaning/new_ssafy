def postorder(t):
    # 트리의 범위 => 노드의 개수
    # 트리의 범위 밖이면
    # return 0
    # 트리의 범위 안이면
    if t * 2 <= n+1:
        # 현재 내 값(tree[t]) 가 0이 아니면
        # return tree[t]
        # 0 이면 계산
        left = postorder(t * 2)
        right = postorder(t * 2 + 1)
        if not tree[t]:
            tree[t] = left + right

    return tree[t]


T = int(input())

for tc in range(1, T + 1):
    n, m, l = map(int, input().split())
    tree = [0] * (n*2)

    for _ in range(m):
        leaf, num = map(int, input().split())
        tree[leaf] = num

    ans = postorder(l)
    print(f"#{tc} {ans}")
