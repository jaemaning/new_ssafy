# 이진 탐색 다시 풀어보기 연습

def inorder(node):
    global cnt

    if node <= n:
        inorder(node*2)

        tree[node] = cnt
        cnt += 1

        inorder(node*2+1)


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    tree = [0] * (n+1)
    cnt = 1
    inorder(1)
    print("#{} {} {}".format(tc, tree[1], tree[n//2]))

