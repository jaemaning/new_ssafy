import sys
sys.stdin = open('../0222/input.txt', 'r')


def inorder(t):
    # t 노드가 존재 한다면
    if tree[t]:
    # 왼쪽 방문
        inorder(tree[t][0]) # none 리턴될 때 처리
    # 데이터처리
    #     print(f"이거 뭐야 ? : {tree[t][0]}")
    #     print(f"너는 뭐야 ? : {n_lst[tree[t][0]]}")
        result.append(n_lst)
    # if len(tree[t]) == 2:
    # 오른쪽 방문
        inorder(tree[t][1])
        # result.append(n_lst[tree[t][0]])
    else:



for tc in range(1,11):
    n = int(input())
    tree = [[] for _ in range(n+1)]
    n_lst = [0]
    result = []

    for _ in range(n):
        p, *c = input().split()
        p = int(p)
        n_lst.append(c[0])

        if len(c) == 3:
            tree[p].append(int(c[1]))
            tree[p].append(int(c[2]))




    print(n_lst)
    print(tree)
    inorder(1)
    print(result)
