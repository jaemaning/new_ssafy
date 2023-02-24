import sys
sys.stdin = open('0221\input.txt', 'r')

# 3 . 후위 순회 (postorder) L-R-V
def postorder(t):
    # 노드 인덱스를 담은 리스트에 다음 노드로 갔는데 빈리스트라면?
    if not node_idx[t]:
        return node_v[t]
    else:

    # 왼쪽 방문
        left = postorder(node_idx[t][0])
    # 오른쪽 방문
        right = postorder(node_idx[t][1])

    # 결과 계산
        if node_v[t] == '+':
            return left + right
        elif node_v[t] == '-':
            return left - right
        elif node_v[t] == '*':
            return left * right
        elif node_v[t] == '/':
            return left / right


for tc in range(1, 11):
    n = int(input())
    node_idx = [[] for _ in range(n+1)]
    node_v = [0] * (n+1)

    for _ in range(n):
        p, *c = input().split()
        p = int(p)
        # print(c)
        if len(c) > 2:
            node_v[p] = c[0]
            node_idx[p].append(int(c[1]))
            node_idx[p].append(int(c[2]))
        else:
            node_v[p] = int(c[0])
        

    ans = postorder(1)
    print(f"#{tc} {int(ans)}")

